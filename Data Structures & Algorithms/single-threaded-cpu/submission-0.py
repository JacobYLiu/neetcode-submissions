class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''
        restate
        given # amount of tasks in array named tasks (len(tasks)) 
        where each element is a subarray containing [enqueueTime, processingTime]
        avaliable at this time and will take this much time

        the single thread cpu will process at most one task at a time:
        - if no avaliable task >> cpu idle
        - if there are avaliable task, cpu will choose the one with shortest
        processing time
            - if there equal shortest proc time then take smallest index
        - cpu will process the entire task without stopping
        - cpu can start a new task instantly

        Constraint: 
        - there are equal processing times, but are there equal enqueue times?
        - is the array sorted by enqueue time from the beginning?
            - if not, then we sort by enqueue time 
        - are there empty inputs?
        - are there enqueueTime with 0 processing time?
        - are there negative numbers?
        - There can be equal processing time for all tasks
            - [[1,3][2,3][3,3]...]
        - all tasks can be avaliable at same time

        Examples: 
        - [[1,3],[2,3][3,2]]
        outputs: [2,0,1]

        Approach: greedy approach with minheap approach 
        - prioritizing the smaller processing time.
        time complexity: O(n)
        space: O(n)
        '''
        # if not tasks: 
        #     return []

        for i, t in enumerate(tasks): 
            # iterating thru 
            t.append(i)
        tasks.sort(key = lambda x: x[0])

        res, minHeap = [], []
        i, time = 0, tasks[0][0]

        # As we going thru the tasks array and making sure we still
        # have tasks in the minHeap. 
        while minHeap or i < len(tasks):
            # We need to push all into the minHeap  
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1

            if not minHeap: 
                time = tasks[i][0]
            else: 
                pt, index = heapq.heappop(minHeap)
                time += pt
                res.append(index)
        return res



