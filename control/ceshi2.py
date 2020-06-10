import requests
import json


# 例子三：将unittest与requests模块结合 进行接口测试
# 1.将requests的post请求与get请求封装成一个类，便于在unittest中进行调用


class RunMain(object):
    def get(self, url, data):
        res = requests.get(url=url,data=data).json()
        return res

    def post(self, url, data):
        res = requests.post(url=url, data=data).json()
        return res

    def run_main(self, url, method, data=None):
        res = None

        # 不区分大小写
        if method.lower() == 'GET':
            res = self.get(url, data)
        else:
            res = self.post(url, data)
        return res
