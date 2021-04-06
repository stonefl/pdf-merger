""" A python scripts to merge pdf files.
python merge_pdf.py -i "folder-name-of-pdf-files-to-merge" -o "merged-pdf-file-name"
exmample: `python merge_pdf.py -i files-to-merge -o merged-file`
or `python merge_pdf.py` to use the default arguments

"""

import argparse
import os
import PyPDF2

def parse_arguments():
    """
    A function to parse arguments.
    """
    parser = argparse.ArgumentParser(add_help=True)

    parser.add_argument(
        '-i', '--input_folder',
        metavar='input_folder', default="files-to-merge",
        help="path of the pdf files to merge."
    )

    parser.add_argument(
        '-o', '--output_file',
        metavar='output_file', default="merged-pdf.pdf",
        help="name of merged pdf file."
    )

    return parser

def merge_pdfs():
    # Step 0: get arguments
    parser = parse_arguments()
    args = parser.parse_args()
    input_folder = args.input_folder
    output_file = args.output_file


    # Step 1: read all PDF files to merge
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(cur_dir, input_folder)
    ouput_dir = os.path.join(cur_dir, output_file)

    pdf2merge = []
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf2merge.append(filename)

    # Step 2: set up the pdf writer
    pdfMerger = PyPDF2.PdfFileWriter()

    # Step 3: read files to merge
    for filename in pdf2merge:
        # read the bianry
        pdfFileObj = open(os.path.join(input_dir, filename), 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        # read each page
        for pagenum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pagenum)
            pdfMerger.addPage(pageObj)

    # Step 4: save merged file to output file
    pdfOutput = open(ouput_dir, 'wb')
    pdfMerger.write(pdfOutput)
    pdfOutput.close()





if __name__ == "__main__":
    merge_pdfs()