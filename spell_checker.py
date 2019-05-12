letter = "abcdefghijklmnopqrstuvwxyz"


def readDictionary():
    try:
        fileIn = open('text.txt')
        dictionary = []
        for i, line in enumerate(fileIn):
            line = line.replace("\n", "")
            dictionary.append(line)
        fileIn.close()
        return set(dictionary)
    except FileNotFoundError:
        dataList = {}
        return dataList


def letterRemoving(string):
    wordList = []
    for i in range(len(string)):
        newWord = string[:i] + string[i+1:]
        wordList.append(newWord)
    return wordList


def letterSwapping(string):
    wordList = []
    for i in range(len(string)-1):
        newString = string[:i] + string[i+1] + string[i] + string[i+2:]
        wordList.append(newString)
    return wordList


def letterReplace(string):
    wordList = []
    global letter
    for i in range(len(string)):
        for j in range (len(letter)):
            newWord = string[:i] + letter[j] + string[i + 1:]
            wordList.append(newWord)
    return wordList


def letterInsert(string):
    wordList = []
    global letter
    for i in range(len(string)+1):
        for j in range(len(letter)):
            newWord = string[:i] + letter[j] + string[i:]
            wordList.append(newWord)
    return wordList


def getOneEditWords(string):
    removeLetter = letterRemoving(string)
    swapLetter = letterSwapping(string)
    replace = letterReplace(string)
    insert = letterInsert(string)

    combined = removeLetter + swapLetter + replace + insert
    return set(combined)


def getTwoEditWords(oneEditWords):
    newList = []
    for i in oneEditWords:
        removeLetter = letterRemoving(i)
        swapLetter = letterSwapping(i)
        replace = letterReplace(i)
        insert = letterInsert(i)
        combined = removeLetter + swapLetter + replace + insert
        newList += combined
    return set(newList)


def getPossibleWords(string, dictionary):
    oneEditWords = list(getOneEditWords(string))
    twoEditWords = getTwoEditWords(oneEditWords)
    possibleOne = set(oneEditWords).intersection(dictionary)
    possibleTwo = twoEditWords.intersection(dictionary)
    return sorted(possibleOne), sorted(possibleTwo)


def main():
    dictionary = readDictionary()
    if len(dictionary) == 0:
        print("Dictionary not available! Exiting program.")
        return
    print("Supply words to test the spell checker.\nPress <enter> " + \
          "when you are done.")
    string = "Spelling"
    while len(string) > 0:
        string = input("A word to check: ")
        if len(string) > 0 and not string.isalpha():
            print("Use only letters in your word.")
        elif len(string) > 0:
            oneEditInDictionary, twoEditInDictionary = getPossibleWords(string, dictionary)
            if string in oneEditInDictionary:
                print("Word is spelled correctly! Similar words obtained:")
            print("Higher probability:")
            if len(oneEditInDictionary) > 0:
                print(list(oneEditInDictionary))
            else:
                print("No words found.")
            print("Lower probability:")
            if len(twoEditInDictionary) > 0:
                print(twoEditInDictionary)
            else:
                print("No words found.")
    print("All done!")


main()
