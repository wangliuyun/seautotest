import unittest
# def setUpClass(cls): 和 def tearDownClass(cls):同样也是unittest内置方法但要注意的是需要加上：@classmethod来进行装饰，它们的意思是在执行用例是只有最初和
# 最后会被执行，适用场景是：例如登录接口会返回一个token，将这个token提取出来放在header中，这样其他接口才可以正常访问

class MyTestCase(unittest.TestCase):

    # 必须装饰这个类
    @classmethod
    def setUpClass(cls):
        print('最初执行一次')

    def test_01(self):
        print("这是用例1")
        self.assertEqual(True,True)
    def test_02(self):
        print("这是用例2")
        self.assertEqual(True,True)

    @classmethod
    def tearDownClass(cls):
        print("最后一次执行")
if __name__ == '__main__':
    unittest.main()