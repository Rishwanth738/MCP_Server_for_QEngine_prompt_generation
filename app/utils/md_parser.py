import os
import re

def parse_all_markdowns():
    docs = []
    base_path = "data/"

    for fname in os.listdir(base_path):
        if fname.endswith(".md"):
            file_path = os.path.join(base_path, fname)
            with open(file_path, encoding="utf-8") as f:
                content = f.read()

                if "functions" in fname.lower():
                    chunks = re.split(r"####\s+\*\*Function:", content)
                    for chunk in chunks:
                        lines = chunk.strip().splitlines()
                        if not lines:
                            continue

                        title = lines[0].strip(" *") if lines else "Untitled"
                        body = "\n".join(lines[1:])
                        block = f"Function: {title}\n{body}"

                        docs.append({
                            "text": block,
                            "meta": {"source": fname, "type": "function", "title": title}
                        })

                elif "elements" in fname.lower():
                    chunks = re.split(r"###\s+Module:", content)
                    for chunk in chunks:
                        if not chunk.strip():
                            continue
                        lines = chunk.strip().splitlines()
                        title = lines[0].strip() if lines else "Unknown Module"
                        block = "\n".join(lines)
                        docs.append({
                            "text": f"UI Module: {title}\n{block}",
                            "meta": {"source": fname, "type": "ui-element", "module": title}
                        })

                elif "variables" in fname.lower():
                    chunks = re.split(r"####\s+\*\*Variable:", content)
                    for chunk in chunks:
                        if not chunk.strip():
                            continue
                        lines = chunk.strip().splitlines()
                        title = lines[0].strip() if lines else "Untitled"
                        block = "\n".join(lines[1:])
                        docs.append({
                            "text": f"Variable: {title}\n{block}",
                            "meta": {"source": fname, "type": "variable", "name": title}
                        })

    return docs
