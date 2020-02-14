import unittest


#创建套件
from case.test_list import TestUserList

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestUserList))

#运行测试
unittest.TextTestRunner(verbosity=2).run(suite)