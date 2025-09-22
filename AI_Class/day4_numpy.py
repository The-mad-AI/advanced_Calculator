import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(arr.dtype)
print(arr + 2)
print(arr * 2)
print( arr ** 2)


even_numbrs = np.arange(10,21,2)
print(even_numbrs)
sum_numbrs = np.sum(even_numbrs)
print(sum_numbrs)
if 12 in even_numbrs:
    print("ast")
else:
    print("nist")







numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 2]
count_dict = {}
for num in numbers :
    if num in count_dict:
        count_dict[num] +=1
else:
    count_dict[num] = 1
for num , count in count_dict.items():
    if count > 1:
        print(f"add {num}: {count}")

