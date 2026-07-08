class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append( (value,timestamp) )

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ''
        res = ''
        valueTimes = self.hashmap[key]
        l, r = 0, len(valueTimes) - 1
        
        while l <= r:
            m = (l + r) // 2
            if valueTimes[m][1] <= timestamp:
                res = valueTimes[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
