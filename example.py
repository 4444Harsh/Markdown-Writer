from markdown_writer import *

content = ""
content += h1("Markdown Writer Library")
content += h2("Introduction")
content += bold("This library makes Markdown generation easy!") + "\n\n"
content += blockquote("Write Markdown files using simple Python functions.")
content += unordered_list(["Easy to use", "Supports multiple Markdown elements", "Generates clean Markdown"])
content += ordered_list(["Install the package", "Import the functions", "Generate Markdown"])
content += table(["Feature", "Supported"], [["Headings", "✅"], ["Lists", "✅"], ["Tables", "✅"]])
content += horizontal_rule()
content += link("GitHub Repository", "https://github.com/example")
content += image("Markdown Logo", "https://example.com/markdown.png")

write_to_file("example.md", content)
