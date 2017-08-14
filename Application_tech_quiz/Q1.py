# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 00:06:38 2017

@author: HSIN
"""

# input k
while(1):
    try:
        k = input('Input K: ')
        k = int(k)
        
        if k <= 0 or k >= 10**9:
            print('Please make sure 0 < K < 10^9')
        else:
            break
        
    except ValueError:
        print('Please make sure K is an integer')
    
    
# input the number list
while(1):
    try:
        user_input = input('Input a list of N integers: ')
        numbers = user_input.split(' ')
        numbers = [int(x) for x in numbers] 
        
        if len(numbers) < 2 or len(numbers) > 10**5:
            print('Please make sure 2 <= N <= 10^5')
        else:
            break
        
    except ValueError:
        print('Please make sure each number in the list is an integer')



# sort the list from small to large
# Timsort O(nlogn)
numbers = sorted(numbers)


count = 0

# set left pointer and right pointer to the list
left = 0
right = 0

# find pairs with diff == k
# O(nlogn)
while(right < len(numbers)):
    
    # the diff == k, take count
    if numbers[right] - numbers[left] == k:
        
        l = left
        r = right
        left_dup = 1
        right_dup = 1
        
        # consider the duplication on left and right side
        while(1):
            if l + 1 < len(numbers) and numbers[l+1] == numbers[left]:
                left_dup += 1
                l += 1
            else:
                left = l + 1
                break
        
        while(1):
            if r + 1 < len(numbers) and numbers[r+1] == numbers[right]:
                right_dup += 1
                r += 1
            
            else:
                right = r + 1
                break
        
        
        count += left_dup * right_dup
        
    # the diff > k, move the left pointer
    elif numbers[right] - numbers[left] > k:
        left += 1
        
    # the diff < k, move the right pointer
    else:
        right += 1


print('The number of pairs whose difference is K:', count)


# Time Complexity: O(nlogn)
# Space Complexity: O(n)