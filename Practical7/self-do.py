def bubble_sort(arr):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(arr)):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                swap = False

# 输入处理
L = input("请输入一组数字，用逗号分隔: ").strip()
# 转换为整数列表
nums = [int(x) for x in L.split(',')]

bubble_sort(nums)
print(nums)