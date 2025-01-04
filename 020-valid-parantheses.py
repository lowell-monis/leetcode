class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        li = []
        for b in s:
        
            if b in '({[':
                li.append(b)
                
            elif b in ')}]':
            
                if not li:
                    return False
                
                top = li.pop()
                if (top == '(' and b != ')') or (top == '{' and b != '}') or (top == '[' and b != ']'):
                    return False
                
        return len(li) == 0