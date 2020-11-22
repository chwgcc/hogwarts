# -*- coding: utf-8 -*-
# @Time     : 2020/11/22 10:35
# @Author   : chw
# @File     : test_wx1.py
import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWX1:
    def setup(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case1(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.ID, 'menu_contacts').click()

    def test_cookie1(self):
        # cookies = self.driver.get_cookies()
        cookies = [
            {'domain': '.qq.com', 'expiry': 1606012841, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'y4sESv0coCQlD_o5L3I6CfLEZuCWJpxFj3N6zl7wPMEWIxwOZSeYrgq6-OWcmzeso3SimK6aN1bqVGhTXtGbK0lt_ls4ASotdmda-eojy6GKbB9xNbhT8GMsTqtGGQtk2OX-wXzzjPzKB5jgT3ei8OB_nnLa_LGuTH2VH9T-FyBz8Y-OXToOCdjGBS2p1JBCpss1yzHiOj95sGGBdz26V-Mi8TR_8wvTmRo6kQZBjjO7AWdTUBOq6ucBAwTkH8eH0MWX4sHULaLYDqYcyMFcKA'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a7122173'},
            {'domain': '.qq.com', 'expiry': 1669084781, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.745212008.1605703362'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True,
             'value': '01011512'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': True, 'value': '1605827816'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1606041700, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '455sbep'},
            {'domain': '.qq.com', 'expiry': 1606099181, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.256861384.1606008688'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853469235889'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1606039721, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': True, 'value': '4tt3v1s'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853469235889'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325044197427'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'xE04uJjGag0WTaZeNs-RvtXhrKAI7LsI_GMwmI6Iov8K9d9g1huqKWqf8cGcrynB'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1637239133, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': True, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1637363815, 'httpOnly': False,
             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True,
             'value': '1605703362,1605703380,1605827816'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1608604782, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'}]
        # 打开企业微信首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 加入cookie信息
        for cookie in cookies:
            # 因为expiry必须为整形，且在服务器端存储了一份，这个可以去掉
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 刷新页面
        self.driver.refresh()
        sleep(3)

    # 此方法用来将cookie存储下来
    def test_database(self):
        cookies = [
             {'domain': '.qq.com', 'expiry': 1606025132, 'httpOnly': False, 'name': '_gat', 'path': '/',
              'secure': False, 'value': '1'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
              'value': '1688853469235889'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
              'value': '2RR7mwc-5jSjawDqKuHh4Nq_O1uuH53OKBA-6lywqylVcrOWQvP2RHlmSdlqPfm5aQFcUb629ju6zqwbg8Gk_7GipUD9XXT75n1cPPVf0zOo1GRHVybxnNdYd0NOmZdxwuv-CY6UjALmeuumBV16mTLYuRfD5NmEqkLO-Mk02ARbHScJ9Grht6oY9g7uGZA3xwywUuSTjI4QMnGGOcyWc8ts2oe1ubxAzYpYQyWG13G4emSDrYH0RSpur56N3M3iX_dgZ0DiKTvfBF86FArELg'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
              'value': '1970325044197427'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
              'value': 'a1137843'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
              'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1637560930, 'httpOnly': False,
                              'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                              'value': '1605703380,1605827816,1606024232,1606024930'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
              'value': 'direct'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
              'path': '/', 'secure': False, 'value': '1606024930'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
              'value': '0129991'},
             {'domain': '.qq.com', 'expiry': 1606111472, 'httpOnly': False, 'name': '_gid', 'path': '/',
              'secure': False, 'value': 'GA1.2.256861384.1606008688'},
             {'domain': 'work.weixin.qq.com', 'expiry': 1606041700, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
              'secure': False, 'value': '455sbep'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
              'value': 'xE04uJjGag0WTaZeNs-RvjDSVMJKH8smnAumPPkhGQIR_Xq_o2SKnp_tuUwrQFdu'},
             {'domain': '.work.weixin.qq.com', 'expiry': 1637239133, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
              'path': '/', 'secure': True, 'value': '0'},
             {'domain': '.qq.com', 'expiry': 1669097072, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
              'value': 'GA1.2.745212008.1605703362'},
             {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
              'value': '1688853469235889'},
             {'domain': '.work.weixin.qq.com', 'expiry': 1606039721, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
              'secure': True, 'value': '4tt3v1s'},
             {'domain': '.work.weixin.qq.com', 'expiry': 1608617072, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
              'path': '/', 'secure': False, 'value': 'zh'}]
        # shelve模块 python自带的对象持久化存储（也就算是一个数据库啦）
        # mac会生成一个文件.db，Windows会生成三个文件，读取方式都是一样的，不用太在意
        db = shelve.open('cookies')
        db['cookie'] = cookies
        db.close()

        # 此方法使用已存储在db中的cookie

    def test_cookiedb(self):
        db = shelve.open('cookies')
        # 找到数据之后存放在cookies中
        cookies = db['cookie']
        db.close()

        # 打开企业微信首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 加入cookie信息
        for cookie in cookies:
            # 因为expiry必须为整形，且在服务器端存储了一份，这个可以去掉
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 刷新页面
        self.driver.refresh()
        sleep(3)

    def test_import_contacts(self):
        db = shelve.open('cookies')
        # 找到数据之后存放在cookies中
        cookies = db['cookie']
        db.close()

        # 打开企业微信首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 加入cookie信息
        for cookie in cookies:
            # 因为expiry必须为整形，且在服务器端存储了一份，这个可以去掉
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 刷新页面
        self.driver.refresh()
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(2)').click()
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys(
            "E:/hogwarts_chw/test_webdriver/mydata.xlsx")
        result = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        assert "mydata.xlsx" == result
        sleep(3)
