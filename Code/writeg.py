# -*- coding:utf-8 -*-
'''
Created on 2017��5��7��

@author: dell
'''

def readGraph(fileName):
    graph = []
    with open(fileName,'r') as f:
        while 1:
            line = f.readline()
            if not line:
                break
            line = line.strip('[]\n')
            a = list(line.split(","))
            
            #a = [int(x) for x in a]
            if a[0] == '-1':
                a = ()
            graph.append(a)
    
    return graph

def writeGraph(graph,nodes,i):
    with open("测试用例/otheranswer/answer"+str(i)+".txt",'w+') as f:
        f.write(str(nodes-1))
        f.write("\n")
        for g in graph:
            #g = [str(x) for x in g]
            if not g:
                f.write("[-1]\n")
                continue
            f.write(str(g))
            f.write("\n")
            
if __name__ == '__main__':
    for i in range(0,16):
        graph = readGraph('shhe_result/anwser/anwser'+str(i))
        print(graph)
        #nodes = len(graph)
        #writeGraph(graph,nodes,i)