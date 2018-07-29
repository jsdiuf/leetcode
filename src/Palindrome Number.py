
#https://leetcode.com/problems/palindrome-number/description/
class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        result=0
        t=x
        while t!=0:
            result=result*10+t%10
            t//=10
        return result==x

    #only search harf of the list
    def isPalindrome2(self, x):
        if x<0:
            return False
        if x>=0 and x<10:
            return True
        if x%10==0:
            return False
        rev=0
        while x>rev:
            rev=rev*10+x%10
            x//=10
        return rev==x or rev//10==x


t = Solution()
#print(123%10)
print(t.isPalindrome2(17890))