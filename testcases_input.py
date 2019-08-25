import os
import sys
import xlrd
import xlwt
from datetime import datetime
import itertools
import argparse


def open_file(path):
    """
    Open and read an Excel file
    """  
    test_count = 0
    #read all the excel sheets in the given directory
    for root,dirs,files in os.walk(path):
        xlsfiles=[ _ for _ in files if _.endswith('.xlsx')]
        for xlsfile in xlsfiles:
            book = xlrd.open_workbook(os.path.join(root,xlsfile))
            print(xlsfile)
            # print number of sheets
            sheet_count = book.nsheets
            print(sheet_count)  
            # print sheet names
            print(book.sheet_names())
            list_sheet = book.sheet_names()
           
            # get the first worksheet
            for sheet in range (sheet_count):
                work_sheet = book.sheet_by_index(sheet)
                list_sheet[sheet] 
                #no of row 
                row_count=work_sheet.nrows
                print("No of Test cases in %s  is %s " %(list_sheet[sheet],row_count-1))         
                #print the test cases name
                for i in range (1,row_count):
                    cell=work_sheet.cell(i,0)
                    print(cell.value)
                    test_count +=1
    print("No of test cases included in all the Web services is ",test_count)   

def write_file(path):
    """
    Write the contents of different web services into single excel sheet
    """
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Test_cases')
    col_width = 256 * 35                        # 30 characters wide 
    try:
        for m in itertools.count():
            ws.col(m).width = col_width
    except ValueError:
        pass    
    headers = ('sl.no','Web_service','Method_names','Test_cases', 'Test_case Count')
    for n, header in enumerate(headers):
        ws.row(0).write(n, header)
    wb.save(args.outfile)

    k=1  
    j=i=1 
    sl_no = 0
    # for calculating the web services    
    for root,dirs,files in os.walk(path):
        xlsfiles=[ _ for _ in files if _.endswith('.xlsx')]
        for xlsfile in xlsfiles: 
            #for adding row spaces after every web service
            i+=1
            j+=1
            k+=1             
            book = xlrd.open_workbook(os.path.join(root,xlsfile))
            sl_no +=1
            ws.row(i).write(0, sl_no)
            ws.row(i).write(1, xlsfile)      
            list_sheet = book.sheet_names()
            sheet_count = book.nsheets      
            # for getting the method names
            for sheet in range (sheet_count):
                #for calculating the test cases 
                work_sheet = book.sheet_by_index(sheet)
                method = list_sheet[sheet]
                row_count = work_sheet.nrows                 
                ws.row(j).write(2, method)
                ws.row(k).write(4,row_count-1)          
                for row_no in range(1,row_count):
                    cell = work_sheet.cell(row_no, 0)
                    ws.row(k).write(3, cell.value)
                    i+=1
                    j+=1
                    k+=1
                # for adding space after every method
                i+=1
                j+=1
                k+=1                             
    wb.save(args.outfile)   

#--------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("infile")
    parser.add_argument("outfile")    
    args=parser.parse_args()
    open_file(args.infile)
    write_file(args.infile)