class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = re.sub('[^a-zA-Z0-9]','',s).lower() # sub(pattern, replace with, string) here ^ means NOT, basically not an alphanumeric character
        # return (s == s[::-1])

        # BRUTE FORCE SOLUTION:
        # palindrome = ""
        # for char in s :
        #     if char.isalnum():
        #         palindrome += char
        #     else :
        #         continue
        # palindrome = palindrome.lower()
        # # if s not in range(a-z or A-Z or 0-9):
        # #     return False
        # # also convert to lowercase
        # return (palindrome == palindrome[::-1])

        l,r = 0,len(s)-1
        while l<r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
        return True