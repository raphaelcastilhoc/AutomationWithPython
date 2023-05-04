import os
import uuid
from PIL import Image

directoryPath = input('Type the directory path: ')

if not os.path.isdir(directoryPath):
    print('%s is not a valid directory path.' % directoryPath)
    quit()

outputFolderPath = os.path.join(directoryPath, '_rotated_images_%s' % uuid.uuid4())
os.mkdir(outputFolderPath)

for fileName in os.listdir(directoryPath):
    filePath = os.path.join(directoryPath, fileName)
    if os.path.isfile(filePath):
        imageFile = Image.open(filePath)
        rotatedImage = imageFile.rotate(180)
        rotatedImage.save(os.path.join(outputFolderPath, fileName))

print('Rotated images saved on %s' % outputFolderPath)