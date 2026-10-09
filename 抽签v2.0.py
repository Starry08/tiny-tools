"""

把名单写成如下形式:
A
B
C
D
E
F
G
H
I
J
K
...

"""

import random as r

try :

    print("输入名单，每行一个，输入空行结束：")

    pool = []

    while True:

        line = input()

        if line.strip() == '':

            break

        pool.append(line.strip())

    n = int(input("抽几人："))

    index = r.sample(range(len(pool)),n)

    print("读取后的列表：",pool)

    print("索引：",index)

    print("抽中的人：",[pool[i] for i in index])

    input("抽取完毕，按下回车键退出...")

except :

    print("输入格式错误！")