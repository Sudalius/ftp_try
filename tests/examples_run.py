from tests.readers import cvs_reader, xlsx_reader
from tests.variables import variables
from ftplib import FTP

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


#Readers functions calls
cvs_reader.string_from_csv(variables.addresses, line_number=2)
cvs_reader.dictionary_from_csv(variables.addresses, keys_column=1, values_column=2)
xlsx_reader.line_from_xls(variables.capitals, row=2)
xlsx_reader.dictionary_from_xls(variables.capitals, rows_quantity=5, keys_column=0, values_column=1)


