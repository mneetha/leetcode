def maxArea(height) -> int:
    cur_area = 0
    index = 0
    max_index = len(height)-1
    l,r= index,max_index
    cur_area = min(height[l], height[r]) * (r - l)
    while l <r:
        if height[l]<height[r]:
            l =l+1
        else:
            r=r-1
        new_area_1 = min(height[l],height[r])*(r-l)
        if cur_area < new_area_1:
            cur_area = new_area_1


    return cur_area

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([8,7,2,1]))