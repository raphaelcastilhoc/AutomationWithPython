import fitz
from os import path
import Helpers.TextExtractor as TextExtractor

filePath = input('Type the file path: ')

if not path.isfile(filePath):
    print('%s is not a valid file path.' % filePath)
    quit()

pdfFile = fitz.open(filePath)

contacts = []
for page in pdfFile:
    pageText = page.get_text()
    pdfContacts = TextExtractor.extractContacts(pageText)
    for pdfContact in pdfContacts:
        contacts.append(pdfContact)

if not contacts:
    print('Contacts not found')
    quit()

newPdf = fitz.open()
newPdfPage = newPdf.new_page()

positionY = 0
lineCount = 0
for contact in contacts:
    if(lineCount == 40):
        newPdfPage = newPdf.new_page()
        positionY = 0
        lineCount = 0

    positionY += 20
    newPdfPage.insert_text((20, positionY), contact)
    lineCount += 1

fileName, fileExtension = path.splitext(filePath)
newPdfFileName = '%s_only_contacts.pdf' % fileName
newPdf.save(newPdfFileName)

print('Contacts extracted to %s' % newPdfFileName)