import os
import zipfile
from ftplib import FTP



# Upload file to FTP
ftp = FTP("ftp.dlptest.com")
print(ftp.login("dlpuser@dlptest.com", "fLDScD4Ynth0p4OJ6bW6qCxjh"))
data = ftp.retrlines('LIST')
print(data)
path = "C:\\ftp_test\\upload_test.txt"

with open(path) as fobj:
    ftp.storlines('STOR ' + path, fobj)


# Download file from FTP
ftp = FTP("speedtest.tele2.net")
# print(ftp.login())
ftp.login()
data = ftp.retrlines('LIST')
#print(data)
savedFileName = "C:\\ftp_test\\saved.zip"
fileNameForDownload = "2MB.zip"
with open(savedFileName, 'wb') as f:
    ftp.retrbinary('RETR ' + fileNameForDownload, f.write)
    print("File has been downloaded")
ftp.close()

# dirName = "/upload/"
# ftp.cwd(dirName)
# file_example = "1MB.zip"
# myFile = open(file_example)
# print("Success...")
# myFile.close()


# ftp = FTP("speedtest.tele2.net")
# ftp.login("anonymous", "test")
# dirName = "/upload/"
# ftp.cwd(dirName)
# files = ftp.nlst()
#
# for fileName in files:
#     if os.path.isfile(fileName):
#         print('Downloading...')
#         ftp.retrbinary("RETR %s" %fileName, open(fileName, "wb").write)



# file_example = "1MB.zip"
# localFile = open(file_example, 'wb')
# newFileBytes = [123, 3, 255, 0, 100]
# ftp.retrbinary('RETR' + file_example, localFile.write(bytearray(b'{\x03\xff\x00d')))
#
# savedir = "C:/ftp_test"
# os.chdir(savedir)
#
# ftp.quit()
# localFile.close()
