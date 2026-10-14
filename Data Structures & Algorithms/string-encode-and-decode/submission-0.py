class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s      # e.g. "neet" becomes "4#neet"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0                                  # current position in the string
        while i < len(s):
            j = i
            while s[j] != "#":                 # find the # after the length
                j += 1
            length = int(s[i:j])               # number between i and # is the length
            word = s[j + 1 : j + 1 + length]   # grab exactly that many chars after #
            res.append(word)
            i = j + 1 + length                 # jump to the start of the next length
        return res