import csv
from os import path
import Helpers.TextExtractor as TextExtractor

filePath = input('Type the file path: ')

if not path.isfile(filePath):
    print('%s is not a valid file path.' % filePath)
    quit()

delimiter = input('Type the delimiter: ')

hasHeaderInput = input('Does the file have a header? (y/n)')
hasHeader = True if hasHeaderInput == 'y' else False

csvFile = open(filePath)
csvReader = csv.reader(csvFile, delimiter = delimiter)

contacts = []
for row in csvReader:
    if hasHeader and csvReader.line_num == 1:
        continue

    for column in row:
        csvContacts = TextExtractor.extractContacts(column)
        contacts += csvContacts

fileName, fileExtension = path.splitext(filePath)
newCsvFileName = '%s_only_contacts.csv' % fileName

outputFile = open(newCsvFileName, 'w', newline='')
outputWriter = csv.writer(outputFile, delimiter = ';')

outputWriter.writerow(contacts)

print('Contacts extracted to %s' % newCsvFileName)
        