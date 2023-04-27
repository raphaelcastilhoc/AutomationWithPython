import os
from pathlib import Path
import zipfile
import uuid

directoryPath = input('Type the directory path: ')

if not os.path.isdir(directoryPath):
    print('%s is not a valid directory path.' % directoryPath)
    quit()

files = [fileName for fileName in os.listdir(directoryPath) if os.path.isfile(os.path.join(directoryPath, fileName))]

zipFilePath = Path(directoryPath, 'new_zip%s.zip' % uuid.uuid4())
zipArchiver = zipfile.ZipFile(zipFilePath, 'a')
for fileName in files:
    fileNameWithoutExtension, fileExtension = os.path.splitext(fileName)
    originalFile = Path(directoryPath, fileName)
    renamedFileName = '%s_compressed%s' % (fileNameWithoutExtension, fileExtension)
    renamedFile = Path(directoryPath, renamedFileName)
    originalFile.rename(renamedFile)

    zipArchiver.write(renamedFile, renamedFileName, compress_type=zipfile.ZIP_DEFLATED)

zipArchiver.close()

print('Files compressed in %s' % zipFilePath)
