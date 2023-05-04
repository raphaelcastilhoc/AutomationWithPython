import os
import uuid
from PIL import Image

directoryPath = input('Type the directory path: ')

if not os.path.isdir(directoryPath):
    print('%s is not a valid directory path.' % directoryPath)
    quit()

newWidth = int(input('Type the new width: '))
newHeight = int(input('Type the new height: '))

outputFolderPath = os.path.join(directoryPath, '_resized_images_%s' % uuid.uuid4())
os.mkdir(outputFolderPath)

for fileName in os.listdir(directoryPath):
    filePath = os.path.join(directoryPath, fileName)
    if os.path.isfile(filePath):
        imageFile = Image.open(filePath)
        resizedImage = imageFile.resize((newWidth, newHeight))
        resizedImage.save(os.path.join(outputFolderPath, fileName))

print('Resized images saved on %s' % outputFolderPath)