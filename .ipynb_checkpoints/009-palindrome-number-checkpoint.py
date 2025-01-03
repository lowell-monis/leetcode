class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x<10:
            return True
        else:
            temp = x
            rev = 0
            while temp != 0:
                rev = rev*10 + temp%10
                temp //=10
            
            return rev==x