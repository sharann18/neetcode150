#TC: O(logn)
#SC: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        start = 0
        end = len(nums1)

        while start <= end:
            partitionA = (start + end) // 2

            partitionB = ((len(nums1) + len(nums2) + 1) // 2) - partitionA

            maxLeftA = float(-inf) if partitionA == 0 else nums1[partitionA - 1] 
            maxLeftB = float(-inf) if partitionB == 0 else nums2[partitionB - 1] 

            minRightA = float(inf) if partitionA == len(nums1) else nums1[partitionA]
            minRightB = float(inf) if partitionB == len(nums2) else nums2[partitionB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    return max(maxLeftA, maxLeftB)
            
            if maxLeftA > minRightB:
                end = partitionA - 1
            else:
                start = partitionA + 1
        
        return None