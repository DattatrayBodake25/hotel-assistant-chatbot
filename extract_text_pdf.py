import fitz  # type: ignore # PyMuPDF

def extract_text_from_pdf(pdf_file_path):
    """Extracts text from a PDF file."""
    try:
        doc = fitz.open(pdf_file_path)
        pdf_text = ""
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            pdf_text += page.get_text("text")
        doc.close()
        return pdf_text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""

# Specify PDF path
pdf_path = "Vivanta-New-Delhi-Dwarka-Hotel.pdf"

# Extract text
print(f"Extracting text from: {pdf_path}")
extracted_text = extract_text_from_pdf(pdf_path)

# Write text to file
if extracted_text.strip():
    output_file = "pdf_text.txt"
    print(f"Writing extracted text to: {output_file}")
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(extracted_text)
    print("Text extraction completed successfully.")
else:
    print("No text was extracted from the PDF.")