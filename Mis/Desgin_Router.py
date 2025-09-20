from collections import deque, defaultdict
import bisect

class Router:
    def __init__(self, memoryLimit):
        self.memoryLimit = memoryLimit
        self.queue = deque()
        self.packet_set = set()
        self.dest_map = defaultdict(list)
        
    def addPacket(self, destination, timestamp, source):
        key = (source, destination, timestamp)
        if key in self.packet_set:
            return False
        
        if len(self.queue) == self.memoryLimit:
            old_src, old_dist, old_ts = self.queue.popleft()
            self.packet_set.remove((old_src, old_dist, old_ts))
            idx = bisect.bisect_left(self.dest_map[old_dist], old_ts)
            if idx < len(self.dest_map[old_dist]) and self.dest_map[old_dist][idx] == old_ts:
                self.dest_map[old_dist].pop(idx)

        self.queue.append(key)
        self.packet_set.add(key)
        self.dest_map[destination].append(timestamp)
        return True
    
    def forwardPacket(self):
        if not self.queue:
            return []
        src, dst, ts = self.queue.popleft()
        self.packet_set.remove((src, dst, ts))
        idx = bisect.bisect_left(self.dest_map[dst], ts)
        if idx<len(self.dest_map[dst]) and self.dest_map[dst][idx] == ts:
            self.dest_map[dst].pop(idx)
        return [src, dst, ts]
    
    def getCount(self, destination, startTime, endTime):
        if destination not in self.dest_map:
            return 0
        timestamps = self.dest_map[destination]
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_left(timestamps, endTime)
        return right-left
    
R = Router(3)
print(R.addPacket(1,4,90) )
print(R.addPacket(2,5,90) )
print(R.addPacket(1,4,90)  )
print(R.addPacket(3,5,95) )
print(R.addPacket(4,5,105))
print(R.forwardPacket() )
print(R.addPacket(5,2,110) )
print(R.getCount(5,100,110) )
