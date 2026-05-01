from __future__ import annotations

import struct
import zlib
from pathlib import Path
from typing import Any


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def _paeth(a: int, b: int, c: int) -> int:
    p = a + b - c
    pa = abs(p - a)
    pb = abs(p - b)
    pc = abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    if pb <= pc:
        return b
    return c


def _bytes_per_pixel(color_type: int) -> int:
    if color_type == 0:
        return 1
    if color_type == 2:
        return 3
    if color_type == 4:
        return 2
    if color_type == 6:
        return 4
    return 0


def _decode_png_scanlines(raw: bytes, width: int, height: int, bpp: int) -> bytes:
    stride = width * bpp
    out = bytearray()
    previous = bytearray(stride)
    offset = 0
    for _row in range(height):
        filter_type = raw[offset]
        offset += 1
        scanline = bytearray(raw[offset : offset + stride])
        offset += stride
        for i in range(stride):
            left = scanline[i - bpp] if i >= bpp else 0
            up = previous[i]
            upper_left = previous[i - bpp] if i >= bpp else 0
            if filter_type == 1:
                scanline[i] = (scanline[i] + left) & 0xFF
            elif filter_type == 2:
                scanline[i] = (scanline[i] + up) & 0xFF
            elif filter_type == 3:
                scanline[i] = (scanline[i] + ((left + up) // 2)) & 0xFF
            elif filter_type == 4:
                scanline[i] = (scanline[i] + _paeth(left, up, upper_left)) & 0xFF
            elif filter_type != 0:
                raise ValueError(f"unsupported_png_filter:{filter_type}")
        out.extend(scanline)
        previous = scanline
    return bytes(out)


def analyze_png(path: Path, *, black_threshold: int = 3, min_variance: float = 0.01) -> dict[str, Any]:
    if not path.exists():
        return {"success": False, "file_path": str(path), "error": "file_not_found"}
    raw = path.read_bytes()
    if not raw.startswith(PNG_SIGNATURE):
        return {"success": False, "file_path": str(path), "error": "not_png"}

    offset = len(PNG_SIGNATURE)
    width = 0
    height = 0
    bit_depth = 0
    color_type = 0
    palette: list[tuple[int, int, int]] = []
    idat = bytearray()

    while offset + 8 <= len(raw):
        length = struct.unpack(">I", raw[offset : offset + 4])[0]
        chunk_type = raw[offset + 4 : offset + 8]
        chunk_data = raw[offset + 8 : offset + 8 + length]
        offset += 12 + length
        if chunk_type == b"IHDR":
            width, height, bit_depth, color_type = struct.unpack(">IIBB", chunk_data[:10])
        elif chunk_type == b"PLTE":
            palette = [
                tuple(chunk_data[i : i + 3])  # type: ignore[arg-type]
                for i in range(0, len(chunk_data), 3)
                if i + 2 < len(chunk_data)
            ]
        elif chunk_type == b"IDAT":
            idat.extend(chunk_data)
        elif chunk_type == b"IEND":
            break

    if width <= 0 or height <= 0:
        return {"success": False, "file_path": str(path), "error": "invalid_dimensions"}
    if bit_depth != 8:
        return {
            "success": False,
            "file_path": str(path),
            "width": width,
            "height": height,
            "error": "unsupported_bit_depth",
            "bit_depth": bit_depth,
        }

    try:
        decompressed = zlib.decompress(bytes(idat))
        bpp = _bytes_per_pixel(color_type)
        if color_type == 3:
            decoded = _decode_png_scanlines(decompressed, width, height, 1)
            pixels: list[tuple[int, int, int, int]] = []
            for index in decoded:
                r, g, b = palette[index] if index < len(palette) else (0, 0, 0)
                pixels.append((r, g, b, 255))
        else:
            if bpp <= 0:
                return {
                    "success": False,
                    "file_path": str(path),
                    "width": width,
                    "height": height,
                    "error": "unsupported_color_type",
                    "color_type": color_type,
                }
            decoded = _decode_png_scanlines(decompressed, width, height, bpp)
            pixels = []
            for i in range(0, len(decoded), bpp):
                if color_type == 0:
                    v = decoded[i]
                    pixels.append((v, v, v, 255))
                elif color_type == 2:
                    pixels.append((decoded[i], decoded[i + 1], decoded[i + 2], 255))
                elif color_type == 4:
                    v = decoded[i]
                    pixels.append((v, v, v, decoded[i + 1]))
                else:
                    pixels.append((decoded[i], decoded[i + 1], decoded[i + 2], decoded[i + 3]))
    except Exception as exc:
        return {
            "success": False,
            "file_path": str(path),
            "width": width,
            "height": height,
            "error": f"png_decode_failed:{exc}",
        }

    pixel_count = len(pixels)
    if pixel_count == 0:
        return {"success": False, "file_path": str(path), "width": width, "height": height, "error": "no_pixels"}

    luminance_values = [(r + g + b) / 3.0 for r, g, b, _a in pixels]
    mean = sum(luminance_values) / pixel_count
    variance = sum((value - mean) ** 2 for value in luminance_values) / pixel_count
    non_black = sum(1 for value in luminance_values if value > black_threshold)
    non_transparent = sum(1 for _r, _g, _b, a in pixels if a > 0)
    appears_non_black = non_black > 0 and variance >= min_variance
    appears_non_empty = non_transparent > 0 and appears_non_black

    return {
        "success": True,
        "file_path": str(path),
        "width": width,
        "height": height,
        "bit_depth": bit_depth,
        "color_type": color_type,
        "pixel_count": pixel_count,
        "non_black_pixel_count": non_black,
        "non_transparent_pixel_count": non_transparent,
        "mean_luminance": mean,
        "luminance_variance": variance,
        "appears_non_black": appears_non_black,
        "appears_non_empty": appears_non_empty,
    }


def analyze_bmp(path: Path, *, black_threshold: int = 3, min_variance: float = 0.01) -> dict[str, Any]:
    if not path.exists():
        return {"success": False, "file_path": str(path), "error": "file_not_found"}
    raw = path.read_bytes()
    if len(raw) < 54 or raw[:2] != b"BM":
        return {"success": False, "file_path": str(path), "error": "not_bmp"}
    pixel_offset = int.from_bytes(raw[10:14], "little")
    width = int.from_bytes(raw[18:22], "little", signed=True)
    height = int.from_bytes(raw[22:26], "little", signed=True)
    bpp = int.from_bytes(raw[28:30], "little")
    compression = int.from_bytes(raw[30:34], "little")
    if width <= 0 or height == 0:
        return {"success": False, "file_path": str(path), "error": "invalid_dimensions"}
    if compression != 0 or bpp not in {24, 32}:
        return {
            "success": False,
            "file_path": str(path),
            "width": width,
            "height": abs(height),
            "error": "unsupported_bmp_format",
            "bits_per_pixel": bpp,
            "compression": compression,
        }
    abs_height = abs(height)
    row_stride = ((width * bpp + 31) // 32) * 4
    luminance_values: list[float] = []
    non_transparent = 0
    for row in range(abs_height):
        base = pixel_offset + row * row_stride
        for col in range(width):
            offset = base + col * (bpp // 8)
            if offset + (bpp // 8) > len(raw):
                continue
            b = raw[offset]
            g = raw[offset + 1]
            r = raw[offset + 2]
            a = raw[offset + 3] if bpp == 32 else 255
            luminance_values.append((r + g + b) / 3.0)
            if a > 0:
                non_transparent += 1
    if not luminance_values:
        return {"success": False, "file_path": str(path), "width": width, "height": abs_height, "error": "no_pixels"}
    mean = sum(luminance_values) / len(luminance_values)
    variance = sum((value - mean) ** 2 for value in luminance_values) / len(luminance_values)
    non_black = sum(1 for value in luminance_values if value > black_threshold)
    return {
        "success": True,
        "file_path": str(path),
        "width": width,
        "height": abs_height,
        "bits_per_pixel": bpp,
        "pixel_count": len(luminance_values),
        "non_black_pixel_count": non_black,
        "non_transparent_pixel_count": non_transparent,
        "mean_luminance": mean,
        "luminance_variance": variance,
        "appears_non_black": non_black > 0 and variance >= min_variance,
        "appears_non_empty": non_transparent > 0 and non_black > 0 and variance >= min_variance,
    }


def analyze_jpeg_dimensions(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"success": False, "file_path": str(path), "error": "file_not_found"}
    raw = path.read_bytes()
    if not raw.startswith(b"\xff\xd8"):
        return {"success": False, "file_path": str(path), "error": "not_jpeg"}
    offset = 2
    while offset + 9 < len(raw):
        if raw[offset] != 0xFF:
            offset += 1
            continue
        marker = raw[offset + 1]
        offset += 2
        if marker in {0xD8, 0xD9}:
            continue
        length = int.from_bytes(raw[offset : offset + 2], "big")
        if marker in set(range(0xC0, 0xC4)) | set(range(0xC5, 0xC8)) | set(range(0xC9, 0xCC)) | set(range(0xCD, 0xD0)):
            height = int.from_bytes(raw[offset + 3 : offset + 5], "big")
            width = int.from_bytes(raw[offset + 5 : offset + 7], "big")
            return {
                "success": True,
                "file_path": str(path),
                "width": width,
                "height": height,
                "pixel_statistics_available": False,
                "appears_non_empty": width > 0 and height > 0,
            }
        offset += length
    return {"success": False, "file_path": str(path), "error": "jpeg_dimensions_not_found"}


def analyze_image(path: Path) -> dict[str, Any]:
    suffix = path.suffix.lower()
    if suffix == ".png":
        return analyze_png(path)
    if suffix == ".bmp":
        return analyze_bmp(path)
    if suffix in {".jpg", ".jpeg"}:
        return analyze_jpeg_dimensions(path)
    return {"success": False, "file_path": str(path), "error": "unsupported_image_format"}


def find_visual_artifact_paths(payload: Any) -> list[Path]:
    paths: list[Path] = []

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            for key, item in value.items():
                if isinstance(item, str) and key in {"file_path", "output_file", "screenshot_file", "image_file"}:
                    suffix = Path(item).suffix.lower()
                    if suffix in {".png", ".jpg", ".jpeg", ".bmp"}:
                        paths.append(Path(item))
                else:
                    walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    walk(payload)
    seen: set[str] = set()
    unique: list[Path] = []
    for path in paths:
        key = str(path)
        if key in seen:
            continue
        seen.add(key)
        unique.append(path)
    return unique


def validate_visual_artifacts(payload: Any) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for path in find_visual_artifact_paths(payload):
        results.append(analyze_image(path))
    return results
