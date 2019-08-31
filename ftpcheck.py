from ftplib import FTP


def ftptest(server, filename):

    print("going to connect " + server)
    print("filename to upload " + filename)
    ftp = FTP(server)   # connect to host, default port

    ftp.login('jatul','password@123')               # user anonymous, passwd anonymous@

    ftp.retrlines('LIST')     # list directory contents

    # # files = ftp.dir()
    # # print (files , "- this is coming as null")
    # ftp.cwd("upload") #changing to upload
    # fp = open(filename, 'rb')
    # ftp.storbinary('STOR %s' % filename, fp, 1024)
    # # # ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
    # # # ftp.retrlines('LIST')  # list inside upload
    # # # ftp.delete("payload.zip")
    #
    # ftp.retrlines('LIST')  # list inside upload post delete
    # ftp.close()

    # localfile = open(filename, 'wb')
    # ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

    # ftp.quit()
    # localfile.close()

    def placeFile():
        filename = 'exampleFile.txt'
        ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
        ftp.quit()

    placeFile()

ftptest('localhost', 'test.txt')
