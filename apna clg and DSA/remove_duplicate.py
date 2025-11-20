class Solution(object):
    def removeDuplicates(self, nums):
        ls = []
        ls_ = []
        count = 0
        for item in nums:
            if item not in ls:
                ls.append(item)
            else:
                ls_.append('_')
        ls.extend(ls_)
        print(ls)
        """
        :type nums: List[int]
        :rtype: int
        """
    
nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
sol.removeDuplicates(nums)