import re

def inDocument(document, fieldName):
    return (fieldName in document)

#250
def documentContainsAllFields(document):
     return inDocument(document, "byr:") and inDocument(document, "iyr:") and inDocument(document, "eyr:") and inDocument(document, "hgt:") and inDocument(document, "hcl:") and inDocument(document, "ecl:") and inDocument(document, "pid:")

def ValidateBYR(valueToCheck):
    return len(valueToCheck) == 4 and int(valueToCheck) >= 1920 and int(valueToCheck) <= 2002

def ValidateIYR(valueToCheck):
    return len(valueToCheck) == 4 and int(valueToCheck) >= 2010 and int(valueToCheck) <= 2020

def ValidateEYR(valueToCheck):
    return len(valueToCheck) == 4 and int(valueToCheck) >= 2020 and int(valueToCheck) <= 2030

def ValidateHGT(valueToCheck):
    if valueToCheck.endswith("cm"):
        numeric = int(valueToCheck[:-2])
        return numeric >= 150 and numeric <= 193
    elif valueToCheck.endswith("in"):
        numeric = int(valueToCheck[:-2])
        return numeric >= 59 and numeric <= 76
    else:
        return False

hclPattern = re.compile('^#[a-f0-9]{6}$')
def ValidateHCL(valueToCheck):
    return hclPattern.match(valueToCheck) != None

def ValidateECL(valueToCheck):
    return valueToCheck == "amb" or valueToCheck == "blu" or valueToCheck == "brn" or valueToCheck == "gry" or valueToCheck == "grn" or valueToCheck == "hzl" or valueToCheck == "oth"

pidPattern = re.compile('^[0-9]{9}$')
def ValidatePID(valueToCheck):
    return pidPattern.match(valueToCheck) != None

def documentIsValid(document):

    if documentContainsAllFields(document):

        fields = document.split(' ')
        for field in fields:
            parts = field.split(':')
            if (len(parts) == 2):
                fieldName = parts[0]
                fieldValue = parts[1]

                if (fieldName == "byr") and not ValidateBYR(fieldValue):
                    return False

                if (fieldName == "iyr") and not ValidateIYR(fieldValue):
                    return False

                if (fieldName == "eyr") and not ValidateEYR(fieldValue):
                    return False             

                if (fieldName == "hgt") and not ValidateHGT(fieldValue):
                    return False      

                if (fieldName == "hcl") and not ValidateHCL(fieldValue):
                    return False      

                if (fieldName == "ecl") and not ValidateECL(fieldValue):
                    return False   

                if (fieldName == "pid") and not ValidatePID(fieldValue):
                    return False  

        return True
    else:
        return False


    fields = document.split(' ')
    print()

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