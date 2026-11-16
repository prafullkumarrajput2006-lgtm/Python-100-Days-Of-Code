# Exercise 8... Solution... Operations on PDF 





from pypdf import PdfWriter, PdfReader
import os


# 1. Merge Multiple PDF Files
def merge_pdfs():

    writer = PdfWriter()

    files = input("Enter PDF filenames separated by comma: ").split(",")

    for file in files:
        file = file.strip()

        if os.path.exists(file):
            writer.append(file)
            print(f"{file} added successfully!")
        else:
            print(f"{file} not found!")

    output = input("Enter output PDF name: ")

    if not output.lower().endswith(".pdf"):
        output += ".pdf"

    with open(output, "wb") as f:
        writer.write(f)

    writer.close()

    print("PDF files merged successfully!")


# 2. Split PDF into Individual Pages
def split_pdf():

    filename = input("Enter PDF filename: ")

    if not os.path.exists(filename):
        print("File not found!")
        return

    reader = PdfReader(filename)

    for i, page in enumerate(reader.pages):

        writer = PdfWriter()
        writer.add_page(page)

        output = f"page_{i + 1}.pdf"

        with open(output, "wb") as f:
            writer.write(f)

        writer.close()

    print("PDF split successfully!")


# 3. Extract Selected Pages
def extract_pages():

    filename = input("Enter PDF filename: ")

    if not os.path.exists(filename):
        print("File not found!")
        return

    reader = PdfReader(filename)
    writer = PdfWriter()

    print(f"Total pages: {len(reader.pages)}")

    pages = input("Enter page numbers separated by comma: ").split(",")

    try:
        for page in pages:

            page_num = int(page.strip())

            if 1 <= page_num <= len(reader.pages):
                writer.add_page(reader.pages[page_num - 1])
            else:
                print(f"Invalid page number: {page_num}")

        output = input("Enter output PDF name: ")

        if not output.lower().endswith(".pdf"):
            output += ".pdf"

        with open(output, "wb") as f:
            writer.write(f)

        writer.close()

        print("Selected pages extracted successfully!")

    except ValueError:
        print("Please enter valid page numbers!")


# 4. Extract Text from PDF
def extract_text():

    filename = input("Enter PDF filename: ")

    if not os.path.exists(filename):
        print("File not found!")
        return

    reader = PdfReader(filename)

    for i, page in enumerate(reader.pages):

        print(f"\n----- Page {i + 1} -----")

        text = page.extract_text()

        print(text if text else "No extractable text found.")

    
# 5. Count PDF Pages
def count_pages():

    filename = input("Enter PDF filename: ")

    if not os.path.exists(filename):
        print("File not found!")
        return

    reader = PdfReader(filename)

    print("Total Pages:", len(reader.pages))


# 6. Display PDF Metadata
def pdf_metadata():

    filename = input("Enter PDF filename: ")

    if not os.path.exists(filename):
        print("File not found!")
        return

    reader = PdfReader(filename)

    metadata = reader.metadata

    print("\nPDF Metadata:")

    if metadata:
        print("Title:", metadata.title)
        print("Author:", metadata.author)
        print("Subject:", metadata.subject)
        print("Creator:", metadata.creator)
        print("Producer:", metadata.producer)
    else:
        print("No metadata available.")


# Main Menu
while True:

    print("\n========== PDF MANIPULATION TOOL ==========")

    print("1. Merge PDF Files")
    print("2. Split PDF")
    print("3. Extract Selected Pages")
    print("4. Extract Text from PDF")
    print("5. Count PDF Pages")
    print("6. View PDF Metadata")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        merge_pdfs()

    elif choice == "2":
        split_pdf()

    elif choice == "3":
        extract_pages()

    elif choice == "4":
        extract_text()

    elif choice == "5":
        count_pages()

    elif choice == "6":
        pdf_metadata()

    elif choice == "7":
        print("Thank you for using PDF Manipulation Tool!")
        break

    else:
        print("Invalid choice! Please try again.")
