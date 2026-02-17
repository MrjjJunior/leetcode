
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.replace(",", "").replace(":", "").replace(" ", "").lower()
    return s[::1] == s[::-1]

if __name__ == "__main__":
    print(isPalindrome( "A man, a plan, a canal: Panama"))
