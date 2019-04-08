from functools import *

def intersect(*ar):#교집합
    return reduce(__intersectSC, ar)

def __intersectSC(listX,listY):
    setList=[]
    for x in listX:
        if x in listY:
            setList.append(x)
    return setList

def difference(*ar):
    return reduce(__difference,ar)

def __difference(A,B):
    setList=[]
    for x in A:
        if not x in B:
            setList.append(x)
    return setList

def union(*ar):
    setList=[]
    for item in ar:
        for x in item:
            if not x in setList:
                setList.append(x)
    return setList