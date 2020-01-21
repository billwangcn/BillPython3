def conflict(state, nextX):  # state为已摆放的棋子的位置的元组，比如（1,3,0）
    nextY = len(state)  # 获取当前行号
    for i in range(nextY):  # 检查每一个已摆放的棋子和当前行要摆放的棋子的位置（nextX, nextY）是否冲突
        if abs(state[i] - nextX) in (0, nextY - i):  # 关键！若是两个棋子 行差值 的绝对值 出现在元组 （0，行差值）中，则冲突发生，返回True
            return True
    return False  # 无冲突，可行的摆放位置


def queens(num=8, state=()):  # num为棋盘的行数，state为已摆放的棋子的列数汇总，类型为 元组
    if len(state) == num - 1:  # 检查是否最后一行，如果是最后一行，则执行终极操作，不再递归
        for pos in range(num):  # pos从 0 到 棋盘行数 - 1
            if not conflict(state, pos):  # 检查是否冲突yield (pos,)
        #                             #没有冲突，返回列数的元组
                return ""
    else:  # 不是最后一行
        for pos in range(num):  # 检查当前行每一个列的位置
            if not conflict(state,pos):  # 检查是否有冲突for result in queens(num, state + (pos,)): #递归调用queens，不过找到了更多的一行的摆放位置，所以，加上（pos,）
                # 如果是最后一行，返回一个数字的元组，比如，（2）
                # 此时，如果pos为0，那么，倒数第二行返回的为两个数字的元组，比如，（0, 2）
                # 调用每返回一层，返回的元组的长度就加1，直到最后用户在外部调用queens的位置
                # 返回所有行的皇后位置的 元组，其长度为行数
                yield (pos,) + result  # 这里和想象的有些不同，下面是在Python 2.7.14上运行代码发生的错误
                # 程序执行后没问题，可是~~看来还没想明白！（下面有进一步分析）

def queens2(num=8, state=()):
    for pos in range(num):              #重复部分
        if not conflict(state, pos):    #重复部分
            if len(state) == num - 1:   #分支1
                yield (pos,)
            else:                       #分支2
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


print(list(queens2(8)))