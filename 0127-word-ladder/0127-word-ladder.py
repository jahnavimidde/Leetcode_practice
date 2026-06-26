class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        wordSet = set(wordList)
        def fun(word,d):
            
            d[word]=[]
            for i in range(len(word)):
                
                for ch in "abcdefghijklmnopqrstuvwxyz":

                    newWord = word[:i] + ch + word[i+1:]

                    if newWord != word and newWord in wordSet:
                        d[word].append(newWord)
        d={} 
        fun(beginWord, d)           
        for word in wordList:
            fun(word,d)
        queue=deque()
        vis={word:False for word in wordList}
        if beginWord in vis:
            vis[beginWord]=True
        if beginWord not in d:
            return 0
        for val in d[beginWord]:
            vis[val]=True
            queue.append((val,2))
        
        while queue:
            word,num=queue.popleft()
            
            if word==endWord:
                return num
            for nei in d[word]:
                if not vis[nei]:
                    vis[nei]=True
                    queue.append((nei,num+1))
        return 0
        
                    
        

        
            

