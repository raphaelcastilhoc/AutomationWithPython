from os import path
import TextExtractor

filePath = input('Type the file path: ')

if not path.isfile(filePath):
    print('%s is not a valid file path.' % filePath)
    quit()

fileToExtract = open(filePath)
contentFile = fileToExtract.read()
contacts = TextExtractor.extractContacts(contentFile)
fileToExtract.close()

fileName, fileExtension = path.splitext(filePath)
editedFile = open('%s_edited%s' % (fileName, fileExtension), 'w')
editedFile.write('\n'.join(contacts))
editedFile.close()

print('Contacts extracted to %s' % editedFile.name)