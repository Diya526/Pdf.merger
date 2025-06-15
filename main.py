from PyPDF2 import PdfMerger

def main():
    merger = PdfMerger()
    try:
        n = int(input("How many PDFs do you want to merge? "))
        pdfs = []
        for i in range(n):
            name = input(f"Enter the path of PDF {i+1}: ").strip()
            pdfs.append(name)

        for pdf in pdfs:
            try:
                merger.append(pdf)
            except Exception as e:
                print(f"Error appending {pdf}: {e}")

        output_name = input("Enter the output file name (e.g., merged.pdf): ").strip()
        if not output_name.lower().endswith('.pdf'):
            output_name += '.pdf'
        merger.write(output_name)
        print(f"Merged PDF saved as {output_name}")
    finally:
        merger.close()

if __name__ == "__main__":
    main()