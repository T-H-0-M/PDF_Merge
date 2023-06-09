"""
Author: Thomas Bandy
Project: PDF Merger

This script merges multiple PDF files into a single PDF file using the PyPDF2 library.
"""


import os
from os.path import dirname, abspath, join
from typing import Final
from PyPDF2 import PdfMerger


ROOT: Final[str] = dirname(abspath(__file__))
"""
The root directory of the project.
"""

INPUT_DIR: Final[str] = join(ROOT, "input")
"""
The directory where the files to be joined are stored.
"""


def merge_pdf_files():
    """
    Merge the PDF files in the INPUT_DIR directory and save the result as 'result.pdf'.
    """
    pdf_files = [
        filename for filename in os.listdir(INPUT_DIR) if filename.endswith(".pdf")
    ]
    merger = PdfMerger()

    for pdf_file in pdf_files:
        pdf_path = os.path.join(INPUT_DIR, pdf_file)
        merger.append(open(pdf_path, "rb"))

    with open("result.pdf", "wb") as output_file:
        merger.write(output_file)

    print("Complete")


if __name__ == "__main__":
    merge_pdf_files()
