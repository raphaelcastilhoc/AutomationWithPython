import re

def extractContacts(text):
    matches = []

    if not text or not isinstance(text, str):
        return matches

    brazilianPhoneRegex = re.compile(r'''(
    (\d{2}|\(\d{2}\))? # area code
    (\s|-|\.)? # separator
    (\d{5}) # first 5 digits
    (\s|-|\.) # separator
    (\d{4}) # last 4 digits
    )''', re.VERBOSE)

    emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @ # @ symbol
    [a-zA-Z0-9.-]+ # domain name
    (\.[a-zA-Z]{2,4}) # dot-something
    )''', re.VERBOSE)

    for groups in brazilianPhoneRegex.findall(text):
        phoneNumber = ''.join([groups[1], groups[3], groups[5]])
        matches.append(phoneNumber)

    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    return matches
