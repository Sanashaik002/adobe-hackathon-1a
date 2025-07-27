# 🧠 Adobe Hackathon Round 1A – PDF Outline Extractor

## 🚀 Challenge Objective
Extract a structured outline from raw PDFs, including the **document title**, and **headings** (H1, H2, H3) along with their **page numbers**, and output in a specified JSON format.

This forms the foundation for smart document understanding in the Adobe “Connecting the Dots” challenge.

---

## 🛠️ Tech Stack

- Python 3.10
- PyMuPDF (fitz)
- pdfminer.six
- Docker(for containerization)

---

## 📂 Project Structure

pdf-outline-extractor/

  ├── Dockerfile

  ├── main.py

  ├── utils.py

  ├── requirements.txt

  ├── README.md

  ├── input/ # Place PDF files here (ignored in Git)

  ├── output/ # JSON files will be saved here (ignored in Git)

## 🐳 How to Build and Run

```bash
docker build --platform linux/amd64 -t pdfoutline:round1a .

docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdfoutline:round1a


