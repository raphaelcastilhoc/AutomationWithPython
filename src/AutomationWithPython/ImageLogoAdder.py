import os
import uuid
from PIL import Image

directoryPath = input('Type the directory path: ')

if not os.path.isdir(directoryPath):
    print('%s is not a valid directory path.' % directoryPath)
    quit()

logoFilePath = input('Type the logo file path: ')

if not os.path.isfile(logoFilePath):
    print('%s is not a valid file path.' % logoFilePath)
    quit()

outputFolderPath = os.path.join(directoryPath, '_images_with_logo_%s' % uuid.uuid4())
os.mkdir(outputFolderPath)

logoWidth, logoHeight = (150, 150)
logoImage = Image.open(logoFilePath).resize((logoWidth, logoHeight))

for fileName in os.listdir(directoryPath):
    filePath = os.path.join(directoryPath, fileName)
    if os.path.isfile(filePath):
        imageFile = Image.open(filePath)
        width, height = imageFile.size

        imageFile.paste(logoImage, (width - logoWidth, height - logoHeight), logoImage)
        imageFile.save(os.path.join(outputFolderPath, fileName))

print('Images with logo saved on %s' % outputFolderPath)
