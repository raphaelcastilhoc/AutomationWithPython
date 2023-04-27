import pyperclip
import Helpers.TextExtractor as TextExtractor

text = str(pyperclip.paste())

contacts = TextExtractor.extractContacts(text)

if len(contacts) > 0:
    pyperclip.copy('\n'.join(contacts))
    print('Copied to clipboard:')
    print('\n'.join(contacts))
else:
    print('No phone numbers or email addresses found.')