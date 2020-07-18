def bubblesort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swaps = swaps+1
    print("Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}".format(swaps,arr[0],arr[n-1]))

num = int(input())
arr = list(map(int, input().rstrip().split()))
bubblesort(arr)
