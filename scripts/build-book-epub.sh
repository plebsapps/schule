#!/bin/sh
set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
output_dir="$repo_root/buch/build"
output_file="$output_dir/arbeiten-mit-codex-zwischenstand.epub"

mkdir -p "$output_dir"

docker run --rm \
  --volume "$repo_root:/data" \
  --user "$(id -u):$(id -g)" \
  pandoc/core:3.10.0.0 \
  --from=markdown+smart \
  --to=epub3 \
  --standalone \
  --toc \
  --toc-depth=2 \
  --epub-cover-image=static/images/book-covers/titelbild-gpt-5-6-sol.png \
  --metadata-file=buch/metadata.yaml \
  --css=buch/epub.css \
  --resource-path=.:buch \
  buch/01-projektstart-planung-repository.md \
  buch/02-django-grundgeruest.md \
  buch/03-ui-grundsystem-beispieldaten.md \
  buch/04-gpt-5-6-sol-codex-oberflaechen.md \
  buch/05-backup-und-wiederherstellung.md \
  buch/06-stammdaten-ohne-vorlagen.md \
  buch/07-demo-noten-und-zeugnis.md \
  buch/bildkonzept.md \
  buch/anhang-codex-kommandoreferenz.md \
  buch/projektchronik.md \
  --output=buch/build/arbeiten-mit-codex-zwischenstand.epub

printf 'EPUB erstellt: %s\n' "$output_file"
