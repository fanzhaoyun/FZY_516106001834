# -*- coding:utf-8 -*-
'''
Created on 2017年5月8日

@author: dell
'''

import primePath
import unittest
import time 
from HTMLTestRunner import HTMLTestRunner

class TestPrime(unittest.TestCase):
    
    def readAnswer(self,fileName):
        graph = []
        with open(fileName,'r') as f:
            nodeNum = int(f.readline())
            while 1:
                line = f.readline()
                if not line:
                    break
                line = line.strip('[]\n')
                a = list(line.split(","))
                a = [int(x) for x in a]
                if a[0] == -1:
                    a = []
                graph.append(a)
        
        return nodeNum,graph
    
    def setUp(self):
        print("test start-->")
        self.gp = primePath.readGraph('测试用例/case10.txt')
        self.nn,self.tanswer = self.readAnswer('测试用例/hshanswer/answer10.txt')
        self.prime = primePath.findPrimePath(self.gp)
    
    def test_prime(self):
        """测试prime：@范照云"""
        nodeNum = self.nn
        prime = self.prime
        prime.sort(key=lambda x:(len(x),x))
        tanswer = self.tanswer
        self.assertEqual(len(prime), nodeNum, msg="nodes number false!!!")
        self.assertEqual(prime, tanswer, msg="prime path false!!!")
            
    def tearDown(self):
        print("test end <--")
    
if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(TestPrime("test_prime"))

    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # 定义报告存放路径
    # filename = './report/result.html'
    filename = './report/fzy-primePath-' + now + '-result.html'
    fp = open(filename, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,                  # 指定测试报告文件
                        title='百度搜索测试报告',        # 定义测试报告标题 
                        description='用例执行状况：')    # 定义测试报告副标题
    runner.run(testunit)    # 运行测试用例
    fp.close()  # 关闭报告文件
    