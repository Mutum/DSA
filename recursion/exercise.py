
def head_recursion(num):

    # base case
    if num == 0:
        return 
    # recursion call first
    head_recursion(num -1 )

    #compute after recursion
    print(num)

def  tail_recursion(num):
    if num ==0:  # base case
        return
    print(num) # compute before recursion 
    tail_recursion(num-1) # recursion call last

# Run above two and see the difference 

head_recursion(5) # output 1,2,3,4,5
tail_recursion(5) # putput 5,4,3,2,1
# 1. factorial 

def recursive_func(n):
    if n < 0 :
        return "Invalid inputs : need 0 or positive"
    if n == 0 or n ==1  :
        return 1
    else :
        return recursive_func(n-1) * n

# But know maximum recursion limit of python 


# 2. Find Uppercase Letter in String

str_1 = "lucidProGramming"

for i in str_1:
    if i.isupper():
        print(i)

def find_all_uppercase(input_str, indx=0, result=None):
    # Initialize result list on first call
    if result is None:
        result = []

    # Base case: if we've reached the end of the string
    if indx >= len(input_str):
        return result

    # If current character is uppercase, add it to result
    if input_str[indx].isupper():
        result.append(input_str[indx])

    # Always continue to next character (no early return)
    return find_all_uppercase(input_str, indx+1, result)

# Test with example
str_1 = "lucidProGramming"
uppercase_letters = find_all_uppercase(str_1)
print(uppercase_letters)  # Should print ['P', 'G']