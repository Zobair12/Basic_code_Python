from barcode import EAN13
from barcode.writer import ImageWriter
from IPython.display import Image, display

#Create PNG Barcode

clcoding = EAN13("5901234123457", writer=ImageWriter())
png_file = clcoding.save("ean13_clcoding")

#Create SVG Barcode
clcoding_svg = EAN13("5901234123457")
svg_file = clcoding_svg.save("ean13_clcoding_svg")

display(Image(png_file))