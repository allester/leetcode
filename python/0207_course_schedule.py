'''
https://leetcode.com/problems/course-schedule/submissions/1668776464/
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        courseToRemaining = [0] * numCourses
        
        for a, b in prerequisites:
            courses[a].append(b)
            courseToRemaining[b] += 1

        s = [course for course in range(numCourses) if courseToRemaining[course] == 0]
        
        while s:
            course = s.pop()
            for postRequisite in courses[course]:
                courseToRemaining[postRequisite] -= 1
                if courseToRemaining[postRequisite] == 0:
                    s.append(postRequisite)
        
        return sum(courseToRemaining) == 0