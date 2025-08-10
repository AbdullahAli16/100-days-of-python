# Day: 76(Ex: 08 "Merge the PDF")

import pypdf

# Reading:

reader=pypdf.PdfReader("new/Ai.pdf")

print(reader)

print(len(reader.pages))                # Total no of pages in the pdf

first_page=reader.pages[0]
print(first_page.extract_text())        # Text present on the first line of the pdf


# Merging:
writer=pypdf.PdfWriter()
list_of_pdfs=["new/Ai.pdf","new/Seylani.pdf"]

for pdf in list_of_pdfs:
    writer.append(pdf)

with open ("new/merged-pdf.pdf","wb") as merged_file:
    writer.write(merged_file) 

writer.close()