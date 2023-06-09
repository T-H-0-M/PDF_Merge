# Author: Thomas Bandy
# Project: PDF Merger
#

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

if __name__ == "__main__":
    x = [a for a in os.listdir(INPUT_DIR) if a.endswith(".pdf")]

    merger = PdfMerger()

    for pdf in x:
        merger.append(open(os.path.join(INPUT_DIR, pdf), "rb"))

    with open("result.pdf", "wb") as out:
        merger.write(out)

    print("Complete")
