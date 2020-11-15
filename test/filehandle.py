# -*- coding: utf-8 -*-
# @Time     : 2020/11/6 6:48
# @Author   : chw
# @File     : filehandle.py

# f = open("data.txt")
# # 文件是否可读
# print(f.readable())
# # 读取文件中的一行
# print(f.readline()
# # 读取文件中的所有行（文件较大时不建议使用，会出现卡死）(如果有换行会默认增加\n，返回的结果会存在一个列表中)
# print(f.readlines())
#
# # 关闭文件，释放资源，否则可能会出现死锁
# f.close()


# with语句块，可以将文件打开操作之后，自动关闭文件
# 图片读取需要使用rb  读取二进制的格式
# 正常的文本，可以使用rt,也就是它的默认格式即可

with open("data.txt") as f:
    print(f.readable())
    while True:
        line = f.readline()
        if line:
            # 打印结果有空行，是因为print有回车的操作，文件中又有换行，所以回车两次，就出现了空行
            print(line)
        else:
            break



