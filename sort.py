import os
os.system('cls')

class Sort:

    def bubbleSort(self, arr):
        n = len(arr)

        for i in range(n-1):
            swapped = False

            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

            if not swapped:
                break

        return arr

    def insertionSort(self, arr):
        n = len(arr)

        for i in range(1,n):
            key = arr[i]
            
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = key

        return arr
    
    def mergeSort(self, arr):
        n = len(arr)

        if n > 1:
            mid = n // 2
            l = arr[:mid]
            r = arr[mid:]

            l = self.mergeSort(l)
            r = self.mergeSort(r)

            arr = self.merge(l, r)

        return arr
    
    def merge(self, l, r):
        result = []
        i = j = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1

        result.extend(l[i:])
        result.extend(r[j:])

        return result

sorter = Sort()

arr = [2, 5, 6, 89, 54, 24, 12]

sorted = sorter.bubbleSort(arr)
print(sorted)

sorted = sorter.insertionSort(arr)
print(sorted)

sorted = sorter.mergeSort(arr)
print(sorted)
