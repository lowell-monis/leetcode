class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        count = 0
        for word in words:
            if len(word) >= len(pref):
                for i in range(len(pref)):
                    if pref[i] != word[i]:
                        break
                else:
                    count += 1
        return count