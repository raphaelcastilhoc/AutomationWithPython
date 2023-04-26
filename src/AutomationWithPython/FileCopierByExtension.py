import os
import shutil
import re
from pathlib import Path
import uuid

directoryPath = input('Type the directory path: ')
filesExtension = input('Type the files extension: ')

if not os.path.isdir(directoryPath):
    print('%s is not a valid directory path.' % directoryPath)
    quit()

if not ('.' in filesExtension):
    filesExtension = '.%s' % filesExtension

outputFolderPath = Path(directoryPath, 'copiedFiles_%s' % uuid.uuid4())
os.mkdir(outputFolderPath)

extensionRegex = re.compile('^.+\%s' % filesExtension)
for folderName, subfolders, fileNames in os.walk(directoryPath):
    if folderName == str(outputFolderPath):
        continue

    fileNamesWithChosenExtension = [fileName for fileName in fileNames if(extensionRegex.search(fileName))]

    for fileNameWithChosenExtension in fileNamesWithChosenExtension:
        shutil.copy(Path(folderName, fileNameWithChosenExtension), Path(outputFolderPath, fileNameWithChosenExtension))

print('Files copied to %s' % outputFolderPath)
