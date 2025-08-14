from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        taken = 0
        while q:
            cur_course = q.popleft()
            taken += 1
            for c in graph[cur_course]:
                indegree[c] -= 1
                if indegree[c] == 0: # pre 都修過了
                    q.append(c)

        if taken == numCourses:
            return True
        return False



    def canFinish3(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        
        d = {}
        for pre in prerequisites:
            if pre[0] == pre[1]:
                return False
            
            print(d)
            if pre[0] not in d and pre[1] not in d:
                d[pre[0]] = [pre[1]]
            elif pre[0] in d and pre[1] not in d[pre[0]]:
                d[pre[0]].append(pre[1])
            elif pre[1] in d and pre[0] not in d[pre[1]]:
                continue
            else:
                return False
        return True

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        
        q = []
        for pre in prerequisites[::-1]:
            if pre[0] == pre[1]:
                return False
            
            print(q)
            if pre[0] not in q:
                if pre[1] not in q:
                    q.append(pre[1])
                    q.append(pre[0])
                else:
                    q.append(pre[0])
            else:
                if pre[1] not in q:
                    q.insert(q.index(pre[0]), pre[1])
                elif q.index(pre[1]) > q.index(pre[0]):
                    return False
        return True