class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        length = len(nums)
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        
        # 考虑一个从头一个从尾的情况
        lst = [min_index+1,max_index+1,length - min_index,length-max_index,max(min_index,max_index)]
        lst = sorted(lst)
        step = lst[0] + lst[1]
        
        # 考虑都从一边的情况
        lst_new = [step,max(min_index+1,max_index+1),max(length-min_index,length - max_index)]
        return min(lst_new)
