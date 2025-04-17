# This program is converts a txt file to a docx file

import docx
import sys, os
import glob

# The main program

if __name__ == "__main__":
    files = glob.glob("txt/*.txt")

    for file in files:
        doc = docx.Document()
        with open(file, "r") as f:
            for line in f:
                doc.add_paragraph(line)
        doc.save("docx/" + os.path.basename(file).replace(".txt", ".docx"))

    print("Done")