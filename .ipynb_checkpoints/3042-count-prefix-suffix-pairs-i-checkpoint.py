class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def isPrefixAndSuffix(str1, str2):
            if len(str1)<=len(str2):
                for i in range(len(str1)):
                    if str1[i]!=str2[i]:
                        return False
                for i in range(1, len(str1)+1):
                    if str1[-i]!=str2[-i]:
                        return False
                return True
            else:
                return False
        count = 0
        for i in range(len(words)):
            for j in range(len(words)):
                if i<j:
                    if isPrefixAndSuffix(words[i], words[j]):
                        count += 1
        return count