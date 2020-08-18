largestPalindrome = 0  # intial value of largest palindrome considered 0


def IsPalidrome(num):
    possiblePal = str(num)
    return possiblePal == possiblePal[::-1]


for firstNum in range(100, 1000):
    for lastNum in range(100, 1000):
        product = firstNum * lastNum
        if IsPalidrome(product) and product > largestPalindrome:
            largestPalindrome = product

print(f"The largest palindrome made from the product of two 3-digit numbers is {largestPalindrome}")