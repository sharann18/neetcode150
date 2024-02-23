#Using prefix & postfix arrays
#TC: O(n)
#SC: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        output = []

        for i in range(0, len(nums)):
            if i == 0:
                prefix.append(nums[i])
                continue
            prefix.append(nums[i]*prefix[i-1])
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                postfix.append(nums[i])
                continue
            postfix.insert(0, nums[i]*postfix[0])
        
        for i in range(0, len(nums)):
            if i == 0:
                output.append(postfix[i+1])
                continue
            
            if i == len(nums) - 1:
                output.append(prefix[i-1])
                continue

            output.append(prefix[i-1]*postfix[i+1])

        return output

#Using two passes to calculate prefix and postfix products
#TC: O(n)
#SC: O(1), ignoring the output array as mentioned in the question
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = 1
        postfix = 1

        for i in range(0, len(nums)):
            output.append(prefix)
            prefix = prefix*nums[i]

        for i in  range(len(nums)-1, -1, -1):
            output[i] = output[i]*postfix
            postfix = postfix*nums[i]

        return output