-- Wandelt rohe HTML-Zeilenumbrüche in native Pandoc-Zeilenumbrüche um.
-- Der EPUB-Writer erzeugt daraus das für XHTML erforderliche <br />.
function RawInline(element)
  if element.format == "html" and element.text:match("^<br%s*/?>$") then
    return pandoc.LineBreak()
  end
end
