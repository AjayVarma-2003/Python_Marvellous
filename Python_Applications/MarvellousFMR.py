def FilterX(Task, Values):
    Result = []

    for i in Values:
        ret = Task(i)
        if(ret == True):
            Result.append(i)

    return Result

def MapX(Task, Values):
    Result = []

    for i in Values:
        ret = Task(i)
        Result.append(ret)

    return Result

def ReduceX(Task, Values):
    Result = 0

    for i in Values:
        Result = Task(Result, i)

    return Result