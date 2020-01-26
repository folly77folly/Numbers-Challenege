# 2. Write a Python function to find the Max of three numbers

def solution(first_number, second_number, third_number):
    #assume the first digit is the highest and compare it with others
    highest_numb = first_number

    if highest_numb > second_number:

        highest_numb = highest_numb

    elif second_number > highest_numb:

        highest_numb = second_number

    elif highest_numb > third_number:

        highest_numb = highest_numb

    else:
        highest_numb = third_number

    return highest_numb

print(solution(889, 130, 80))