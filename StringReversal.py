
def stringRev(txt):
    return txt[::-1]

def sentenceRev(txt):
    words = txt.split()
    wordsRev = words[::-1]
    sRev = ' '.join(wordsRev)
    return sRev

print("Hello! Welcome to Sam's Python String Reversal.\n")
#print()

while True:
    print("What would you like to do?\n")
    choice = input("String Reverse(s) or Sentence Reverse?(se): ")

    if choice.lower() == 's':
        rev = stringRev(input("Please enter the string you wish reversed: "))
        print(rev)

    elif choice.lower() == 'se':
        newSentence = sentenceRev(input("Please enter the sentence you wish reversed: "))
        print(newSentence)
    
    else:
        print("Sorry! Please enter one of the two choices.")

    if input('Do you wish to continue?:').lower().startswith('y'):
        continue