def find_minimum(nums):
    minimum = float("inf")
    if len(nums) == 0:
        return None
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum
        
def sum(nums):
    tot = 0
    for num in nums:
        tot += num
    return tot

def get_estimated_spread(audiences_followers):
    num_followers = len(audiences_followers)
    if num_followers == 0:
        return 0
    else:
        return sum(audiences_followers)/ num_followers * ( num_followers ** 1.2 )

def binary_search(target, arr):
    begin = 0
    end = len(arr) - 1
    mid = (begin + end) //2
    print(begin)
    print(end)
    print(mid)
    while begin != end:
        if end == begin and target != arr[mid]:
            return None
        elif target == arr[mid]:
            return arr[mid]
        elif target > arr[mid]:
            begin = mid + 1
            mid = (begin + mid) //2
        else:
            end = mid - 1
                mid = (begin + mid) //2
