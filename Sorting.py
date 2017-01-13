def sort(arr):
    for idx in range(1, len(arr)):
        x = arr[idx]
        j = idx - 1
        while j >= 0 and arr[j] > x:
            arr[j+1] = arr[j]
            j = j -1
        arr[j+1] = x
    return arr

if __name__ == "__main__":
    arr = raw_input("Give me list of numbers: ").split(" ")
    print sort(arr)
