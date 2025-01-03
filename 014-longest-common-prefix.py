class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()

        start = strs[0]
        end = strs[-1]
        length = min(len(start), len(end))

        i = 0
        while i < length and start[i] == end[i]:
            i += 1

        return start[:i]