# Writer Markdown

A simple Python library for generating Markdown files using Python functions.

## Features
- Easy-to-use functions for writing Markdown
- Supports headings, bold, italics, lists, tables, links, images, and more
- Generates clean Markdown syntax
- Includes a command-line tool for quick Markdown file creation

## Installation
Install the package using pip:
```sh
pip install writer_markdown
```

## Usage
### Import the library
```python
from writer_markdown import *
```

### Create a Markdown file
```python
content = ""
content += h1("Markdown Writer Library")
content += h2("Introduction")
content += bold("This library makes Markdown generation easy!") + "\n\n"
content += unordered_list(["Easy to use", "Supports multiple Markdown elements", "Generates clean Markdown"])
content += table(["Feature", "Supported"], [["Headings", "✅"], ["Lists", "✅"], ["Tables", "✅"]])
content += horizontal_rule()
content += link("GitHub Repository", "https://github.com/example")

write_to_file("example.md", content)
```


## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Author
Created by [Harsh](https://github.com/4444harsh)."
