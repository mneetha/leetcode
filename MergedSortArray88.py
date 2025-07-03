from typing import List


class Solution:

    def binary_insert(self, arr, x):
        left=0
        right = len(arr) -1
        while left <= right:
            mid = (left + right)//2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid -1
        print(f"Stopped at {mid} value is {arr[mid]}")
        return mid


    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        test_m = m - n
        print(nums2)

        for num2 in nums2:
            test_nums1 = nums1[:test_m]
            print(test_nums1)

            # find index where num2 in the correct spot in nums1

            if test_nums1:
                insert_after = self.binary_insert(test_nums1, num2)
                i = insert_after+1
                j=test_m
                while j >i:
                    nums1[j+1] = nums1[j]
                    j=j-1
                nums1[i] = num2
                test_m = test_m +1
            else:
                nums1 = nums2
                break
        print(f"final nums1 {nums1}")



# test1 = Solution()
# test1.merge([1,2,3,0,0,0], 6, [3,5,6], 3)
# test2 = Solution()
# test2.merge([1], 1, [], 0)
test3 = Solution()
test3.merge([0], 0, [1], 1)
