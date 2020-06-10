import unittest

# 导入请求类
from control import ceshi2


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # 初始化请求类
        self.run = ceshi2.RunMain()

    def test_01(self):
        '''
        查询红余额接口
        get请求方法
        :return:
        '''
        print("这是第一个用例")
        url = 'http://ios.wecash.net/biz/wallet/amount'
        data = 'CUSTOMER_ID=56256A951F81F0BCA10780AD02139B29'
        rep = self.run.get(url,data)
        print(rep)
        # if rep['code'] == 0:
        #     print("通过")
        # else:
        #     print("no通过")
        # 对返回结果进行断言（内置断言） 提取的值，断言的值，匹配不上的输出信息
        self.assertEqual(rep['code'],0,'查询红包接口失败')
        # self.assertEqual() 验证两个是否相等
        # self.assertNotEqual() 判断不相等
        # self.assertTrue（） 布尔类型判断 如果返回是 True == True

    def test_02(self):
        '''
        豆瓣api , 发一条广播
        :return:
        '''
        print("这是第二条用例")
        url = 'https://www.cnblogs.com/wangsen-123/ajax/GetViewCount.aspx?postId=9098555'
        data  = "{'postId': 9098555}"
        rep1 = self.run.post(url,data)
        print(rep1)
        self.assertEqual(rep1,929,'发送广播失败')


if __name__ == '__main__':
    unittest.main()