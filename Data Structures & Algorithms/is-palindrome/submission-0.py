class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""
        for char in s :
            if char.isalnum():
                palindrome += char
            else :
                continue
        palindrome = palindrome.lower()
        # if s not in range(a,z or A,Z or 0,9):
        #     return False
        # also convert to lowercase
        return (palindrome == palindrome[::-1])