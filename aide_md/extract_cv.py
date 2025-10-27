import pdfplumber

pdf_path = r"c:\Users\mayeu\Desktop\Git\projet-cv\cv-old\CV Eric MAYEUX 2025 DirQ.pdf"

with pdfplumber.open(pdf_path) as pdf:
    full_text = ""
    for page_num, page in enumerate(pdf.pages, 1):
        print(f"\n{'='*60}")
        print(f"PAGE {page_num}")
        print(f"{'='*60}\n")
        text = page.extract_text()
        print(text)
        full_text += text + "\n\n"

# Save to file for reference
with open("cv_extracted.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("\n\nText saved to cv_extracted.txt")
