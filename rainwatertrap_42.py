def trap(height):
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    total_water = 0

    # Move from both ends of the array towards the center
    while left < right:
        if height[left] < height[right]:
            # If the left boundary is shorter
            if height[left] >= left_max:
                left_max = height[left]  # Update left_max if necessary
            else:
                total_water += left_max - height[left]  # Calculate water above current bar
            left += 1  # Move left pointer
        else:
            # If the right boundary is shorter
            if height[right] >= right_max:
                right_max = height[right]  # Update right_max if necessary
            else:
                total_water += right_max - height[right]  # Calculate water above current bar
            right -= 1  # Move right pointer

    return total_water

# print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))










