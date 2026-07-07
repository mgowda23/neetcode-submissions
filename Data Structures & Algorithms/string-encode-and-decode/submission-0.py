class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for s in strs:
            msg += str(len(s)) + "#" + s
            print(msg)
        return msg

    def decode(self, s: str) -> List[str]:
        msg = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != '#':
                j+= 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            msg.append(s[i:j])
            i = j
        return msg