# 变量赋值，查看内存地址
x = 1
print(id(x))    # --> 2330081650992

x = 2
print(id(x))    # --> 2751813544272

# 同时赋值多个变量
a = (2, 54, 66)
b, c, d = a     # 变量个数 多 或 少 于值得个数，会报错，错误类型 ValueError
print(b, c, d)