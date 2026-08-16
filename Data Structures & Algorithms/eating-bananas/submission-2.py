class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        The problem is asking me to return the optimal speed to eat all bananas in
        the array. The speed value is k 
        There are n amount of piles in the input and each index has b amount of 
        bananas
        The guard will come back in h hours

        Constraints and edge cases
        - Is it possible to have 0 bananas in a pile?
        - can hours be 0? prob not
        - Can hours be less than len(piles)? no

        Approach: 
        Because we are trying to return the minimum integer so koko can eat all 
        bananas, the approach would be
        Greedy and sorting with binary search 
        time complexity would O(nlogn) 
        
        '''

        if len(piles) == h: 
            return max(piles)
        

        left, right = 1, max(piles)
        out = right 
        while left <= right: 
            total = 0
            k = (left + right) // 2
            for p in piles:
                total += math.ceil(float(p)/k) 
            if total <= h: 
                out = k
                right = k - 1
            else:
                left = k + 1
            
        return out 