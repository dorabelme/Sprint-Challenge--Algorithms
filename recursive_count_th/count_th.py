'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    th_length = 2  # "th"
    if len(word) < th_length:
        return 0

    if (word[0: th_length] == "th"):
        return 1 + count_th(word[th_length - 1:])
    else:
        return count_th(word[th_length - 1:])


print(count_th("abcthxyz"))
