#coding=utf-8
import time
import random

from public.common import mytest, basepage
from public.common import mydate
from public.pages import APPtest
from public.common.log import Log
from time import sleep
from public.common import datainfo

class CaitongchenjianApp(mytest.MyTesth):
    logger = Log()
    # 首页收益日期，用于后面判断用

    def test01_login(self):
        """H5进入登录页，登录"""
        pages = APPtest.Pages(self.hdr)
        # 进入首页页面
        self.logger.info('############################### 进入首页页面 ###############################')
        # 点击立即登录按钮，跳转登录页之后进行登录操作
        pages.into_firstpage()
        pages2 = APPtest.Actions(self.hdr)
        datas = datainfo.get_xls_to_list('searKey.xlsx', 'Sheet1')
        account = random.choice(datas)
        pages2.mylogin(account)
        # 校验登录结果
        pages2.loginresult()
        self.logger.info('############################### 进入首页页面结束 ###############################')

    def test02_buyin(self):
        """H5买入产品005307"""
        pages = APPtest.Pages(self.hdr)
        # 进入首页页面
        pages.into_firstpage()
        pages2 = APPtest.Actions(self.hdr)
        # 登录
        datas = datainfo.get_xls_to_list('searKey.xlsx', 'Sheet1')
        account = random.choice(datas)
        pages2.mylogin(account)
        self.logger.info('############################### 进入买入操作 ###############################')
        # 点击顶部搜索框买入搜索基金
        pages2.buy_in()
        # 买入成功页面的元素获取判断
        test02buyinresult=pages2.buyinresult()
        self.logger.info('############################### 进入买入操作结束 ###############################')

    def test03_buyincash(self):
        """H5买入产品005307-线下汇款"""
        pages = APPtest.Pages(self.hdr)
        # 进入首页页面
        pages.into_firstpage()
        pages2 = APPtest.Actions(self.hdr)
        # 登录
        datas = datainfo.get_xls_to_list('searKey.xlsx', 'Sheet1')
        account = random.choice(datas)
        pages2.mylogin(account)
        self.logger.info('############################### 进入线下汇款操作 ###############################')
        # 点击顶部搜索框买入搜索基金
        pages2.buy_incash()
        self.logger.info('############################### 进入线下汇款操作结束 ###############################')

    def test04_walletcharge(self):
        """H5进入财鑫宝充值"""
        pages = APPtest.Pages(self.hdr)
        # 进入首页页面
        pages.into_firstpage()
        pages2 = APPtest.Actions(self.hdr)
        # 登录
        datas = datainfo.get_xls_to_list('searKey.xlsx', 'Sheet1')
        account = random.choice(datas)
        pages2.mylogin(account)
        self.logger.info('############################### 进入财鑫宝页面 ###############################')
        # 点击财鑫宝页面TAB进入财鑫宝页面
        pages.into_wallet()
        self.logger.info('############################### 点击财鑫宝页面充值按钮进入充值操作 ###############################')
        pages2.wallet_charge()
        self.logger.info('############################### 点击财鑫宝页面充值按钮进入充值结束 ###############################')

    def test05_walletencashnormals(self):
        """H5进入财鑫宝取现普通取现"""
        pages = APPtest.Pages(self.hdr)
        # 进入首页页面
        pages.into_firstpage()
        pages2 = APPtest.Actions(self.hdr)
        # 登录
        datas = datainfo.get_xls_to_list('searKey.xlsx', 'Sheet1')
        account = random.choice(datas)
        pages2.mylogin(account)
        self.logger.info('############################### 进入财鑫宝页面 ###############################')
        # 点击财鑫宝页面TAB进入财鑫宝页面
        pages.into_wallet()
        self.logger.info('############################### 点击财鑫宝页面取现按钮进入普通取现操作 ###############################')
        pages2.walletencashnormals()
        self.logger.info('############################### 点击财鑫宝页面取现按钮进入普通取现结束 ###############################')

    def test06_walletencashimmediates(self):
        """H5进入财鑫宝取现快速取现"""
        pages = APPtest.Pages(self.hdr)
        # 进入首页页面
        pages.into_firstpage()
        pages2 = APPtest.Actions(self.hdr)
        # 登录
        datas = datainfo.get_xls_to_list('searKey.xlsx', 'Sheet1')
        account = random.choice(datas)
        pages2.mylogin(account)
        self.logger.info('############################### 进入财鑫宝页面 ###############################')
        # 点击财鑫宝页面TAB进入财鑫宝页面
        pages.into_wallet()
        self.logger.info('############################### 点击财鑫宝页面取现按钮进入快速取现操作 ###############################')
        pages2.walletencashimmediates()
        self.logger.info('############################### 点击财鑫宝页面取现按钮进入快速取现结束 ###############################')

    def test07_traderedeemtoBank(self):
        """H5进入资产详情赎回到银行卡"""
        pages = APPtest.Pages(self.hdr)
        # 进入首页页面
        pages.into_firstpage()
        pages2 = APPtest.Actions(self.hdr)
        # 登录
        datas = datainfo.get_xls_to_list('searKey.xlsx', 'Sheet1')
        account = random.choice(datas)
        pages2.mylogin(account)
        self.logger.info('############################### 进入我的页面 ###############################')
        # 点击我的页面TAB进入我的页面
        pages.into_my()
        self.logger.info('############################### 在我的页面点进入我的资产页面 ###############################')
        # 点击我的页面TAB进入我的页面
        pages.into_my_products()
        self.logger.info('############################### 在我我的资产页面点击第一个持仓产品 ###############################')
        # 点击我的页面第一个产品详情
        pages.into_products_productdetail()
        # 进入资产详情点赎回/转换按钮
        pages.into_productdetail_redeem()
        self.logger.info('############################### 赎回到银行卡-开始 ###############################')
        pages2.traderedeemtoBank()
        self.logger.info('############################### 赎回到银行卡-结束 ###############################')

    def test08_traderedeemtoWallet(self):
        """H5进入资产详情赎回到财鑫宝"""
        pages = APPtest.Pages(self.hdr)
        # 进入首页页面
        pages.into_firstpage()
        pages2 = APPtest.Actions(self.hdr)
        # 登录
        datas = datainfo.get_xls_to_list('searKey.xlsx', 'Sheet1')
        account = random.choice(datas)
        pages2.mylogin(account)
        self.logger.info('############################### 进入我的页面 ###############################')
        # 点击我的页面TAB进入我的页面
        pages.into_my()
        self.logger.info('############################### 在我的页面点进入我的资产页面 ###############################')
        # 点击我的页面TAB进入我的页面
        pages.into_my_products()
        self.logger.info('############################### 在我我的资产页面点击第一个持仓产品 ###############################')
        # 点击我的页面第一个产品详情
        pages.into_products_productdetail()
        # 进入资产详情点赎回/转换按钮
        pages.into_productdetail_redeem()
        self.logger.info('############################### 赎回到财鑫宝-开始 ###############################')
        pages2.traderedeemtowallet()
        self.logger.info('############################### 赎回到财鑫宝-结束 ###############################')

    def test09_tradetransinout(self):
        """H5进入资产详情进行转换操作"""
        pages = APPtest.Pages(self.hdr)
        # 进入首页页面
        pages.into_firstpage()
        pages2 = APPtest.Actions(self.hdr)
        # 登录
        datas = datainfo.get_xls_to_list('searKey.xlsx', 'Sheet1')
        account = random.choice(datas)
        pages2.mylogin(account)
        self.logger.info('############################### 进入我的页面 ###############################')
        # 点击我的页面TAB进入我的页面
        pages.into_my()
        self.logger.info('############################### 在我的页面点进入我的资产页面 ###############################')
        # 点击我的页面TAB进入我的页面
        pages.into_my_products()
        self.logger.info('############################### 在我我的资产页面点击第一个持仓产品 ###############################')
        # 点击我的页面第一个产品详情
        pages.into_products_productdetail()
        # 进入资产详情点赎回/转换按钮
        pages.into_productdetail_redeem()
        self.logger.info('############################### 进入转换页面-转换开始 ###############################')
        pages2.tradetransinout()
        self.logger.info('############################### 进入转换页面-转换结束 ###############################')