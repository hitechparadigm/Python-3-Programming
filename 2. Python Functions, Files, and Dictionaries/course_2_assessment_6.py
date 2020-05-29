# course_2_assessment_6
# 1. Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
def sublist(input_list):
    output_list = []
    index = 0
    while index < len(input_list):
        if input_list[index] != 5:
            output_list.append(input_list[index])
            index += 1
        else:
            break
    return output_list

# 2. Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.


def check_nums(input_list):
    out_list = []
    idx = 0
    while idx < len(input_list):
        if input_list[idx] != 7:
            out_list.append(input_list[idx])
            idx += 1
        else:
            break
    return out_list

# 3. Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).
def sublist(input_list):
    out_list = []
    idx = 0
    while idx < len(input_list):
        if input_list[idx] != "STOP":
            out_list.append(input_list[idx])
            idx += 1
        else:
            break
    return out_list

# 4. Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.
