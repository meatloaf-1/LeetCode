class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        results = set()
        results.add(word)  
        i = 0
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            length = j - i
            if length > 1:
                for new_len in range(1, length):
                    new_word = word[:i] + word[i] * new_len + word[j:]
                    results.add(new_word)
            i = j   
        return len(results)