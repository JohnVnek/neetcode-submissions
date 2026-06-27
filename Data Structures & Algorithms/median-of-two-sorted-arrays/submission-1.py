class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        n, m = len(nums1), len(nums2)
        merge = []

        while i < n and j < m:
            if nums1[i] < nums2[j]:
                merge.append(nums1[i])
                i += 1
            else:
                merge.append(nums2[j])
                j += 1

        while i < n:
            merge.append(nums1[i])
            i += 1   
        while j < m:
            merge.append(nums2[j])
            j += 1
        
        middle = (len(merge)) / 2
        print(middle)
        if (len(merge) % 2) == 0:
            print("enter")
            print((merge[math.floor(middle-1)] + merge[math.floor(middle)])/2)
            return (merge[math.floor(middle-1)] + merge[math.floor(middle)])/2
        else:
            return merge[math.floor(middle)]
