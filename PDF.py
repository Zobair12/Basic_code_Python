from pdf2docx import Converter

pdf = 'MD ZOBAIR AHMED FULL UPDATE.pdf'
docx = 'MD ZOBAIR AHMED FULL UPDATE.docx'
cv = Converter(pdf)
cv.convert(docx, start=0, end=None)
cv.close()