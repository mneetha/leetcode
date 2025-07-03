def threeSum(nums):
    nums.sort()  # Sort the array
    triplets = []  # Initialize a list to store unique triplets

    for i in range(len(nums) - 2):
        # Skip the same element to avoid duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            # Calculate the sum of the current triplet
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                # Triplet found, add to result list
                triplets.append([nums[i], nums[left], nums[right]])
                # Move both pointers past duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # Move pointers inward
                left += 1
                right -= 1
            elif current_sum < 0:
                # If the sum is less than zero, move the left pointer to increase the sum
                left += 1
            else:
                # If the sum is more than zero, move the right pointer to decrease the sum
                right -= 1

    return triplets


threeSum([-1,0,1,2,-1,-4])
threeSum([0,1,1])
threeSum([0,0,0])
