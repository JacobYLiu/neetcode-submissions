class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        given int array 
        return occurrence of numbers that match k
        '''
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        '''
        count = 
        { 1: 1, 
          2: 1, }
        '''
        res = []
        for value, occurrences in count.items(): 
            res.append([occurrences, value])
        res.sort()
        # occurrences will be sorted and extract value into another array

        arr = [] 
        for i in range(len(res)): 
            if len(arr) < k: 
                arr.append(res.pop()[1])
        return arr
