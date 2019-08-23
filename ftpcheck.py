from ftplib import FTP


def ftptest(server, filename):

    print("going to connect " + server)
    print("filename to upload " + filename)
    ftp = FTP(server)   # connect to host, default port

    ftp.login()               # user anonymous, passwd anonymous@

    ftp.retrlines('LIST')     # list directory contents

    # files = ftp.dir()
    # print (files)
    ftp.cwd("upload") #changing to upload
    fp = open(filename, 'rb')
    ftp.storbinary('STOR %s' % filename, fp, 1024)
    # ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
    # ftp.retrlines('LIST')  # list inside upload
    # ftp.delete("payload.zip")

    ftp.retrlines('LIST')  # list inside upload post delete
    ftp.close()



ftptest('speedtest.tele2.net', 'ftpcheck.py')
