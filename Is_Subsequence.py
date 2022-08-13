class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        start = 0
        for letter in s:
            found = t.find(letter,start,len(t))
            print(str(found) + " " + str(start))
            if found >= start:
                start = found + 1
            else:
                return False
        return True
sol = Solution()
print(sol.isSubsequence("aaaaaa","bbaaaa"))