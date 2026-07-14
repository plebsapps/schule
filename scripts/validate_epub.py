#!/usr/bin/env python3
"""Prüft die XML-basierten Dokumente eines EPUB-Archivs."""

import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

XML_SUFFIXES = (".xhtml", ".opf", ".ncx", ".xml")


def validate_epub(epub_path: Path) -> None:
    with zipfile.ZipFile(epub_path) as archive:
        documents = [name for name in archive.namelist() if name.lower().endswith(XML_SUFFIXES)]
        if not documents:
            raise ValueError("Das EPUB enthält keine XML- oder XHTML-Dokumente.")

        errors = []
        for document in documents:
            try:
                ET.fromstring(archive.read(document))
            except ET.ParseError as error:
                errors.append(f"{document}: {error}")

    if errors:
        raise ValueError("Ungültiges EPUB-XHTML:\n" + "\n".join(errors))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"Verwendung: {Path(sys.argv[0]).name} DATEI.epub")

    path = Path(sys.argv[1])
    validate_epub(path)
    print(f"EPUB-XHTML gültig: {path}")
