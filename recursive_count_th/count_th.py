'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # Variables
    first_letter = list(word)

    # Checks
    if len(first_letter) == 0:
        return 0
    if len(first_letter) == 1:
        return 0
        
    # DO NOT USE .lower
    if first_letter[0] == 't' and first_letter[1] == 'h':
        return 1 + count_th(first_letter[1:])
    else:
        return 0 + count_th(first_letter[1:])
