class Solution(object):
    def isIsomorpic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letters = {}
        for index,letter in enumerate(s):
            if letter in letters.keys():
                if letters[letter] != t[index]:
                    return False
            else:
                for val in letters.values():
                    if t[index] == val:
                        return False
                letters[letter] = t[index]
        return True

sol = Solution()
print(sol.isIsomorpic("egg","add"))
print(sol.isIsomorpic("foo","bar"))
print(sol.isIsomorpic("badc","baba"))
