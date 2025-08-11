def sort_arr(arr):
    if len(arr) == 1:
        return
    temp = arr.pop()
    sort_arr(arr)
    insert_arr(arr, temp)
    
def insert_arr(arr, temp):
    if len(arr) == 0 or arr[-1] <= temp:
        arr.append(temp)
        return
    
    val = arr.pop()
    insert_arr(arr, temp)
    arr.append(val)
    
if __name__ == '__main__':
    nums = [2, 3, 7, 6, 4, 5, 9]
    sort_arr(nums)
    print(nums)
    
