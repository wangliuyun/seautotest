import unittest
import requests

class MyTestCase(unittest.TestCase):
    # 每次方法执行之前执行
    def setUp(self):
        print("_____起始_____")
    # 执行测试的函数,注意：所有执行测试的方法必须test开头,执行顺序后面的罗马数字升序执行
    def test_01(self):
        print("这是第一个用例")
        # 断言true等于true
        self.assertEqual(True ,True)
    def test_02(self):
        print("这是第二个用例")
        # 断言true等于true
        self.assertEqual(True,True)
    def tearDown(self):
        print("-----结束-----")




if __name__ == '__main__':
    unittest.main()
