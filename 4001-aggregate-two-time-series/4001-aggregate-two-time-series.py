class Solution(object):
    def aggregateTimeSeries(self, series1, series2):
        """
        :type series1: List[List[int]]
        :type series2: List[List[int]]
        :rtype: List[List[int]]
        """
        s1=sorted(series1,key=lambda x:x[0])
        s2=sorted(series2,key=lambda x:x[0])
        a=b=0
        aggr=[]
        while a<len(s1) and b<len(s2):
            if s1[a][0]<s2[b][0]:
                aggr.append([s1[a][0],s1[a][1]+s2[b][1]])
                a+=1
            elif a<len(s1) and b<len(s2) and s1[a][0]>s2[b][0]:
                aggr.append([s2[b][0],s1[a][1]+s2[b][1]])
                b+=1
            if a<len(s1) and b<len(s2) and s1[a][0]==s2[b][0]: 
                aggr.append([s2[b][0],s1[a][1]+s2[b][1]])
                a+=1
                b+=1
        if a<len(s1):
            while a<len(s1):
                aggr.append([s1[a][0],s1[a][1]])
                a+=1
        if b<len(s2):
            while b<len(s2):
                aggr.append([s2[b][0],s2[b][1]])
                b+=1
        return aggr








