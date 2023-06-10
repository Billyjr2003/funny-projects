import string
def find_missing_letter(given_letters):
    letters = string.ascii_lowercase
    letters_list = [i for i in letters]
    start = letters_list.index(given_letters[0])
    end = letters_list.index(given_letters[-1])
    for letter in letters_list[start:end+1]:
        if letter in given_letters :
            print('no missing letter')
        else :
            print(letter)
            

find_missing_letter('abcdeghjkmnp')

    
