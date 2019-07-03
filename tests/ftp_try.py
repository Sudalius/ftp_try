from ftplib import FTP
from tests import cvs_reader

# Upload file to FTP
ftp = FTP("ftp.dlptest.com")
print(ftp.login("dlpuser@dlptest.com", "fLDScD4Ynth0p4OJ6bW6qCxjh"))
data = ftp.retrlines('LIST')
print(data)
path = "../tests/files_store/upload_test.txt"

with open(path) as fobj:
    ftp.storlines('STOR ' + path, fobj)


# Download file from FTP
ftp = FTP("speedtest.tele2.net")
ftp.login()
data = ftp.retrlines('LIST')
print(data)
savedFileName = "../tests/files_store/saved.zip"
fileNameForDownload = "2MB.zip"
with open(savedFileName, 'wb') as f:
    ftp.retrbinary('RETR ' + fileNameForDownload, f.write)
    print("File has been downloaded")
ftp.close()


#Reads CSV file and return 1st string
cvs_reader.string_from_csv("../tests/files_store/addresses.csv")

