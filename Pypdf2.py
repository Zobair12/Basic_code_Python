

import PyPDF2

with open("MD ZOBAIR AHMED FULL UPDATE.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    page=reader.pages[0]
    text=page.extract_text()
    print("page 1 Content:\n",text)