class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k > len(bloomDay):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        
        while low<=high:
            cnt=0
            bouquets=0
            mid=(low+high)//2
            for i in range(len(bloomDay)):
                if bloomDay[i]<=mid:
                    cnt+=1
                else:
                    bouquets+=cnt//k
                    cnt=0
            bouquets+=cnt//k
            
            if bouquets<m:
                low=mid+1
            else:
                high=mid-1
        return low
        