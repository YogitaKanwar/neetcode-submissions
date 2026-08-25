class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count = {}
        if len(s) != len(t):
            return False

        for character in s:
            if character in count:
                count[character] += 1
            else:
                count[character] = 1

        for char_t in t:
            if char_t in count:
                count[char_t] -= 1
                if count[char_t] < 0:
                    return False
            else:
                return False

        return True