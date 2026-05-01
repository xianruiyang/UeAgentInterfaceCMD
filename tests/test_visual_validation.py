import struct
import tempfile
import unittest
import zlib
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli.visual_validation import analyze_bmp, analyze_jpeg_dimensions, analyze_png, find_visual_artifact_paths


def _write_rgb_png(path: Path, width: int, height: int, pixels: list[tuple[int, int, int]]) -> None:
    def chunk(kind: bytes, data: bytes) -> bytes:
        crc = zlib.crc32(kind)
        crc = zlib.crc32(data, crc)
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", crc & 0xFFFFFFFF)

    raw = bytearray()
    for y in range(height):
        raw.append(0)
        for x in range(width):
            raw.extend(pixels[y * width + x])
    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    path.write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(bytes(raw))) + chunk(b"IEND", b""))


def _write_indexed_png_with_up_filter(path: Path) -> None:
    def chunk(kind: bytes, data: bytes) -> bytes:
        crc = zlib.crc32(kind)
        crc = zlib.crc32(data, crc)
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", crc & 0xFFFFFFFF)

    ihdr = struct.pack(">IIBBBBB", 2, 2, 8, 3, 0, 0, 0)
    palette = bytes([0, 0, 0, 255, 0, 0])
    raw = bytes(
        [
            0,
            0,
            1,
            2,
            1,
            0,
        ]
    )
    path.write_bytes(
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", ihdr)
        + chunk(b"PLTE", palette)
        + chunk(b"IDAT", zlib.compress(raw))
        + chunk(b"IEND", b"")
    )


class VisualValidationTests(unittest.TestCase):
    def test_detects_non_black_png(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "shot.png"
            _write_rgb_png(path, 2, 1, [(0, 0, 0), (255, 0, 0)])
            result = analyze_png(path)
            self.assertTrue(result["success"])
            self.assertTrue(result["appears_non_empty"])

    def test_detects_black_png(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "black.png"
            _write_rgb_png(path, 2, 1, [(0, 0, 0), (0, 0, 0)])
            result = analyze_png(path)
            self.assertTrue(result["success"])
            self.assertFalse(result["appears_non_empty"])

    def test_finds_visual_paths_in_report_payload(self):
        paths = find_visual_artifact_paths({"response": {"data": {"file_path": "D:/tmp/a.png"}}})
        self.assertEqual([path.as_posix() for path in paths], ["D:/tmp/a.png"])

    def test_detects_black_bmp(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "black.bmp"
            width, height = 1, 1
            pixel_data = bytes([0, 0, 0, 0])
            header_size = 54
            file_size = header_size + len(pixel_data)
            header = bytearray(b"BM")
            header.extend(file_size.to_bytes(4, "little"))
            header.extend((0).to_bytes(4, "little"))
            header.extend(header_size.to_bytes(4, "little"))
            header.extend((40).to_bytes(4, "little"))
            header.extend(width.to_bytes(4, "little", signed=True))
            header.extend(height.to_bytes(4, "little", signed=True))
            header.extend((1).to_bytes(2, "little"))
            header.extend((24).to_bytes(2, "little"))
            header.extend((0).to_bytes(4, "little"))
            header.extend(len(pixel_data).to_bytes(4, "little"))
            header.extend((0).to_bytes(16, "little"))
            path.write_bytes(bytes(header) + pixel_data)
            result = analyze_bmp(path)
            self.assertTrue(result["success"])
            self.assertFalse(result["appears_non_empty"])

    def test_decodes_indexed_png_filters_across_rows(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "indexed.png"
            _write_indexed_png_with_up_filter(path)
            result = analyze_png(path)
            self.assertTrue(result["success"])
            self.assertEqual(result["non_black_pixel_count"], 3)

    def test_reads_jpeg_dimensions_without_pixel_stats(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "shot.jpg"
            payload = (
                b"\xff\xd8"
                b"\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00"
                b"\xff\xc0\x00\x11\x08\x00\x02\x00\x03\x03\x01\x11\x00\x02\x11\x00\x03\x11\x00"
                b"\xff\xd9"
            )
            path.write_bytes(payload)
            result = analyze_jpeg_dimensions(path)
            self.assertTrue(result["success"])
            self.assertEqual(result["width"], 3)
            self.assertEqual(result["height"], 2)
            self.assertFalse(result["pixel_statistics_available"])


if __name__ == "__main__":
    unittest.main()
