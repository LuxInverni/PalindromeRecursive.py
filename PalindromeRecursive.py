string = input("Please write a number or word:  ")

def isPal(word):
    if len(word) <= 1:
        return True
    return (word[0] == word[-1]) * isPal(word[1:-1])

print(isPal(string))

##Outputs "1" if it is a Palindrome, and "0" if not a palindrome
