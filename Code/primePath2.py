# -*- coding:utf-8 -*-

'''
随机生成图并找出所有的prime Paths
'''

__author__ = "FZY"

from random import randint
import copy

def readGraph(fileName):
    graph = []
    with open(fileName,'r') as f:
        f.readline()
        while 1:
            line = f.readline()
            if not line:
                break
            line = line.strip('[]\n')
            a = list(line.split(","))
            a = [int(x) for x in a]
            sorted(a)
            if a[0] == -1:
                a = []
            graph.append(a)
    
    return graph
 
def getNext(t, next_list):  
    next_list[0] = -1  
    j = 0  
    k = -1  
    while j < len(t) - 1:  
        if k == -1 or t[j] == t[k]:  
            j = j + 1  
            k = k + 1  
            next_list[j] = k  
        else:  
            k = next_list[k]
            
def KMP_Match(s, t):  
    slen = len(s)  
    tlen = len(t)  
    if slen >= tlen:  
        i = 0
        j = 0  
        next_list = [-2 for i in range(len(t))]  
        getNext(t, next_list)    
        while i < slen:  
            if j == -1 or s[i] == t[j]:  
                i = i + 1  
                j = j + 1  
            else:  
                j = next_list[j]  
            if(j == tlen):  
                return i - tlen  
    return -1         

def genGraph(nodeNum):
    graph = [[] for i in range(nodeNum)]
    indegree = [0 for i in range(nodeNum)]   #图节点的入度
    outdegree = [0 for i in range(nodeNum)]  #图节点的出度
    while(0 in indegree[1:] or 0 in outdegree[:nodeNum-1]):  #判断是否还有入度或者出度为0的点,入度的起始节点不判断，出度的
        start = randint(0, nodeNum-1)
        end = randint(0, nodeNum-1)
        while(start == end):                 #生成两个不一样的随机数
            start = randint(0, nodeNum-1)
            end = randint(0, nodeNum-1)  
        if end not in graph[start]:
            graph[start].append(end)
        indegree[end] += 1
        outdegree[start] += 1
        '''
        #下面处理不连通情况，但鉴于出现概率较低，故不予考虑    
        for i in range(1, nodeNum):
            colle = set(graph[i])
            if max(colle) < i :
                graph[i].append(i+1)
        '''
    for i in range(nodeNum):
        graph[i].sort()

    return graph


def addPath(graph, simplePath, i, primePath, tempPath, tpcirclePath):
    temp = graph[simplePath[i][-1]]
    copySp = copy.deepcopy(simplePath[i])
    if temp[0] == simplePath[i][0]: #如果加入的节点存在于当前路径，则证明有环，直接加入primePath
        simplePath[i].append(temp[0])
        primePath.append(simplePath[i])
        tpcirclePath.append(simplePath[i])
        simplePath[i] = []
    elif temp[0] in simplePath[i]: #如果重复节点不是第一个，则当前路径加入判断路径，如果是最长链则加入primePath，否则删除
        tempPath.append(simplePath[i])
        simplePath[i] = []
    else:
        simplePath[i].append(temp[0])
    for j in range(1, len(temp)):
        if temp[j] == copySp[0]:
            depcopysp = copy.deepcopy(copySp)
            depcopysp.append(temp[j])
            primePath.append(depcopysp)
            tpcirclePath.append(depcopysp)
        elif temp[j] in copySp:
            tempPath.append(copySp)
        else:
            depcopysp = copy.deepcopy(copySp)
            depcopysp.append(temp[j])
            #simplePath[i] = []
            simplePath.append(depcopysp)

def checkRepeat(tempPath,simplePath,tpcirclePath,primePath):
    for x in tempPath:
        tempSet = [str(y) for y in x]
        flag = 0
        for sp in simplePath:
            spSet = [str(y) for y in sp]
            if KMP_Match(spSet, tempSet) != -1:
                flag = 1
                break
            
        # 新生成的环是否包含判断路径中的存在
        if flag == 0:
            for pp in tpcirclePath:
                spSet = [str(y) for y in pp]
                if KMP_Match(spSet, tempSet) != -1:
                    flag = 1
                    break       
        if flag == 0:
            primePath.append(x)

def length_cmp(x,y):
    return len(x)-len(y)

def writePrimePath(primePath,i):
    primePath.sort(key=lambda x:(x[0]))
    primePath.sort(key=lambda x:(len(x)))
    with open("测试用例/answer/result"+str(i)+".txt",'w+') as f:
        f.write(str(len(primePath)))
        f.write("\n")
        for g in primePath:
            f.write(str(g))
            f.write("\n")
    
    
def findPrimePath(graph):
    simplePath = [[i] for i in range(len(graph))] #每个节点的初始长度
    primePath = []
    tempPath = []
    tpcirclePath = []
    while len(simplePath) != 0 :

        #simplePath = [x for x in simplePath if graph[x[-1]] != 0]
        for x in simplePath:
            if len(graph[x[-1]]) == 0:
                tempPath.append(x)
        simplePath = [f for f in simplePath if len(graph[f[-1]]) != 0]
        csize = len(simplePath)
        for i in range(csize):
            temp = graph[simplePath[i][-1]]
            copySp = copy.deepcopy(simplePath[i])
            if temp[0] == simplePath[i][0]: #如果加入的节点存在于当前路径，则证明有环，直接加入primePath
                simplePath[i].append(temp[0])
                primePath.append(simplePath[i])
                tpcirclePath.append(simplePath[i])
                simplePath[i] = []
            elif temp[0] in simplePath[i]: #如果重复节点不是第一个，则当前路径加入判断路径，如果是最长链则加入primePath，否则删除
                tempPath.append(simplePath[i])
                simplePath[i] = []
            else:
                simplePath[i].append(temp[0])
            for j in range(1, len(temp)):
                if temp[j] == copySp[0]:
                    depcopysp = copy.deepcopy(copySp)
                    depcopysp.append(temp[j])
                    primePath.append(depcopysp)
                    tpcirclePath.append(depcopysp)
                elif temp[j] in copySp:
                    tempPath.append(copySp)
                else:
                    depcopysp = copy.deepcopy(copySp)
                    depcopysp.append(temp[j])
                    #simplePath[i] = []
                    simplePath.append(depcopysp)
        simplePath = [f for f in simplePath if len(f) != 0] #删除空链
       
        checkRepeat(tempPath,simplePath,tpcirclePath,primePath)
        tempPath = []
        tpcirclePath = []

    
    #最后一步，对primePath去重
    prime = []
    for pp in primePath:
        if pp not in prime:
            prime.append(pp)
    
    '''
    for x in tempPath[(count-1)%2]:
            tempSet = [str(y) for y in x]
            tempSet = "".join(tempSet)
            flag = 0
            for sp in primePath:
                spSet = [str(y) for y in sp]
                spSet = "".join(spSet)
                if tempSet in spSet:
                    flag = 1
                    break
            
            if flag == 0:
                primePath.append(x)
    '''
    return prime


def checkdup(primePath):
    for x in primePath:
            tempSet = [str(y) for y in x]
            #tempSet = "".join(tempSet)
            for sp in primePath:
                spSet = [str(y) for y in sp]
                #spSet = "".join(spSet)
                if KMP_Match(tempSet,spSet) != -1 and tempSet != spSet: 
                    print(x)
                    print(sp)
                    return False
    return True

if __name__ == '__main__':
    nodeNum = 10
    #graph = genGraph(nodeNum)
    #graph = [[7, 8, 1, 6], [0, 13, 14], [12, 8, 13], [9, 6, 0, 13, 2], [6, 10, 14], [4, 9], [14, 0], [6], [10, 1], [3, 5], [3, 11], [1, 4, 8, 5], [3, 14], [8, 12], [11, 4]]
    #graph = [[1], [2,37], [3], [4,6], [5], [3], [7], [8,21], [9], [10,11],[11],[12,13],[14],[14],[15],[16,38],[17,18],[18],[19],[15],[15],[22],[23],[24],[25,28],[26],[24,27],[28],[29,34],[30],[31,34],[32],[30,33],[34],[22,35],[22],[1],[],[7]]
    #graph = [[1],[2,20],[3,5],[2,4],[2],[6],[7,19],[8],[9,10],[13],[11,12],[13],[13],[14],[15,16],[13],[17,18],[13],[13],[1],[]]
    
    for i in range(0,16):
        graph = readGraph('测试用例/case'+str(i)+'.txt')
        primePath = findPrimePath(graph)
        writePrimePath(primePath,i)
    
    '''
    filename = "测试用例/case0.txt"
    graph = readGraph(filename)
    print(graph)
    primePath = findPrimePath(graph)
    #writePrimePath(primePath,filename)
    print(primePath)
    print(len(primePath))
    #print(checkdup(primePath))
    '''
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
'''
        for x in tempPath:
            tempSet = [str(y) for y in x]
            tempSet = "".join(tempSet)
            flag = 0
            for sp in simplePath:
                spSet = [str(y) for y in sp]
                spSet = "".join(spSet)
                if tempSet in spSet:
                    flag = 1
                    break
            
            #新生成的环是否包含判断路径中的存在
            if flag == 0:
                for pp in tpcirclePath:
                    spSet = [str(y) for y in pp]
                    spSet = "".join(spSet)
                    if tempSet in spSet:
                        flag = 1
                        break
'''   
