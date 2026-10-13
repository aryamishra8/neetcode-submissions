class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #different lengths can't be anagrams
            return False
        countS, countT = {}, {} #letter -> how many times it appears
        for i in range(len(s)): #walk both strings together
            countS[s[i]] = countS.get(s[i], 0) + 1 #count letter in s
            countT[t[i]] = countT.get(t[i], 0) +1 #count letter in t
        return countS == countT #came counts means anagram
        