#!/usr/bin/env python3
"""Erzeugt die einseitige Veröffentlichungsinformation ohne externe Abhängigkeiten."""

import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "buch" / "veroeffentlichungstext.md"
OUTPUT = ROOT / "static" / "downloads" / "veroeffentlichungstext.pdf"


def pdf_text(value: str) -> bytes:
    return (value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")).encode("cp1252")


def text_command(font: str, size: int, x: int, y: int, value: str) -> bytes:
    return f"BT /{font} {size} Tf {x} {y} Td (".encode() + pdf_text(value) + b") Tj ET\n"


def build_pdf() -> bytes:
    source = SOURCE.read_text(encoding="utf-8")
    title = re.search(r"^# (.+)$", source, re.MULTILINE).group(1)
    subtitle = re.search(r"^## (.+)$", source, re.MULTILINE).group(1)
    author = re.search(r"^\*\*Autor:\*\* (.+)$", source, re.MULTILINE).group(1)
    description = source.split("## Buchbeschreibung", maxsplit=1)[1]
    paragraphs = [" ".join(part.split()) for part in description.strip().split("\n\n")]

    stream = bytearray()
    stream.extend(b"0.73 0.05 0.10 rg 0 770 595 72 re f\n")
    stream.extend(text_command("F2", 27, 52, 720, title))
    for index, line in enumerate(textwrap.wrap(subtitle, width=54)):
        stream.extend(text_command("F1", 15, 52, 684 - index * 20, line))
    stream.extend(text_command("F2", 12, 52, 625, f"Autor: {author}"))
    stream.extend(b"0.73 0.05 0.10 RG 52 606 m 543 606 l S\n")
    stream.extend(text_command("F2", 17, 52, 572, "Buchbeschreibung"))

    y = 544
    for paragraph in paragraphs:
        for line in textwrap.wrap(paragraph, width=79, break_long_words=False):
            stream.extend(text_command("F1", 10, 52, y, line))
            y -= 15
        y -= 9

    stream.extend(b"0.30 0.30 0.30 rg\n")
    stream.extend(text_command("F1", 9, 52, 48, "Freies Projekt unter der GNU GPLv3"))

    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] "
        b"/Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> /Contents 4 0 R >>",
        b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n" + stream + b"endstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>",
    ]

    pdf = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for number, obj in enumerate(objects, start=1):
        offsets.append(len(pdf))
        pdf.extend(f"{number} 0 obj\n".encode() + obj + b"\nendobj\n")
    xref = len(pdf)
    pdf.extend(f"xref\n0 {len(objects) + 1}\n".encode())
    pdf.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        pdf.extend(f"{offset:010d} 00000 n \n".encode())
    pdf.extend(f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode())
    return bytes(pdf)


if __name__ == "__main__":
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(build_pdf())
    print(f"PDF erstellt: {OUTPUT}")
