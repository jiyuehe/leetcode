import os
os.system('cls')

class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l1 = len(word1)
        l2 = len(word2)
        
        merged = ""
        if l1 >= l2:
            for i in range(l2):
                merged = merged + word1[i]
                merged = merged + word2[i]

            merged = merged + word1[i+1:]
        elif l1 < l2:
            for i in range(l1):
                merged = merged + word1[i]
                merged = merged + word2[i]
        
            merged = merged + word2[i+1:]

        return merged

sol = Solution()

merged = sol.mergeAlternately('abc','pqr')
print(merged) # apbqcr

merged = sol.mergeAlternately('ab','pqrs')
print(merged) # apbqrs

merged = sol.mergeAlternately('abcd','pq')
print(merged) # apbqcd
