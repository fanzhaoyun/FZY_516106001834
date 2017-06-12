# -*- coding:utf-8 -*-

'''
随机生成图并找出所有的prime Paths
'''

__author__ = "FZY"

from random import randint
import copy


def readGraph(filePath):
    
    pass

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
    return graph

def findPrimePath(graph):
    simplePath = [[i] for i in range(len(graph))] #每个节点的初始长度
    primePath = []
    tempPath = []
    while len(simplePath) != 0 :
        #simplePath = [x for x in simplePath if graph[x[-1]] != 0]
        for x in simplePath:
            if len(graph[x[-1]]) == 0:
                tempPath.append(x)
        simplePath = [f for f in simplePath if len(graph[f[-1]]) != 0]
        csize = len(simplePath)
        for i in range(csize):
            #print(simplePath[i][-1])
            temp = graph[simplePath[i][-1]]
            copySp = copy.deepcopy(simplePath[i])
    
            if temp[0] == simplePath[i][0]:  #如果加入的节点存在于当前路径，则证明有环，直接加入primePath
                simplePath[i].append(temp[0])
                primePath.append(simplePath[i])
                simplePath[i] = []
            elif temp[0] in simplePath[i]:  #如果重复节点不是第一个，则当前路径加入判断路径，如果是最长链则加入primePath，否则删除
                tempPath.append(simplePath[i])
                simplePath[i] = []
            else:
                simplePath[i].append(temp[0])
            for j in range(1,len(temp)):
                if temp[j] == copySp[0]:
                    depcopysp = copy.deepcopy(copySp)
                    depcopysp.append(temp[j])
                    primePath.append(depcopysp)
                elif temp[j] in copySp:
                    tempPath.append(copySp)
                    #simplePath[i] = []
                else:
                    depcopysp = copy.deepcopy(copySp)
                    depcopysp.append(temp[j])
                    simplePath.append(depcopysp)
        simplePath = [f for f in simplePath if len(f) != 0] #删除空链

    for x in tempPath:
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
                for sp in tempPath:
                    spSet = [str(y) for y in sp]
                    spSet = "".join(spSet)
                    if tempSet != spSet and tempSet in spSet:
                        flag = 1
                        break
            if flag == 0:
                primePath.append(x) 
    return primePath


def checkdup(primePath):
    for x in primePath:
            tempSet = [str(y) for y in x]
            tempSet = "".join(tempSet)
            flag = 0
            for sp in primePath:
                spSet = [str(y) for y in sp]
                spSet = "".join(spSet)
                if tempSet in spSet and tempSet != spSet:
                    print(x)
                    print(sp)
                    return False
    return True

if __name__ == '__main__':
    nodeNum = 10
    graph = [[1, 4], [3], [3], [1, 2], [1]]
    #graph = [[1], [2,37], [3], [4,6], [5], [3], [7], [8,21], [9], [10,11],[11],[12,13],[14],[14],[15],[16,38],[17,18],[18],[19],[15],[15],[22],[23],[24],[25,28],[26],[24,27],[28],[29,34],[30],[31,34],[32],[30,33],[34],[22,35],[22],[1],[],[7]]
    print(graph)
    primePath = findPrimePath(graph)
    print(primePath)
    print(len(primePath))
    print(checkdup(primePath))
    