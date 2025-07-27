def extract_headings(doc):
    outline = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                text = " ".join([span["text"] for span in line["spans"] if span["text"].strip()])
                if not text:
                    continue

                font_sizes = [span["size"] for span in line["spans"]]
                max_font_size = max(font_sizes)

                # Heuristic: determine heading level by font size
                if max_font_size >= 16:
                    level = "H1"
                elif max_font_size >= 14:
                    level = "H2"
                elif max_font_size >= 12:
                    level = "H3"
                else:
                    continue

                outline.append({
                    "level": level,
                    "text": text.strip(),
                    "page": page_num
                })

    return outline
