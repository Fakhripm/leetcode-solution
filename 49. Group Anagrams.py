"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""

class Solution:
    # O(m*n) time O(m*n) space for output
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}
        for s in strs:
            AnagramSig = [0 for i in range(26)]
            for c in s:
                AnagramSig[ord(c)-ord('a')] += 1
            key = tuple(AnagramSig)
            if key not in res:
                res[key] = []
            res[key].append(s)
        return list(res.values())
    
# Create an instance of the class
solution = Solution()

result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)

"""
Array HashTable String Sorting
1. Recognizing anagram is basically array with alphabet frequency (Anagram Signature)
2. Group anagram using it signature
3. ps: python list must us immutable so convert ->  tuple(sig)
"""
