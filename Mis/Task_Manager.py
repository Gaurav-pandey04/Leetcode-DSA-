import heapq

class TaskManager:
    def __init__(self, tasks):
        self.task_map = {}  # taskId -> (userId, priority)
        self.heap = []
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId, taskId, priority):
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId, newPriority):
        userId, _ = self.task_map[taskId]
        self.task_map[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId):
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self):
        while self.heap:
            negPriority, negTaskId, taskId = heapq.heappop(self.heap)
            if taskId in self.task_map and self.task_map[taskId][1] == -negPriority:
                userId, _ = self.task_map[taskId]
                del self.task_map[taskId]
                return userId
        return -1
    
taskManager = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
taskManager.add(4, 104, 5)
taskManager.edit(102, 8)
print(taskManager.execTop())
taskManager.rmv(101) 
taskManager.add(5, 105, 15)
print(taskManager.execTop())