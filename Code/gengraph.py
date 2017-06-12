# -*- coding:utf-8 -*-
'''
Created on 2017��4��22��

@author: dell
'''
from random import randint

def genGraph(nodeNum):
    graph = [[] for i in range(nodeNum)]
    indegree = [0 for i in range(nodeNum)]   #ͼ�ڵ�����
    outdegree = [0 for i in range(nodeNum)]  #ͼ�ڵ�ĳ���
    while(0 in indegree[1:] or 0 in outdegree[:nodeNum-1]):  #�ж��Ƿ�����Ȼ��߳���Ϊ0�ĵ�,��ȵ���ʼ�ڵ㲻�жϣ����ȵ�
        start = randint(0, nodeNum-1)
        end = randint(0, nodeNum-1)
        while(start == end):                 #����������һ���������
            start = randint(0, nodeNum-1)
            end = randint(0, nodeNum-1)  
        if end not in graph[start]:
            graph[start].append(end)
        indegree[end] += 1
        outdegree[start] += 1
        
    return graph

def writeGraph(graph,i):
    with open("case"+str(i)+".txt",'w+') as f:
        for g in graph:
            #g = [str(x) for x in g]
            if not g:
                f.write("-1\n")
                continue
            f.write(str(g))
            f.write("\n")
        
if __name__ == '__main__':
    nodeNum = 15
    for i in range(0,16):
        print("case" + str(i))
#         graph = genGraph(nodeNum)
#         writeGraph(graph,i)
#         print(graph)
    