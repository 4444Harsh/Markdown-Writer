def h1(text):
    return f"# {text}\n\n"

def h2(text):
    return f"## {text}\n\n"

def h3(text):
    return f"### {text}\n\n"

def h4(text):
    return f"#### {text}\n\n"

def h5(text):
    return f"##### {text}\n\n"

def h6(text):
    return f"###### {text}\n\n"

def bold(text):
    return f"**{text}**"

def italic(text):
    return f"*{text}*"

def strikethrough(text):
    return f"~~{text}~~"

def code(text):
    return f"`{text}`"

def blockquote(text):
    return f"> {text}\n\n"

def unordered_list(items):
    return "\n".join(f"- {item}" for item in items) + "\n\n"

def ordered_list(items):
    return "\n".join(f"{i+1}. {item}" for i, item in enumerate(items)) + "\n\n"

def table(headers, rows):
    header_row = " | ".join(headers)
    separator = " | ".join(["---"] * len(headers))
    content = "\n".join(" | ".join(row) for row in rows)
    return f"{header_row}\n{separator}\n{content}\n\n"

def link(text, url):
    return f"[{text}]({url})"

def image(alt_text, url):
    return f"![{alt_text}]({url})"

def horizontal_rule():
    return "---\n\n"

def write_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)