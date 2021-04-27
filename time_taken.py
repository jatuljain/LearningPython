import os
import sys
import glob
import linecache
import xlwt
import argparse
import itertools

def time_taken(path):
    """
    Calculates the time taken in each log file
    """

    # print ("directory path : " + path)
    test_list=["DataSource_Loop","DataSource","Property_Transfer","PropertyTransfer_1","StatusCheck-","status_check","DataGen","DataGen2","JDBC_Request","Status_Check","Groovy_Script","CheckStatus","StatucCheck"]
    time_taken=[]
    testcases=[]
    web_services=[]
    methods=[]
    flag = True


    for filename in glob.glob(os.path.join(path, '*.txt')):
        file = os.path.splitext(os.path.basename(filename))[0]
        # print ("filename : " + file)
        web_service = (file[file.find('BasicHttpBinding_')+len('BasicHttpBinding_'):file.rfind('_TestSuite')])
        print(web_service)
        method_name = (file[file.find('TestSuite-')+len('TestSuite-'):file.rfind('_TestCase')])
        print(method_name)
        test = (file[file.find('TestCase-')+len('TestCase-'):file.rfind('-OK')])
        print(test) 

        for test_name in test_list:
            if test_name.lower() in test.lower():
                print("Excluding the file since test is",test_name)
                print('\n')
                break
        else:
            try:
                fp = open(filename, mode='r')
                line = linecache.getline(filename,2)
                time=(line[line.find(':')+len(':'):line.rfind('\n')])
                if(time != ""):
                    seconds_time=round((int(time)/1000), 3)
                    print("Time Taken:",seconds_time)
                    print("\n")
                    time_taken.append(seconds_time) 
                    testcases.append(test)
                    web_services.append(web_service)
                    methods.append(method_name)
                else:
                    print('Log file is empty \n')
            except:
                print("Log file are not in UTF-8 format \n")
                pass
            
            fp.close()

    print(testcases)     
    print(time_taken) 
    write_file(web_services,methods,testcases,time_taken)
                          
def write_file(web_services,methods,testcases,time_taken):
    """
    Write the contents of different web services into single excel sheet
    """
    
    wb = xlwt.Workbook(args.infile)
    ws1 = wb.add_sheet('Time_Taken')
    ws2 = wb.add_sheet('Selected_methods')
    col_width = 256 * 35                        # 30 characters wide 
    try:
        for m in itertools.count():
            ws1.col(m).width = col_width
    except ValueError:
        pass  
    
    headers = ('sl.no','Web_services','Methods','Test_cases','Time_Taken')
    for n, header in enumerate(headers):
        ws1.row(0).write(n, header)
    wb.save(args.outfile)
    
    i=1  
       
    for j, testcase in enumerate(testcases):
        ws1.write(i, 3, testcase)
        ws1.write(i, 4, time_taken[j]) 
        i+=1
            
            
    flag = True
    value=1
    sl_no = 1 
    web = web_services[0]
    method1 = methods[0]
    
    for web_service in web_services:
        if(web == web_service):        
            if (flag==True):
                ws1.write(value, 1, web_service)
                ws1.write(value, 0, sl_no)
                sl_no +=1
                flag=False
            else:
                ws1.row(value).write(1,'')
        elif(web != web_service):
            ws1.row(value).write(1,web_service)
            ws1.write(value, 0, sl_no)
            sl_no +=1
            web = web_service  
        value+=1
        
        
    flag = True
    value=1
    sl_no = 1 
    for method in methods:
        if(method1 == method):        
            if (flag==True):
                ws1.write(value, 2, method)
                flag=False
            else:
                ws1.row(value).write(2,'')
        elif(method1 != method):
            ws1.row(value).write(2,method)
            method1 = method  
        value+=1        
           

    wb.save(args.outfile)   

#--------------------------------------------------------------------
if __name__ == "__main__":
    sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument("infile")
    parser.add_argument("outfile")

    args=parser.parse_args()
    time_taken(args.infile)