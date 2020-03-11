from ftplib import FTP

ftp = FTP('domainname.com')#domain name or ip address
ftp.login(user='username', passwd='password')#credentials
ftp.cwd('/change_to_specific_location_in_server/')#usually login takes to root
#user specific dir; Change working directory from there


def getFile():
    fileName = 'exampleFileToDownload.txt'
    localFile = open(fileName, 'wb')
    ftp.retrbinary('RETR '+fileName, localFile.write, 1024)# retriving file,
    #with byte size 1024 **** basically execute 'RETR file_name' command
    ftp.quit()
    localFile.close()


def putFile():
    fileName = 'exampleFileToUpload.txt'
    ftp.storbinary('STOR '+fileName, open(fileName, 'rb')) # execute 'STOR filename' command
    ftp.quit()
