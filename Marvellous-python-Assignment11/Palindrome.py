def ReverseNumber(n):
    rev = 0
    n = abs(n)
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev

def CheckPalindrome(n):
    return n == ReverseNumber(n)

n = int(input("Enter a number: "))
if CheckPalindrome(n):
    print("Palindrome")
else:
    print("Not a Palindrome")