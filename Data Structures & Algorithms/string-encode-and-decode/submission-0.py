class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # Find the delimiter '#' starting from index i
            j = i
            while s[j] != "#":
                j += 1

            # Extract length and the string segment
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            # Move pointer past the current word
            i = j + 1 + length

        return res
