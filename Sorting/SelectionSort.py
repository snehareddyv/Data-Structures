class Solution:
    def SelectionSort(arr):
        for i in range(0,len(arr)-1):
            min = i
            for j in range(i+1, len(arr)):
                if arr[min] > arr[j]:
                    min = j
            arr[min], arr[i] = arr[i], arr[min]
        return arr
