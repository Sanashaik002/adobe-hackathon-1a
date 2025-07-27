import os
import json
import fitz  
from utils import extract_headings

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"

def process_pdf(file_path):
    doc = fitz.open(file_path)
    title = os.path.basename(file_path).replace(".pdf", "")
    outline = extract_headings(doc)

    return {
        "title": title,
        "outline": outline
    }

def main():
    pdf_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf")]

    for pdf_file in pdf_files:
        input_path = os.path.join(INPUT_DIR, pdf_file)
        output_path = os.path.join(OUTPUT_DIR, pdf_file.replace(".pdf", ".json"))

        try:
            result = process_pdf(input_path)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)
            print(f"Processed: {pdf_file}")
        except Exception as e:
            print(f"Error processing {pdf_file}: {e}")

if __name__ == "__main__":
    main()
