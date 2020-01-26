# 1. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

sample = "The Quick Brow Fox"

def solution(sample):

    #join the string by spaces into a list
    joined_string = list(sample.replace(" ",""))

    #loop through to count for upper
    all_caps = len([letters for letters in joined_string if letters.isupper() == True])
    all_lows = len(joined_string) - all_caps

    print(f'No. of Upper case characters : {all_caps}')
    print(f'No. of Lower case characters : {all_lows}')

solution(sample)