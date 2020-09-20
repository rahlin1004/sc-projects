"""
File: anagram.py
Name: Sarah Lin
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global Variable
Ans = []  # the answer


def main():
    """
    this program that you input a word and find all vocabulary in it
    """
    global Ans
    the_list = read_dictionary([])  # read
    print('========================================================')
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit) ")
    enter = input('Find anagrams for: ')
    if not enter.isalpha():
        while not enter.isalpha():
            if enter != '-1':
                print('illegal format, enter again')
                enter = input('Find anagrams for: ')
            else:
                break
    enter = enter.lower()
    while enter != '-1':
        find_anagrams(enter, the_list)
        print(len(Ans), 'anagrams: ', Ans)
        print('========================================================')
        Ans = []
        enter = input('Find anagrams for: ')
        if not enter.isalpha():
            while not enter.isalpha():
                if enter != '-1':
                    print('illegal format, enter again')
                    enter = input('Find anagrams for: ')
                else:
                    break
        enter = enter.lower()
    print('========================================================')
    print('BYE BYE')


def read_dictionary(dic):
    """
    This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
    """
    with open(FILE, 'r') as f:
        for line in f:
            if not line == '':
                dic.append(line.strip())
    return dic


def find_anagrams(s, dic):
    """
    :param s: the input word
    :return: None
    """
    print('Searching...')
    find_anagrams_helper(s, s, '', dic)


def find_anagrams_helper(enter, s, current_w, dic):
    """
    :param enter: (str) input word
    :param s: (str) apart of input word
    :param current_w: (str) answer
    :param dic: (list) dictionary
    :return: None
    """
    if len(current_w) >= len(enter):  # if len of current_w >= the input word
        if current_w not in Ans and current_w in dic:  # if not repeat and is correct
            print('Found: ' + current_w)
            print('Searching...')
            Ans.append(current_w)
    else:
        for i in range(len(s)):
            if has_prefix(current_w + s[i], dic):
                find_anagrams_helper(enter, s[:i] + s[i+1:], current_w + s[i], dic)


def has_prefix(sub_s, dic):
    """
    :param sub_s: (str) apart of word
    :return: (bool) if correct: True
    """
    for word in dic:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
