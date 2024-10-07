import os
os.system('cls')

class Search:

    def linearSearch(self, arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                index = i

        return index
    
    def binarySearch(self, arr, x):
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                l = mid + 1
            else: 
                r = mid - 1

searcher = Search()

arr = [2, 5, 6, 89, 54, 24, 12]
x = 6

index = searcher.linearSearch(arr,x)
print(index)

index = searcher.binarySearch(arr,x)
print(index)
