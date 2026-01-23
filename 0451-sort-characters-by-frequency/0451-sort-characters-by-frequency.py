class Solution(object):
    def frequencySort(self, s):
        freq = {}

        # step 1: count characters
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # step 2: sort characters by frequency (descending)
        chars = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

        # step 3: build result
        result = ""
        for ch in chars:
            result += ch * freq[ch]

        return result
