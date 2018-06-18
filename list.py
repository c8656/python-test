
list = [1,2.3,4]

print (list)
print (list[1])

list_y = list # 等号 是 传递 内存地址
list_y[0] = 5
print (list_y)


list_copy = list.copy()
print (list_copy)

list_copy[0] = 6
print (list_copy)
print (list)
