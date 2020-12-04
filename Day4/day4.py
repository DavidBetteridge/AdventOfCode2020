def inDocument(document, fieldName):
    return (fieldName in document)

def documentIsValid(document):
    return inDocument(document, "byr:") and inDocument(document, "iyr:") and inDocument(document, "eyr:") and inDocument(document, "hgt:") and inDocument(document, "hcl:") and inDocument(document, "ecl:") and inDocument(document, "pid:")

documents = []
currentDocument = ""
for line in open('Day4/day4.txt').read().splitlines():
    if (line == ""):
        documents.append(currentDocument)
        currentDocument = ""
    else:
        currentDocument = currentDocument + " " + line
documents.append(currentDocument)

validDocuments = 0
for document in documents:
    if (documentIsValid(document)):
        validDocuments = validDocuments + 1


print(validDocuments)

# for document in documents:
#     if missingFromDocument(document, "byr")