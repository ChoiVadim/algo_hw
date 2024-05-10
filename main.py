from method1 import divide_array, find_max_diff
from method2 import divide_students


k = int(input("Enter k: "))
arr = input("Enter array: ").split()
arr = [(i, int(j)) for i, j in enumerate(arr, 1)]
arr_for_method2 = arr


final_array = divide_array(arr, k)
max_sum = str(find_max_diff(final_array, k))
print(max_sum)

with open("Partition1.txt", "w") as f:
    for arr in final_array:
        f.write(" ".join(f"{i}({j})" for i, j in arr) + "\n")

res = divide_students(arr_for_method2, k)
print(res[1])

with open("Partition2.txt", "w") as f:
    for arr in res[0]:
        f.write(" ".join(f"{i}({j})" for i, j in arr) + "\n")
