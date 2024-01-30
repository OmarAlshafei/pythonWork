class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newWord = []
        maxLen = max(len(word1),len(word2))

        for i in range(maxLen):
            if i < len(word1):
                newWord.append(word1[i])

            if i < len(word2):
                newWord.append(word2[i])

        return ''.join(newWord)
    