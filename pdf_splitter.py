import os
import glob
from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_splitter(path, new_file_number):
    fname = os.path.splitext(os.path.basename(path))[0]
    pdf = PdfFileReader(path)
    total_num_pages = pdf.getNumPages()
    # print("Total number of pages is ", total_num_pages)
    split_amount = total_num_pages // new_file_number
    # print("Split amount is ", split_amount)
    start_page = 0
    current_part = 0
    while start_page < total_num_pages:
        if start_page < total_num_pages - split_amount:
            # print(start_page, split_amount)
            pdf_writer = PdfFileWriter()
            for page in range(start_page, start_page + split_amount):
                pdf_writer.addPage(pdf.getPage(page))
            # print("Num pages is: ",pdf_writer.getNumPages())
            output_filename = '{}_part_{}.pdf'.format(fname, current_part)   
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
        else:
            pdf_writer = PdfFileWriter()
            for page in range(start_page, total_num_pages):
                pdf_writer.addPage(pdf.getPage(page))
            output_filename = '{}_part_{}.pdf'.format(fname, current_part)   
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
        current_part +=1
        start_page = start_page + split_amount
        print('Created: {}'.format(output_filename))
    return
        



def main():
    # Getting the current working directory
    curr_working_dir = os.getcwd()

    # Iterate over all pdf files in directory and split if needed
    for pdf_file in glob.glob(curr_working_dir + "/*.pdf"):
        # Split file if size > 100 MB
        new_file_number =  (os.path.getsize(pdf_file) // 100000000  + 1)
        if new_file_number > 1:
            pdf_splitter(pdf_file, new_file_number)
            
if __name__ == "__main__":
    main()
        
    