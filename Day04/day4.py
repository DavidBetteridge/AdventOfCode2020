import re
from functools import partial

HCL_PATTERN = re.compile('^#[a-f0-9]{6}$')
PID_PATTERN = re.compile('^[0-9]{9}$')
ECL_PATTERN = re.compile('^amb|blu|brn|gry|grn|hzl|oth$')
FIELD_TYPES = frozenset([ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" ])

def is_in_range(lower, upper, valueToCheck):
    return lower <= int(valueToCheck) <= upper

def matches_pattern(pattern, valueToCheck):
    return pattern.match(valueToCheck) != None

def hgt_is_valid(valueToCheck):
    if valueToCheck.endswith("cm"):
        return is_in_range(150, 193, valueToCheck[:-2])
    elif valueToCheck.endswith("in"):
        return is_in_range(59, 76, valueToCheck[:-2])
    else:
        return False

VALIDATIONS = {
    "byr" : partial(is_in_range, 1920, 2002),
    "iyr" : partial(is_in_range, 2010, 2020),
    "eyr" : partial(is_in_range, 2020, 2030),
    "hgt" : hgt_is_valid,
    "hcl" : partial(matches_pattern, HCL_PATTERN),
    "pid" : partial(matches_pattern, PID_PATTERN),
    "ecl" : partial(matches_pattern, ECL_PATTERN),
    "cid" : lambda _: True
}

def load_documents() :
    documents = open('Day04/day4.txt').read().split('\n\n')
    return [document.replace('\n',' ') for document in documents]


def field_in_document(document, fieldType):
    return (fieldType + ':' in document)


def document_contains_all_fields(document):
    for fieldType in FIELD_TYPES:
        if not field_in_document(document, fieldType):
            return False
    return True

def documentIsValid(document):
    if document_contains_all_fields(document):
        fields = document.split(' ')
        for field in fields:
            parts = field.split(':')
            if (len(parts) == 2):
                fieldName = parts[0]
                fieldValue = parts[1]

                if (not VALIDATIONS[fieldName](fieldValue) ):
                    return False
        return True
    else:
        return False

def part_one():
    documents = load_documents()
    validDocuments = 0
    for document in documents:
        if (document_contains_all_fields(document)):
            validDocuments = validDocuments + 1
    return validDocuments

def part_two():
    documents = load_documents()
    validDocuments = 0
    for document in documents:
        if (documentIsValid(document)):
            validDocuments = validDocuments + 1
    return validDocuments