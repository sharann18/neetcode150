class TimeMap:

    def __init__(self): #O(1)
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None: #O(1)
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str: #O(logn)
        ans = ""

        values = self.hashmap.get(key, [])

        #binary search
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if values[mid][1] <= timestamp:
                ans = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        
        return ans