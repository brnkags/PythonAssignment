import string

s = input(" Enter a word ")

if str.isdigit(s):
    print("Invalid input")

else:
    def remove_punctuations(word):
        return "".join(i.lower() for i in word if i in string.ascii_letters)


    def reverse(s):
        return s[::-1]


    def isPalindrome(s):
        s = remove_punctuations(s)
        return s == reverse(s)


    ans = isPalindrome(s)

    if ans:
        print("Yes")
    else:
        print("No")
