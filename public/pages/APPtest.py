#coding=utf-8
import pytest
from public.common import mytest
from public.common import basepage,mydate
from public.common.log import Log
from time import sleep, time

project_path = 'C:\\Users\\Administrator\\PycharmProjects\\UItestframework-master\\report\\picture'
class Pages(basepage.Page):

    def into_firstpage(self):
        """打开H5现行版登录首页"""
        self.dr.open('https://www.ctzg.com/hy5/#/home')
        sleep(5)
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[1]/div[1]/div[2]/div[2]')


    def into_wallet(self):
        """点财鑫宝TAB"""
        self.dr.click('css->#app > div > div > div > div.van-tabbar.van-tabbar--fixed.van-hairline--top-bottom.van-safe-area-bottom > div:nth-child(3) > div.van-tabbar-item__text')
        sleep(5)

    def into_my(self):
        """我的页面TAB"""
        self.dr.click('css->#app > div > div > div > div.van-tabbar.van-tabbar--fixed.van-hairline--top-bottom.van-safe-area-bottom > div:nth-child(4)')
        sleep(5)

    def into_my_products(self):
        """我的页面TAB-点我的资产"""
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[1]/div[3]/div[1]')
        sleep(5)

    def into_products_productdetail(self):
        """我的资产页面-点第一个我的持仓"""
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[3]/div[2]/div[1]')
        sleep(5)

    def into_productdetail_redeem(self):
        """我的持仓页面-点赎回/取现"""
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[3]/div/div[1]/div')
        sleep(5)

class Actions(basepage.Page):
    def mylogin(self):
        """登录"""
        self.dr.take_screenshot(project_path + '\\1-login.png')
        self.dr.type('xpath->//*[@id="van-field-2-input"]', '15158171649')
        sleep(3)
        self.dr.type('xpath->//*[@id="van-field-4-input"]', 'Qwer123456')
        sleep(3)
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[2]/div[1]/div/div/i')
        sleep(3)
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[2]/div[2]/div[1]/button')
        sleep(5)
        self.dr.take_screenshot(project_path + '\\2-firstpage.png')

    def buy_in(self):
        """现行版选择产品买入"""
        # 点顶部搜索框
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[1]/div[1]/div[1]/div/div')
        sleep(3)
        # 选择第二个产品买入，当前是鸿福短债007915
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[2]/div/div[2]/div[2]')
        sleep(5)
        # 点击买入按钮
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[6]/div[2]/div[2]/div[2]/button')
        # 买入页买个10000
        self.dr.type('xpath->//*[@id="app"]/div/div/div/div[3]/div[3]/div[2]/input', '1')
        sleep(1)
        # 选中协议签署
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[6]/img')
        # 点确认按钮
        sleep(2)
        self.dr.click('xpath->//*[@id="app"]/div/div/div[1]/div[7]/div/div/button')
        sleep(15)
        # 点我知道了按钮
        self.dr.click('xpath->//*[@id="app"]/div/div/div[3]/div/div[3]/div/div/button')
        sleep(5)
        self.input_tradepassword()
        sleep(5)
        self.dr.quit()

    def buy_incash(self):
        """现行版选择产品买入-线下汇款"""
        # 点顶部搜索框
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[1]/div[1]/div[1]/div/div')
        sleep(3)
        # 选择第二个产品买入，当前是鸿福短债007915
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[2]/div/div[2]/div[2]')
        sleep(5)
        # 点击买入按钮
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[6]/div[2]/div[2]/div[2]/button')
        sleep(3)
        # 点击线下汇款TAB
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[2]/div[2]')
        # 买入页买个100000
        self.dr.type('xpath->//*[@id="app"]/div/div/div/div[3]/div[3]/div[2]/input', '200000')
        sleep(1)
        # 选中协议签署
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[6]/img')
        # 点确认按钮
        sleep(2)
        self.dr.click('xpath->//*[@id="app"]/div/div/div[1]/div[7]/div/div/button')
        sleep(15)
        # 点我知道了按钮
        self.dr.click('xpath->//*[@id="app"]/div/div/div[3]/div/div[3]/div/div/button')
        sleep(5)
        self.input_tradepassword()
        sleep(5)
        self.dr.quit()

    def wallet_charge(self):
        """首页登录后点财鑫宝充值按钮"""
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[1]/div[2]/div[5]/div[2]')
        sleep(5)
        # 输入金额
        self.dr.type('xpath->//*[@id="app"]/div/div/div/div[2]/div[3]/div[2]/input','1')
        sleep(1)
        # 选中协议签署
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[3]/img')
        sleep(2)
        # 点确定转入按钮
        self.dr.click('css->#app > div > div > div.page-wrapper.padding.bottom-fixed-padding > div.van-config-provider > div > div > button')
        sleep(5)
        self.input_wallettradepassword()
        sleep(5)
        self.dr.quit()

    def walletencashnormals(self):
        """首页登录后点财鑫宝取现按钮-普通取现"""
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[1]/div[2]/div[5]/div[1]')
        sleep(5)
        # 输入金额
        self.dr.type('xpath->//*[@id="app"]/div/div/div/div[2]/div[3]/div[2]/input','1')
        sleep(1)
        # 选中普通取现的框
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[3]/div[2]/div[2]/div[1]/div/i')
        sleep(2)
        # 点确定转出按钮
        self.dr.click('css->#app > div > div > div > div.van-config-provider > div > div > button')
        sleep(5)
        self.input_wallettradepassword()
        sleep(5)
        self.dr.quit()

    def walletencashimmediates(self):
        """首页登录后点财鑫宝取现按钮-快速取现"""
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[1]/div[2]/div[5]/div[1]')
        sleep(5)
        # 输入金额
        self.dr.type('xpath->//*[@id="app"]/div/div/div/div[2]/div[3]/div[2]/input','1')
        sleep(1)
        # 选中普通取现框不变点击签署协议
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[4]/img')
        sleep(2)
        # 点确定转出按钮
        self.dr.click('css->#app > div > div > div > div.van-config-provider > div > div > button')
        sleep(5)
        self.input_wallettradepassword()
        sleep(5)
        self.dr.quit()

    def traderedeemtoBank(self):
        """赎回页面-赎回到银行卡"""
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/i')
        sleep(5)
        # 输入份额 1份
        self.dr.type('xpath->//*[@id="app"]/div/div/div/div[2]/div[3]/div[3]/div/input','1')
        sleep(1)
        # 点击确认按钮
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[2]/div[6]/div[2]/button')
        sleep(2)
        self.input_redeemtradepassword()
        sleep(5)
        self.dr.quit()

    def traderedeemtowallet(self):
        """赎回页面-赎回到财鑫宝"""
        # 输入份额 1份
        self.dr.type('xpath->//*[@id="app"]/div/div/div/div[2]/div[3]/div[3]/div/input','1')
        sleep(1)
        # 点击确认按钮
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[2]/div[6]/div[2]/button')
        sleep(2)
        self.input_redeemtradepassword()
        sleep(5)
        self.dr.quit()

    def tradetransinout(self):
        """点击转换页面TAB-转换操作"""
        # 点击转换TAB
        self.dr.click('xpath->/html/body/div/div/div/div/div[1]/div[1]/div/div[2]')
        sleep(2)
        # 点击选择转入的基金，拉出弹窗
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[2]/div[1]/div[4]/div[2]')
        sleep(5)
        # 点选第一支基金作为转入基金
        #self.dr.click('xpath->/html/body/div[8]/div/div[2]/div[1]/ul/li[1]/div')
        #sleep(1)
        # 点弹窗上的确认
        self.dr.click('xpath->/html/body/div[3]/div/div[1]/button[2]')
        sleep(5)
        # 输入份额 1份
        self.dr.type('xpath->/html/body/div[1]/div/div/div/div[2]/div[2]/div[3]/div[1]/input','1')
        sleep(1)
        #点击签署协议
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[2]/div[5]/img')
        # 点击确认按钮
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[2]/div[7]/div/div/button')
        sleep(15)
        # 点我知道了按钮
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[4]/div/div[3]/div/div/button')
        sleep(2)
        self.input_transtradepassword()
        sleep(5)
        self.dr.quit()

    def input_transtradepassword(self):
        """输入交易密码"""
        # 输入密码1
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[6]/div/div[2]/div[3]/div/div/div[1]/div')
        sleep(2)
        # 输入密码2
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[6]/div/div[2]/div[3]/div/div/div[2]/div')
        sleep(2)
        # 输入密码3
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[6]/div/div[2]/div[3]/div/div/div[3]/div')
        sleep(2)
        # 输入密码1
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[6]/div/div[2]/div[3]/div/div/div[1]/div')
        sleep(2)
        # 输入密码2
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[6]/div/div[2]/div[3]/div/div/div[2]/div')
        sleep(2)
        # 输入密码3
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[6]/div/div[2]/div[3]/div/div/div[3]/div')
        sleep(2)

    def input_tradepassword(self):
        """输入交易密码"""
        # 输入密码1
        self.dr.click('xpath->//*[@id="app"]/div/div/div[5]/div/div[2]/div[3]/div/div/div[1]/div')
        sleep(2)
        # 输入密码2
        self.dr.click('xpath->//*[@id="app"]/div/div/div[5]/div/div[2]/div[3]/div/div/div[2]/div')
        sleep(2)
        # 输入密码3
        self.dr.click('xpath->//*[@id="app"]/div/div/div[5]/div/div[2]/div[3]/div/div/div[3]/div')
        sleep(2)
        # 输入密码1
        self.dr.click('xpath->//*[@id="app"]/div/div/div[5]/div/div[2]/div[3]/div/div/div[1]/div')
        sleep(2)
        # 输入密码2
        self.dr.click('xpath->//*[@id="app"]/div/div/div[5]/div/div[2]/div[3]/div/div/div[2]/div')
        sleep(2)
        # 输入密码3
        self.dr.click('xpath->//*[@id="app"]/div/div/div[5]/div/div[2]/div[3]/div/div/div[3]/div')
        sleep(2)

    def input_redeemtradepassword(self):
        """输入赎回用交易密码"""
        # 输入密码1
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[4]/div/div[2]/div[3]/div/div/div[1]/div')
        sleep(2)
        # 输入密码2
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[4]/div/div[2]/div[3]/div/div/div[2]/div')
        sleep(2)
        # 输入密码3
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[4]/div/div[2]/div[3]/div/div/div[3]/div')
        sleep(2)
        # 输入密码1
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[4]/div/div[2]/div[3]/div/div/div[1]/div')
        sleep(2)
        # 输入密码2
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[4]/div/div[2]/div[3]/div/div/div[2]/div')
        sleep(2)
        # 输入密码3
        self.dr.click('xpath->//*[@id="app"]/div/div/div/div[4]/div/div[2]/div[3]/div/div/div[3]/div')
        sleep(2)

    def input_wallettradepassword(self):
        """输入财鑫宝交易密码"""
        # 输入密码1
        self.dr.click('xpath->//*[@id="app"]/div/div/div[3]/div/div[2]/div[3]/div/div/div[1]/div')
        sleep(2)
        # 输入密码2
        self.dr.click('xpath->//*[@id="app"]/div/div/div[3]/div/div[2]/div[3]/div/div/div[2]/div')
        sleep(2)
        # 输入密码3
        self.dr.click('xpath->//*[@id="app"]/div/div/div[3]/div/div[2]/div[3]/div/div/div[3]/div')
        sleep(2)
        # 输入密码1
        self.dr.click('xpath->//*[@id="app"]/div/div/div[3]/div/div[2]/div[3]/div/div/div[1]/div')
        sleep(2)
        # 输入密码2
        self.dr.click('xpath->//*[@id="app"]/div/div/div[3]/div/div[2]/div[3]/div/div/div[2]/div')
        sleep(2)
        # 输入密码3
        self.dr.click('xpath->//*[@id="app"]/div/div/div[3]/div/div[2]/div[3]/div/div/div[3]/div')
        sleep(2)

class Checkies (basepage.Page):
    def loginresult(self):
        self.dr.click('xpath->//*[@id="app"]/div/div/div[3]/div/div[2]/div[3]/div/div/div[1]/div')