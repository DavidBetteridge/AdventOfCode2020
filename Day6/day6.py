def load_answers() :
    documents = []
    currentDocument = ""
    for line in open('Day6/day6.txt').read().splitlines():
        if (line == ""):
            documents.append(currentDocument)
            currentDocument = ""
        else:
            currentDocument = currentDocument + line
    documents.append(currentDocument)
    return documents

groups = load_answers()   

total = 0
for answers in groups:
    letters = list(answers)
    distinctLetters = set(letters)
    numberOfLetters = len(distinctLetters)
    total += numberOfLetters

print(total)