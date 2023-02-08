def multi_list(num):
    res = 1
    for i in num:
        res *= i
    return res



lst1 = [1,2,3,4,5]
result =multi_list(lst1)
print(result)
