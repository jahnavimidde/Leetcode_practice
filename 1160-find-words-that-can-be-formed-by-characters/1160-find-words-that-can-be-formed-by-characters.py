class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        sum_=0
        for i in words:
            if not Counter(i)-Counter(chars):
                sum_+=len(i)
        return sum_