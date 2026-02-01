class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        total_pts=sum(cardPoints)
        #we need to take exactly k cards from beginning or end but concecutively eg:  [1,2,-,-,-,10,9]can be taken ...1&2 from begi (consecutive) 10&9 from end (consecutive)
        #maintain window with n-k size substract from total_pts
        if k==len(cardPoints):
            return sum(cardPoints)
        else:
            w_size=len(cardPoints)-k
        r=l=0
        sum_=0
        max_sum=0
        while r<len(cardPoints):
            sum_=sum_+cardPoints[r]
            if r-l+1==w_size:
                max_sum=max(max_sum,total_pts-sum_)
                sum_=sum_-cardPoints[l]
                l+=1
            r+=1
        return max_sum

        