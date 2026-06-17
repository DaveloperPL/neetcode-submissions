class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        map = {}
        mapTwo = {}
        for x in range(len(alphabet)):
            map[alphabet[x]] = 0
            mapTwo[alphabet[x]] = 0
        for x in range(len(s)):
            map[s[x:x+1]] += 1
        for x in range(len(t)):
            mapTwo[t[x:x+1]] += 1

        for x in range(len(alphabet)):
            if (map[alphabet[x]] != mapTwo[alphabet[x]]):
                return False
 
        return True