# coding=utf-8


print("z", "n")      # seq 默认以 空格 分割多个值之间输出； end 默认以 换行 分隔多个print输出
print("d, e, f", sep=",")   # 设置 seq 的分隔符，输出 d, e, f
print("a", "b", "c", end=",")   # 设置 end 分割，将 换行 转为 “，”；输出 a b c，ww ee rr
print("ww", "ee", "rr")