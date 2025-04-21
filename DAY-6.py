''' Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.'''

def BinarySearch(list,target):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left+right)//2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1
list = list(map(int,input().split()))
target = int(input())
print(BinarySearch(list,target))
