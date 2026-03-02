class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Count frequency of each character
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        stack = []
        seen = set()   # To track already included characters
        
        for ch in s:
            freq[ch] -= 1   # Decrease frequency
            
            # If already in stack → skip
            if ch in seen:
                continue
            
            # Maintain increasing lexicographical order
            while stack and stack[-1] > ch and freq[stack[-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)
            
            stack.append(ch)
            seen.add(ch)
        
        return "".join(stack)