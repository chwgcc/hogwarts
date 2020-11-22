# -*- coding: utf-8 -*-
# @Time     : 2020/11/20 7:18
# @Author   : chw
# @File     : test_wx.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 使用cookie登陆该文件会报错，可以使用test_wx1进行使用cookie登陆

class TestWX():
    def setup(self):
        option = Options()
        # 注意9222 端口要与命令行启动的端口保持一致，且cmd不能关闭：chrome --remote-debugging-port=9222
        # 想在命令行输入以上命令，需将chrome安装路径添加环境变量path中
        option.debugger_address = "127.0.0.1:9222"
        # 去掉options将不再复用，想要复用就需要添加上options参数
        self.driver = webdriver.Chrome(options=option)
        # self.driver = webdriver.Chrome()

    # def teardown(self):
    #     self.driver.quit()


    # @pytest.mark.skip
    def test_wx1(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.ID, 'menu_contacts').click()
    # @pytest.mark.skip
    def test_cookie(self):
        # 获取到当前页面的cookie
        cookies = self.driver.get_cookies()
        # 格式化的快捷键Alt+Ctrl+L
        # cookies = [
        #     {'domain': '.qq.com', 'expiry': 1606009578, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.qq.com', 'expiry': 1606095918, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.256861384.1606008688'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1606039721, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '4tt3v1s'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688853469235889'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'jCFtsZ3mdEl7eFc5PPMJ6rQadZ44ijvAKPmsWlvc-KV8DR1yfaDQX43zNHu1zzkV0NXsLp7HSbGTHlf09AeAgZG-P4bDbuDpvDOGyptL-cc7VpPs45neG2-a3jl0W3DcGJxKJ_Do_aqkfX79aHUx5vB2XQg9CmM4i9Z6hdWQsWYeQzJ3Kg6YtobodsYjx5X-MRUsEFo6t1CRIwlUMm5fjMDs3h-QWyOXoEg2K8xojfBV_iQTqZJppo8f9PUHplx6zHYPKvF4--Ea8wTf1xSghQ'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688853469235889'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970325044197427'}, {'domain': '.work.weixin.qq.com', 'expiry': 1637363815, 'httpOnly': False,
        #                                     'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/',
        #                                     'secure': False, 'value': '1605703362,1605703380,1605827816'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a2670602'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
        #      'path': '/', 'secure': False, 'value': '1605827816'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '01011512'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'xE04uJjGag0WTaZeNs-RvqUPsOtLfpwOq-qnK3i7qmwBw4GkobJ_xATIdW-9NGk7'},
        #     {'domain': '.qq.com', 'expiry': 1669081518, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.745212008.1605703362'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1637239133, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1608601519, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'}]

        print(cookies)
        # 打开页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 添加cookie信息时，需要上传的参数为字典类型，所以按此方法上传
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 刷新页面
        self.driver.refresh()
