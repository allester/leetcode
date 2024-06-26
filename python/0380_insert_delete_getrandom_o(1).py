'''
https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/1239197694/?envType=study-plan-v2&envId=top-interview-150
'''

import random

class RandomizedSet(object):

    def __init__(self):
        self.list = []
        self.dict = dict() 

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if (val in self.dict):
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        
        
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if (val not in self.dict):
            return False
        self.list[self.dict[val]] = self.list[-1]
        self.dict[self.list[-1]] = self.dict[val]
        self.list.pop()
        del self.dict[val]
        return True
       

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()