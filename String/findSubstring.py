from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)

        if s_len < total_len:
            return []

        word_count = Counter(words)
        result = []

        # Try every possible starting offset within one word-length,
        # since matches are aligned to multiples of word_len from some start.
        for offset in range(word_len):
            left = offset
            count = 0                 # how many words currently "matched" in window
            window = Counter()

            for right in range(offset, s_len - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in word_count:
                    window[word] += 1
                    count += 1

                    # too many copies of `word` -> shrink from the left
                    while window[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == num_words:
                        result.append(left)
                        # slide window forward by one word to look for the next match
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    # word not in words at all -> window can't include this position,
                    # reset entirely and start fresh right after it
                    window.clear()
                    count = 0
                    left = right + word_len

        return result

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]

obj = Solution()
res = obj.findSubstring(s, words)
print(res)