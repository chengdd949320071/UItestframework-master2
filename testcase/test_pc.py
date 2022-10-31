#coding=utf-8
import time

from public.common import mytest, basepage
from public.common import mydate
from public.pages import PCtest
from public.common.log import Log
from time import sleep
from public.common import datainfo
from public.pages.PCtest import Actions


class Caitongchenjian(mytest.MyTest):
    logger = Log()
    def test_login(self):
        """在首页点击立即登录按钮，进入登录页"""
        pages = PCtest.Pages(self.dr)
        #进入首页页面
        pages.into_firstpage()
        #点击立即登录按钮，跳转登录页之后进行登录操作
        pages2 = PCtest.Actions(self.dr)
        login_name=pages2.clickljdu()
        self.logger.info('############################### 进入登录后用户名称的判断 ###############################')
        self.assertEquals(login_name, '您好，施倩倩', msg="登录后姓名应等变更")
        self.logger.info('############################### 登录后用户名称的判断 结束 ###############################')

    def test03_wallet_encash_fasts(self):
        """财鑫宝充值"""
        pages = PCtest.Pages(self.dr)
        # 进入首页页面
        pages.into_firstpage()
        # 点击立即登录按钮，跳转登录页之后进行登录操作
        pages2 = PCtest.Actions(self.dr)
        pages2.clickljdu()
        # 财鑫宝充值
        pages2.test03_wallet_encash_fast()

    def test04_wallet_encash_normals(self):
        """财鑫宝取现-普通取现"""

        pages = PCtest.Pages(self.dr)
        # 进入首页页面
        pages.into_firstpage()
        # 点击立即登录按钮，跳转登录页之后进行登录操作
        pages2 = PCtest.Actions(self.dr)
        pages2.clickljdu()
        # 财鑫宝取现-普通取现
        pages2.test04_wallet_encash_normal()

    def test05_productBuy_tonglians(self):
        """测试银行卡购买产品（中国银行）"""

        pages = PCtest.Pages(self.dr)
        # 进入首页页面
        pages.into_firstpage()
        # 点击立即登录按钮，跳转登录页之后进行登录操作
        pages2 = PCtest.Actions(self.dr)
        pages2.clickljdu()
        # 测试银行卡购买产品（中国银行）
        pages2.test05_productBuy_tonglian()

    def test06_productBuy_ICBCs(self):
        """测试银行卡购买产品（中国工商银行）"""
        pages = PCtest.Pages(self.dr)
        # 进入首页页面
        pages.into_firstpage()
        # 点击立即登录按钮，跳转登录页之后进行登录操作
        pages2 = PCtest.Actions(self.dr)
        pages2.clickljdu()
        # 测试银行卡购买产品（中国工商银行）
        pages2.test06_productBuy_ICBC()

    def test07_trade_redeem_toBanks(self):
        """测试pytest实现赎回-产品赎回到银行卡"""
        pages = PCtest.Pages(self.dr)
        # 进入首页页面
        pages.into_firstpage()
        # 点击立即登录按钮，跳转登录页之后进行登录操作
        pages2 = PCtest.Actions(self.dr)
        pages2.clickljdu()
        # 测试pytest实现赎回-产品赎回到银行卡
        pages2.test07_trade_redeem_toBank()

    def test08_trade_redeem_toWallets(self):
        """测试pytest实现赎回-产品赎回到财鑫宝"""

        pages = PCtest.Pages(self.dr)
        # 进入首页页面
        pages.into_firstpage()
        # 点击立即登录按钮，跳转登录页之后进行登录操作
        pages2 = PCtest.Actions(self.dr)
        pages2.clickljdu()
        # 测试pytest实现赎回-产品赎回到财鑫宝
        pages2.test08_trade_redeem_toWallet()

    def test09_trade_trans_in_outs(self):
        """测试pytest实现基金转换"""
        pages = PCtest.Pages(self.dr)
        # 进入首页页面
        pages.into_firstpage()
        # 点击立即登录按钮，跳转登录页之后进行登录操作
        pages2 = PCtest.Actions(self.dr)
        pages2.clickljdu()
        # 测试pytest实现基金转换
        pages2.test09_trade_trans_in_out()

    def append_funcs(self):
        """批量撤单"""
        pages = PCtest.Pages(self.dr)
        # 进入首页页面
        pages.into_firstpage()
        # 点击立即登录按钮，跳转登录页之后进行登录操作
        pages2 = PCtest.Actions(self.dr)
        pages2.clickljdu()
        memain_num = pages2.append_func()
        # 判断当前撤单按钮数量是否为0
        while memain_num > 0:
            self.append_funcs
            # pages.into_firstpage()
            # memain_num = pages2.append_func()
        self.logger.info('############################### 批量撤单 结束 ###############################')

    def test11_homepages(self):
        """测试首页热销产品的数据展示：产品名称、产品净值、净值日期，并校对净值日期是否为交易日的前一天"""
        pages = PCtest.Pages(self.dr)
        # 进入首页页面
        pages.into_firstpage()
        # 点击立即登录按钮，跳转登录页之后进行登录操作
        pages2 = PCtest.Actions(self.dr)
        pages2.clickljdu()
        aimday = pages2.test11_homepage()
        lastworkday = mydate.TimeUtil.getLastBusiness(self)
        self.assertEquals(lastworkday, aimday, msg="净值日期应为交易日的前一天")

    def test12_pruductpages(self):
        """测试产品中心-公募基金的数据展示：基金名称、基金代码、基金类型、风险等级、单位净值、累计净值、昨日增长率、近一周增长率、近一月增长率、近一年增长率,统计产品总数量"""
        pages = PCtest.Pages(self.dr)
        # 进入首页页面
        pages.into_firstpage()
        # 点击立即登录按钮，跳转登录页之后进行登录操作
        pages2 = PCtest.Actions(self.dr)
        pages2.clickljdu()
        pages2.test12_pruductpage()

    def test13_Walletpages(self):
        """测试财鑫宝页面，页面元素检查（财鑫宝名称、总金额、近七日年化、万份收益）"""
        pages = PCtest.Pages(self.dr)
        # 进入首页页面
        pages.into_firstpage()
        # 点击立即登录按钮，跳转登录页之后进行登录操作
        pages2 = PCtest.Actions(self.dr)
        pages2.clickljdu()
        pages2.test13_Walletpage()

    def test14_Mypage(self):
        """实现我的交易页面元素检查，展示我所持有的的产品，并统计总共有多少基金，总共有多少份额，总共昨日盈亏多少，累计盈亏多少，再匹配与基金总市值，昨日盈亏和累计盈亏是否一致"""
        pages = PCtest.Pages(self.dr)
        # 进入首页页面
        pages.into_firstpage()
        # 点击立即登录按钮，跳转登录页之后进行登录操作
        pages2 = PCtest.Actions(self.dr)
        login_name = pages2.clickljdu()
        # 实现我的交易页面元素检查，展示我所持有的的产品，并统计总共有多少基金，总共有多少份额，总共昨日盈亏多少，累计盈亏多少，再匹配与基金总市值，昨日盈亏和累计盈亏是否一致
        pages2.test14_Mypage()

    def test15_Information_notices(self):
        """测试信息公告有无更新"""
        pages = PCtest.Pages(self.dr)
        # 进入首页页面
        pages.into_firstpage()
        # 点击立即登录按钮，跳转登录页之后进行登录操作
        pages2 = PCtest.Actions(self.dr)
        pages2.clickljdu()
        # 测试信息公告有无更新
        pages2.test15_Information_notice()
        # aimday=  pages2.test15_Information_notice()
        # lastworkday = mydate.TimeUtil.getLastBusiness(self)
        # self.assertEquals(lastworkday, aimday, msg="66666")













