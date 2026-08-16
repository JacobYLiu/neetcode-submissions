class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        The constraints already shown with both strings lowercased
         
        Do we have empty strings?
        We can check their length - if different then False
        
        We
        

        '''

        occurrence1 = defaultdict(int)
        occurrence2 = defaultdict(int)
        for i in s: 
            occurrence1[i] += 1
        for j in t:
            occurrence2[j] += 1
        
        return True if occurrence1 == occurrence2 else False
    