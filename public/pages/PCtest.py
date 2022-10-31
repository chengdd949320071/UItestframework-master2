#coding=utf-8
import pytest
from public.common import mytest
from public.common import basepage,mydate
from public.common.log import Log
from time import sleep

class Pages(basepage.Page):

    def into_firstpage(self):
        """打开PC端首页"""
        self.dr.open('https://www.ctzg.com/index.html')
        self.dr.wait(10)

    def into_productpage(self):
        """打开PC端产品中心页"""
        self.dr.open('https://www.ctzg.com/website/#/productcenter')
        self.dr.wait(10)

    def into_cxbpage(self):
        """打开PC端财鑫宝页"""
        self.dr.open('https://www.ctzg.com/website/#/wallet')
        self.dr.wait(10)

    def into_accountpage(self):
        """打开PC端我的交易页"""
        self.dr.open('https://www.ctzg.com/website/#/tradecenter/accountpage')
        self.dr.wait(10)

    def into_xzzqpage(self):
        """打开PC端客户服务页"""
        self.dr.open('https://www.ctzg.com/html/xzzq/')
        self.dr.wait(10)

    def into_gsdtpage(self):
        """打开PC端信息公告页"""
        self.dr.open('https://www.ctzg.com/html/gsdt/')
        self.dr.wait(10)

    def into_accountpage(self):
        """打开PC端关于我们页"""
        self.dr.open('https://www.ctzg.com/html/gsjj/')
        self.dr.wait(10)

class Actions(basepage.Page):
    logger = Log()

    @pytest.fixture(scope='function')
    def setup_function(request):
        def teardown_function():
            print("teardown_function called")

        request.addfinalizer(teardown_function)
        print('setup_function called')

    @pytest.fixture(scope='module')
    def setup_module(request):
        def teardown_module():
            print("teardown_module called.")

        request.addfinalizer(teardown_module)
        print('setup_module called.')

    def append_func(self):
        # 进入撤单页面，获取撤单按钮
        self.dr.click('link_text->我的交易')
        sleep(3)
        self.dr.click('css->#app > div > div.maincontent > div.sidenav > div.navlist > div:nth-child(3) > ul > li:nth-child(3)')
        sleep(5)
        # 统计撤单按钮数量
        withdraw_button = self.dr.find_elements('class->append')
        pro_num = len(withdraw_button)
        pro_num2 = len(withdraw_button)
        pro_num = str(pro_num)
        result = '############################ 您总共可撤单数为:' + pro_num + '个############################ '
        self.logger.info(result)
        # 点击第一个
        withdraw_button[0].click()
        sleep(3)
        # 输入撤单交易密码
        # search_input = None
        try:
            self.dr.type('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(7) > form > div:nth-child(2) > div > div > input','1')
        except:
            self.dr.type('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(6) > form > div:nth-child(2) > div > div > input','1')
        self.dr.type('css->#password','23123')
        sleep(2)
        # 点击撤单按钮
        self.dr.click('xpath->//*[@id=\'app\']/div/div[3]/div[2]/div/div[2]/div[2]/div/div[2]')
        sleep(2)
        remain_num = pro_num2 - 1
        return remain_num


    def clickljdu(self):
        """点击立即登录按钮，进入登陆页"""
        self.dr.click('xpath->/html/body/div[4]/div[2]/div[2]/p[1]/span')
        sleep(10)
        """在登录页录入账户信息"""
        self.dr.type('css->div.loginbox div.banner form.el-form.demo-ruleForm div.el-form-item.is-required:nth-child(2) div.el-form-item__content div.el-input > input.el-input__inner','18811383797')
        sleep(2)
        """"在登录页录入密码第一位"""
        self.dr.type('css->div.loginbox div.banner form.el-form.demo-ruleForm div.el-form-item.is-required:nth-child(4) div.el-form-item__content div.el-input > input.el-input__inner','Q')
        """"在登录页录入密码其他位"""
        self.dr.type('css->#password','wer123456')
        """"在登录页点击登录按钮"""
        self.dr.click('xpath->//body[1]/div[1]/div[1]/div[2]/form[1]/div[5]/div[1]/button[1]/span[1]')
        sleep(5)
        """"点击弹窗的"""
        self.dr.click('css->#app > div > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary > span')
        sleep(2)
        """"获取登录名"""
        login_name = self.dr.get_text('css->#custinfo > li:nth-child(1) > a')
        return login_name
    # 财鑫宝充值
    def test02_wallet_charge(self):
        """财鑫宝充值"""
        self.logger.info('############################### 财鑫宝充值开始 ###############################')
        self.dr.click('link_text->财鑫宝')
        sleep(5)
        self.dr.click('xpath->//*[@id=\"app\"]/div/div[4]/div[2]/div[2]/div[3]/div[1]')
        sleep(3)
        self.dr.type('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > form > div:nth-child(1) > div > div > input','1')
        sleep(1)
        self.dr.type('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > form > div:nth-child(3) > div > div > input','1')
        self.dr.type('css->#password','23123')
        sleep(1)
        self.dr.click('xpath->//*[@id=\'app\']/div/div[3]/div[2]/div/div[2]/div[1]/form/div[4]/div/label/span/span')
        sleep(1)
        self.dr.click('xpath->//*[@id=\'app\']/div/div[3]/div[2]/div/div[2]/div[2]/div/div[2]')
        trade_result = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div > div.block2 > p.fonttips_tit')
        trade_balance = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div > div.block2 > div:nth-child(2) > span > span')
        trade_product = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div > div.block2 > div:nth-child(3)')
        trade_product =trade_product[6:]
        trade_status = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div > div.block2 > p.bankErrMsg')
        result='您好，您的'+trade_product+'，存入金额：'+trade_balance+'元，'+trade_result+'!'+trade_status
        self.logger.info(result)
        self.logger.info('############################### 财鑫宝充值结束 ###############################')
        sleep(3)

    # 财鑫宝取现-快速取现:
    def test03_wallet_encash_fast(self):
        self.logger.info('############################### 财鑫宝取现-快速取现开始 ###############################')
        self.dr.click('link_text->财鑫宝')
        self.dr.click('css->#app > div > div.block.block1 > div.content > div.wallet > div.btnbox > div.takecash')
        sleep(3)
        self.dr.type('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > form > div:nth-child(1) > div > div > input','0.01')
        sleep(1)
        self.dr.type('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > form > div:nth-child(3) > div > div > input','1')
        self.dr.type('css->#password','23123')
        sleep(1)
        self.dr.click('xpath->//*[@id=\'app\']/div/div[3]/div[2]/div/div[2]/div[1]/form/div[4]/div/label/span/span')
        sleep(1)
        self.dr.click('xpath->//*[@id=\'app\']/div/div[3]/div[2]/div/div[2]/div[2]/div/div[2]')
        trade_result = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div > div.block2 > p')
        trade_balance = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div > div.block2 > div:nth-child(2) > span > span')
        trade_product = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div > div.block2 > div:nth-child(3)')
        trade_product = trade_product[6:]
        result = '您好，您的' + trade_product + '，快速取现金额：' + trade_balance + '元，' + trade_result + '!'
        self.logger.info(result)
        self.logger.info('############################### 财鑫宝取现-快速取现结束 ###############################')
        sleep(3)

    # 财鑫宝取现-普通取现:
    def test04_wallet_encash_normal(self):
        self.logger.info('############################### 财鑫宝取现-普通取现开始 ###############################')
        sleep(2)
        self.dr.click('link_text->财鑫宝')
        self.dr.click('css->#app > div > div.block.block1 > div.content > div.wallet > div.btnbox > div.takecash')
        sleep(3)
        self.dr.click('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div.radiobox2 > div:nth-child(2) > div:nth-child(1) > div')
        self.dr.type('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > form > div:nth-child(1) > div > div > input','0.01')
        sleep(1)
        # 输入一个数字以后，触发了控件的事件，修改了dom，导致原来find能找到的输入框，找不到了,so要先输入一个，再看这个输入框的css_selector
        # 开发加了一个函数，输入的时候加了一个校验函数，在前面动态增加了一个标签，导致这个输入的标签就后移了
        self.dr.type('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > form > div:nth-child(3) > div > div > input','1')
        self.dr.type('css->#password','23123')
        sleep(1)
        self.dr.click('xpath->//*[@id=\'app\']/div/div[3]/div[2]/div/div[2]/div[2]/div/div[2]')
        trade_result = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div > div.block2 > p')
        trade_balance = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div > div.block2 > div:nth-child(2) > span > span')
        trade_product = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div > div.block2 > div:nth-child(3)')
        trade_product = trade_product[6:]
        result = '您好，您的' + trade_product + '，普通取现金额：' + trade_balance + '元，' + trade_result + '!'
        self.logger.info(result)
        self.logger.info('############################### 财鑫宝取现-普通取现结束 ###############################')
        sleep(3)

    # 测试银行卡购买产品（中国银行）
    def test05_productBuy_tonglian(self):
        self.logger.info('############################### 测试银行卡购买产品（中国银行）开始 ###############################')
        self.dr.click('link_text->我的交易')
        sleep(1)
        self.dr.click('css->#app > div > div.maincontent > div.sidenav > div.navlist > div:nth-child(3) > ul > li:nth-child(1)')
        sleep(2)
        self.dr.click('css->#app > div > div.maincontent > div.mainright > div > div:nth-child(4) > div.tablebox > ul.fadeIn.animated.delay-1 > li.last > span.append')
        sleep(3)
        #购买金额
        self.dr.type('css->#applyboxid > div.block2 > div > form > div:nth-child(1) > div > div.el-input > input','1000')
        sleep(1)
        self.dr.type('css->#applyboxid > div.block2 > div > form > div:nth-child(3) > div > div > input','1')
        self.dr.type('css->#password','23123')
        sleep(1)
        self.dr.click('xpath->//*[@id=\'box1\']')
        sleep(1)
        self.dr.click('xpath->//*[@id=\'applyboxid\']/div[2]/div/div[4]/div/div[2]')
        sleep(11)
        self.dr.click('css->#applyboxid > div:nth-child(5) > div > div > div.btnWrapper.flex-h > div')
        sleep(2)
        # self.dr.click('css->#applyboxid > div.block2 > div > div:nth-child(6) > div > div.el-dialog__footer > div > button.el-button.el-button--primary > span')
        sleep(8)
        trade_result = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.boxcontent > div.imgbox > p.fonttips_tit2')
        trade_status = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.boxcontent > div.imgbox > p.fonttime.fonttips_tit')
        result = trade_result + trade_status +'!'
        self.logger.info(result)
        self.logger.info('############################### 测试银行卡购买产品（中国银行）结束 ###############################')
        sleep(3)

    # 测试银行卡购买产品（中国工商银行）
    def test06_productBuy_ICBC(self):
        self.logger.info('############################### 测试银行卡购买产品（中国工商银行）开始 ###############################')
        self.dr.click('link_text->我的交易')
        sleep(1)
        self.dr.click('css->#app > div > div.maincontent > div.sidenav > div.navlist > div:nth-child(3) > ul > li:nth-child(1)')
        sleep(2)
        self.dr.click('css->#app > div > div.maincontent > div.mainright > div > div:nth-child(4) > div.tablebox > ul.fadeIn.animated.delay-1 > li.last > span.append')
        sleep(3)
        self.dr.click('css->#applyboxid > div.block2 > div > div.payments > div:nth-child(2) > div:nth-child(3) > div')
        sleep(2)
        self.dr.type('css->#applyboxid > div.block2 > div > form > div:nth-child(1) > div > div.el-input > input','1000')
        sleep(2)
        self.dr.type('css->#applyboxid > div.block2 > div > form > div:nth-child(3) > div > div > input','1')
        self.dr.type('css->#password','23123')
        sleep(1)
        self.dr.click('xpath->//*[@id=\'box1\']')
        sleep(1)
        self.dr.click('xpath->//*[@id=\'applyboxid\']/div[2]/div/div[4]/div/div[2]')
        sleep(11)
        self.dr.click('css->#applyboxid > div:nth-child(5) > div > div > div.btnWrapper.flex-h > div')
        sleep(2)
        # self.dr.click('css->#applyboxid > div.block2 > div > div:nth-child(6) > div > div.el-dialog__footer > div > button.el-button.el-button--primary > span')
        sleep(8)
        trade_result = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.boxcontent > div.imgbox > p.fonttips_tit2')
        trade_status = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.boxcontent > div.imgbox > p.fonttime.fonttips_tit')
        result = trade_result + trade_status + '!'
        self.logger.info(result)
        self.logger.info('############################### 测试银行卡购买产品（中国工商银行）结束 ###############################')
        sleep(3)

    # 测试pytest实现赎回-产品赎回到银行卡
    def test07_trade_redeem_toBank(self):
        self.logger.info('############################### 测试pytest实现赎回-产品赎回到银行卡开始 ###############################')
        self.dr.click('link_text->我的交易')
        self.dr.click('css->#app > div > div.maincontent > div.sidenav > div.navlist > div:nth-child(3) > ul > li:nth-child(2)')
        self.dr.click('css->#app > div > div.maincontent > div.sidenav > div.navlist > div:nth-child(3) > ul > li:nth-child(2)')
        sleep(5)
        redeem_click = self.dr.find_elements('class->withdraw')
        pro_num = len(redeem_click)
        pro_num= str(pro_num)
        result = '############################ 您总共可赎回产品总数为:' + pro_num + '个############################ '
        self.logger.info(result)
        sleep(2)
        # Selenium点击三种方式
        # 方法1：直接调用click()--》a.click()
        # 方法2：调用execute_script()--》self.dr.dojs("arguments[0].click();",a)
        # 方法3：调用webdriver控制--》webdriver.ActionChains(driver).move_to_element(a).click(a).perform()
        element = redeem_click[0]
        self.dr.dojs("arguments[0].click();",element)
        sleep(2)
        self.dr.type('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > form > div:nth-child(3) > div > div > input','0.1')
        sleep(2)
        self.dr.type('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > form > div:nth-child(5) > div > div > input','1')
        self.dr.type('css->#password','23123')
        sleep(1)
        self.dr.click('xpath->//div[contains(text(),\'确定\')]')
        sleep(2)
        trade_result = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > h2')
        trade_proName = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(1) > div.right')
        trade_businflag = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(2) > div.right')
        trade_requestNo = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(3) > div.right')
        trade_time = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(5) > div.right')
        trade_date = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(6) > div.right')
        result2 = '## 您好，您的' + trade_result + '，赎回的产品名称为：'+ trade_proName + '，业务类型为：'+ trade_businflag + '，申请编号为：'+ trade_requestNo + '，申请日期为：'+ trade_date + '，下单时间为：'+ trade_time + '#######'
        self.logger.info(result2)
        sleep(3)
        self.logger.info('############################### 测试pytest实现赎回-产品赎回到银行卡结束 ###############################')
    # 测试pytest实现赎回-产品赎回到财鑫宝
    def test08_trade_redeem_toWallet(self):
        self.logger.info('############################### 测试pytest实现赎回-产品赎回到财鑫宝开始 ###############################')
        self.dr.click('link_text->我的交易')
        self.dr.click('css->#app > div > div.maincontent > div.sidenav > div.navlist > div:nth-child(3) > ul > li:nth-child(2)')
        self.dr.click('css->#app > div > div.maincontent > div.sidenav > div.navlist > div:nth-child(3) > ul > li:nth-child(2)')
        sleep(5)
        redeem_click = self.dr.find_elements('class->withdraw')
        pro_num = len(redeem_click)
        pro_num = str(pro_num)
        result = '############################ 您总共可赎回产品总数为:' + pro_num + '个############################ '
        self.logger.info(result)
        # print(redeem_click[0].text)
        sleep(2)
        # Selenium点击三种方式
        # 方法1：直接调用click()--》a.click()
        # 方法2：调用execute_script()--》self.dr.dojs("arguments[0].click();",a)
        # 方法3：调用webdriver控制--》webdriver.ActionChains(driver).move_to_element(a).click(a).perform()
        element = redeem_click[0]
        self.dr.dojs("arguments[0].click();",element)
        sleep(2)
        # redemption2
        self.dr.click('css->#redemption2')
        sleep(1)
        self.dr.type('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > form > div:nth-child(3) > div > div > input','1')
        sleep(2)
        self.dr.type('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > form > div:nth-child(5) > div > div > input','1')
        self.dr.type('css->#password','23123')
        sleep(1)
        self.dr.click('xpath->//div[contains(text(),\'确定\')]')
        sleep(2)
        trade_result = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > h2')
        trade_proName = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(1) > div.right')
        trade_businflag = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(2) > div.right')
        trade_shares = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(3) > div.right.fundsday')
        trade_requestNo = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(4) > div.right')
        trade_time = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(6) > div.right')
        trade_date = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(7) > div.right')
        result2 = '## 您好，您的' + trade_result + '，赎回的产品名称为：' + trade_proName + '，业务类型为：' + trade_businflag + '申请份额为：'+ trade_shares+'，申请编号为：' + trade_requestNo + '，申请日期为：' + trade_date + '，下单时间为：' + trade_time + '#######'
        self.logger.info(result2)
        sleep(3)
        self.logger.info('############################### 测试pytest实现赎回-产品赎回到财鑫宝结束 ###############################')

    # 测试pytest实现基金转换
    def test09_trade_trans_in_out(self):
        self.logger.info('############################### 测试pytest实现基金转换开始 ###############################')
        self.dr.click('link_text->我的交易')
        sleep(1)
        self.dr.click('css->#app > div > div.maincontent > div.sidenav > div.navlist > div:nth-child(3) > ul > li:nth-child(5)')
        sleep(5)
        trans_click = self.dr.find_elements('class->picked')
        pro_num = len(trans_click)
        pro_num = str(pro_num)
        result = '############################ 您总共可转换的产品总数为:' + pro_num + '个############################ '
        self.logger.info(result)
        sleep(2)
        # 选择第4只转出产品
        element = trans_click[3]
        self.dr.dojs("arguments[0].click();",element)
        sleep(2)
        self.dr.click('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div > form > div:nth-child(3) > div > div > div > input')
        sleep(1)
        # 弹出的弹框列表选择其中一个产品进行转入
        # trans_in = self.dr('class->el-select-dropdown__item')
        trans_in_click = self.dr.find_elements('class->el-select-dropdown__item')
        pro_num = len(trans_in_click)
        pro_num = str(pro_num)
        result = '############################ 您总共可转入的产品总数为:' + pro_num + '个############################ '
        self.logger.info(result)
        sleep(2)
        # 选择第4只转入产品
        element = trans_in_click[3]
        self.dr.dojs("arguments[0].click();",element)
        sleep(2)
        self.dr.type('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div > form > div:nth-child(4) > div > div > input','1')
        sleep(1)
        self.dr.type('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div > form > div:nth-child(6) > div > div > input','1')
        self.dr.type('css->#password','23123')
        sleep(1)
        self.dr.click('css->#box1')
        self.dr.click('xpath->//div[contains(text(),\'确定\')]')
        sleep(11)
        self.dr.click('css->#app > div > div.maincontent > div.mainright > div > div:nth-child(5) > div > div > div.btnWrapper.flex-h > div')
        sleep(1)
        # self.dr.click('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div > div.el-dialog__wrapper > div > div.el-dialog__footer > div > button.el-button.el-button--primary > span')
        sleep(2)
        trans_result = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > h2')
        trans_out = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(1) > div.right')
        trans_in = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(2) > div.right')
        trans_businflag = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(3) > div.right')
        trans_shares = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(4) > div.right')
        trans_requestNo = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(5) > div.right')
        trans_bank = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(6) > div.right')
        trans_time = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(7) > div.right')
        trans_date = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.block2 > div.form > div:nth-child(8) > div.right')
        sleep(3)
        self.logger.info('基金转换交易结果详情如下：')
        result2 = '## 您好，您的' + trans_result + '，转出产品为：' + trans_out + '，转入产品为：'+ trans_in +'，业务类型为：' + trans_businflag + '申请份额为：' + trans_shares + '，申请编号为：' + trans_requestNo + '，申请日期为：' + trans_date + '，下单时间为：' + trans_time + '，银行账户为：'+trans_bank+'#######'
        self.logger.info(result2)
        self.logger.info('############################### 测试pytest实现基金转换结束 ###############################')

    def test10_trade_withdraw(self):
        self.append_func()


    # 测试首页热销产品的数据展示：产品名称、产品净值、净值日期，并校对净值日期是否为交易日的前一天
    def test11_homepage(self):
        self.logger.info('####测试首页热销产品的数据展示：产品名称、产品净值、净值日期，并校对净值日期是否为交易日的前一天开始 ######')
        self.dr.click('link_text->首页')
        product_Name = self.dr.find_elements('xpath->//*[@id=\'newyearBox\']/div[1]/ul/li/a/div/p[1]')
        nav_num = self.dr.find_elements('xpath->//*[@id=\'newyearBox\']/div[1]/ul/li/a/div/p[3]')
        nav_Date = self.dr.find_elements('xpath->//*[@id=\'newyearBox\']/div[1]/ul/li/a/div/p[2]')
        print('\n')
        for i in range(len(product_Name)):
            result2 ='#######' + product_Name[i].text + '， 单位净值：' + nav_num[i].text + '  净值日期：' + nav_Date[i].text[5:15] + '#######'
            self.logger.info(result2)
        aimday=nav_Date[0].text[5:15]
        return  aimday


    # 测试产品中心-公募基金的数据展示：基金名称、基金代码、基金类型、风险等级、单位净值、累计净值、昨日增长率、近一周增长率、近一月增长率、近一年增长率,统计产品总数量
    def test12_pruductpage(self):
        sleep(3)
        self.dr.click('css->body > div.navbox > nav > ul > li:nth-child(2) > a')
        sleep(3)
        self.dr.click('css->#activeli > li:nth-child(3)')
        self.dr.wait(10)
        product_Name_02 = self.dr.find_elements('xpath->//*[@id=\'fund\']/div[2]/ul/li[1]/span[1]')
        product_Code = self.dr.find_elements('xpath->//*[@id=\'fund\']/div[2]/ul/li[1]/span[2]')
        product_type = self.dr.find_elements('xpath->//*[@id=\'fund\']/div[2]/ul/li[2]')
        product_rand = self.dr.find_elements('xpath->//*[@id=\'fund\']/div[2]/ul/li[3]')
        product_nav = self.dr.find_elements('xpath->//*[@id=\'fund\']/div[2]/ul/li[4]')
        product_navtotal = self.dr.find_elements('xpath->//*[@id=\'fund\']/div[2]/ul/li[5]')
        product_dayInc = self.dr.find_elements('xpath->//*[@id=\'fund\']/div[2]/ul/li[6]')
        product_weekInc = self.dr.find_elements('xpath->//*[@id=\'fund\']/div[2]/ul/li[7]')
        product_monthInc = self.dr.find_elements('xpath->//*[@id=\'fund\']/div[2]/ul/li[8]')
        product_yearInc = self.dr.find_elements('xpath->//*[@id=\'fund\']/div[2]/ul/li[9]')
        num = len(product_Name_02)
#        self.logger.info('产品总数为：',num,'，产品详情明细如下：')
        for j in range(0,len(product_Name_02)):
            #print('基金名称:',product_Name_02[j].text,'|基金代码:',product_Code[j].text,'|基金类型:',product_type[j].text,'|风险等级:',product_rand[j].text,'|单位净值:',product_nav[j].text,'|累计净值:',product_navtotal[j].text,'|昨日增长率:',product_dayInc[j].text,'|近一周增长率:',product_weekInc[j].text,'|近一月增长率:',product_monthInc[j].text,'|近一年增长率:',product_yearInc[j].text)
            result2 = '基金名称:' + product_Name_02[j].text + '|基金代码:' + product_Code[j].text + '|基金类型：' + product_type[j].text  + '|风险等级:'+ product_rand[j].text + '|单位净值:'+ product_nav[j].text + '|累计净值:'+ product_navtotal[j].text+ '|昨日增长率:'+ product_dayInc[j].text + '|近一周增长率:'+ product_weekInc[j].text + '|近一月增长率:' + product_monthInc[j].text +'|近一年增长率:'+product_yearInc[j].text
            self.logger.info(result2)
        # 统计当前产品总数量，并通过产品数鲁和原先是否一致来校验是否有产品新增
        assert num == 106, 'not equal'


    # 测试财鑫宝页面，页面元素检查（财鑫宝名称、总金额、近七日年化、万份收益）
    def test13_Walletpage(self):
        self.dr.click('link_text->财鑫宝')
        sleep(8)
        product_WalletName = self.dr.get_text('css->#app > div > div.block.block1 > div.title.flex-h.flex-ve > span')
        totalWalletAsset = self.dr.get_text('css->#app > div > div.block.block1 > div.content > div.wallet > div.firstbox > div > span > span')
        occurIncome = self.dr.get_text('css->#app > div > div.block.block1 > div.content > div.wallet > div.pinkbox > div.profit > span.yesterday > span')
        totalIncome = self.dr.get_text('css->#app > div > div.block.block1 > div.content > div.wallet > div.pinkbox > div.profit > span.accumulative > span')
        fundCurrRatio = self.dr.get_text('css->#app > div > div.block.block1 > div.content > div.wallet > div.pinkbox > div.annualized > span')
        perMyriadIncome = self.dr.get_text('css->#app > div > div.block.block1 > div.content > div.wallet > div.pinkbox > div.tenthousand > span')
        sleep(3)
        #print('基金名称:',product_WalletName.text,'|总金额:',totalWalletAsset.text,'|昨日收益:',occurIncome.text,'|累计收益:',totalIncome.text,'|近七日年化:',fundCurrRatio.text,'|万份收益:',perMyriadIncome.text)
        result2 = '基金名称:' +product_WalletName + '|总金额:' + totalWalletAsset + '|昨日收益:' + occurIncome+ '|累计收益:' + totalIncome + '|近七日年化:' +fundCurrRatio + '|万份收益:' + perMyriadIncome
        self.logger.info(result2)

    # pytest实现我的交易页面元素检查，展示我所持有的的产品，并统计总共有多少基金，总共有多少份额，总共昨日盈亏多少，累计盈亏多少，再匹配与基金总市值，昨日盈亏和累计盈亏是否一致
    def test14_Mypage(self):
        self.dr.click('link_text->我的交易')
        sleep(8)
        Mypage_cust_name = self.dr.get_text('css->#app > div > div.maincontent > div.personalinformation > div > div.information > div:nth-child(1) > span:nth-child(1)')
        Mypage_totalAsset = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.content > div.totalamounts > div > span')
        Mypage_totalWalletAsset = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.content > div.product > div.wallet > div.money > span > span')
        Mypage_totalProAsset = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.content > div.product > div.fund > div.money > span > span')
        Mypage_lastdayIncome = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.content > div.product > div.fund > div.yesterday > span')
        Mypage_accumIncome = self.dr.get_text('css->#app > div > div.maincontent > div.mainright > div > div.content > div.product > div.fund > div.accumulative > span')
        sleep(15)
        # 打印账户首页的资产
        # print(Mypage_cust_name.text,',您的总市值为:',Mypage_totalAsset.text,'，财鑫宝总额为:',Mypage_totalWalletAsset.text,'，基金市值为:',Mypage_totalProAsset.text)
        result2 =Mypage_cust_name+',您的总市值为:'+Mypage_totalAsset+'，财鑫宝总额为:'+Mypage_totalWalletAsset+'，基金市值为:'+Mypage_totalProAsset
        self.logger.info(result2)
        # print('您的昨日收益为:',Mypage_lastdayIncome.text[:-4],'，累计收益为:',Mypage_accumIncome.text[:-4])
        result3 = '您的昨日收益为:'+Mypage_lastdayIncome[:-4]+'，累计收益为:'+Mypage_accumIncome[:-4]
        self.logger.info(result3)
        assert float(Mypage_totalWalletAsset.replace(',', '', 3)) + float(Mypage_totalProAsset.replace(',', '', 3)) == float(Mypage_totalAsset.replace(',', '', 3)),'not equal'

        Mypage_proName = self.dr.find_elements('xpath->//*[@id=\'app\']/div/div[3]/div[3]/div/div[2]/div[1]/div[1]/ul/li[1]')
        Mypage_proType = self.dr.find_elements('xpath->//*[@id=\'app\']/div/div[3]/div[3]/div/div[2]/div[1]/div[1]/ul/li[2]')
        Mypage_proAssert = self.dr.find_elements('xpath->//*[@id=\'app\']/div/div[3]/div[3]/div/div[2]/div[1]/div[1]/ul/li[4]')
        Mypage_proShare = self.dr.find_elements('xpath->//*[@id=\'app\']/div/div[3]/div[3]/div/div[2]/div[1]/div[1]/ul/li[5]')
        Mypage_proNewnav = self.dr.find_elements('xpath->//*[@id=\'app\']/div/div[3]/div[3]/div/div[2]/div[1]/div[1]/ul/li[6]')
        Mypage_prolastdayIncome = self.dr.find_elements('xpath->//*[@id=\'app\']/div/div[3]/div[3]/div/div[2]/div[1]/div[1]/ul/li[8]')
        Mypage_proaccumIncome = self.dr.find_elements('xpath->//*[@id=\'app\']/div/div[3]/div[3]/div/div[2]/div[1]/div[1]/ul/li[9]')
        pro_num = len(Mypage_proName)

        Sum_Mypage_proAssert = 0.00
        Sum_Mypage_proShare = 0.00
        Sum_Mypage_prolastdayIncome = 0.00
        Sum_Mypage_proaccumIncome = 0.00

        # 计算所有产品的资产
        for n in range(len(Mypage_proAssert)):
            Sum_Mypage_proAssert = Sum_Mypage_proAssert + float(Mypage_proAssert[n].text.replace(',', '', 3).replace('--', '0.00'))
            Sum_Mypage_proShare = Sum_Mypage_proShare + float(Mypage_proShare[n].text.replace(',', '', 3).replace('--', '0.00'))
            Mypage_prolastdayIncome1=Mypage_prolastdayIncome[n].text.replace(',', '', 3).replace('--', '0.00')
            if '\n' in Mypage_prolastdayIncome1:
                Mypage_prolastdayIncome1 = Mypage_prolastdayIncome1[0:Mypage_prolastdayIncome1.rfind('\n', 1) ]
            print(Mypage_prolastdayIncome1)
            Sum_Mypage_prolastdayIncome = Sum_Mypage_prolastdayIncome + float(Mypage_prolastdayIncome1)
            Sum_Mypage_proaccumIncome = Sum_Mypage_proaccumIncome + float(Mypage_proaccumIncome[n].text.replace(',', '', 3).replace('--', '0.00'))
         # 方便打印用的
        Sum_Mypage_proAssert = str(Sum_Mypage_proAssert)
        Sum_Mypage_proShare =  str(Sum_Mypage_proShare)
        Sum_Mypage_prolastdayIncome =  str(Sum_Mypage_prolastdayIncome)
        Sum_Mypage_proaccumIncome =  str(Sum_Mypage_proaccumIncome)
        result4 = '您的持有基金总市值为:' + Sum_Mypage_proAssert
        result5 = '您的持有基金总份额:' + Sum_Mypage_proShare
        result6 = '您的持有基金昨日盈亏总计为:' + Sum_Mypage_prolastdayIncome
        result7 = '您的持有基金累计盈亏总计为:' + Sum_Mypage_proaccumIncome
        self.logger.info(result4)
        self.logger.info(result5)
        self.logger.info(result6)
        self.logger.info(result7)

        # 统计总共有多少持有产品，并打印详情
        #print('您的持有产品总数为:',pro_num,',持有详情如下：')
        pro_num=str(pro_num)
        result8 = '您的持有产品总数为:' + pro_num+',持有详情如下：'
        self.logger.info(result8)
        for k in range(1, len(Mypage_proName)):
            #print('基金名称:',Mypage_proName[k].text,' |基金类型:',Mypage_proType[k].text,' |基金市值:',Mypage_proAssert[k].text,' |持有份额:',Mypage_proShare[k].text,' |最新净值:',Mypage_proNewnav[k].text[:-11],' |净值日期:',Mypage_proNewnav[k].text[7:],' |昨日盈亏:',Mypage_prolastdayIncome[k].text,' |累计盈亏:',Mypage_proaccumIncome[k].text)
            result9 = '基金名称:' + Mypage_proName[k].text + ' |基金类型:' + Mypage_proType[k].text + ' |基金市值:' + Mypage_proAssert[k].text + ' |持有份额:' + Mypage_proShare[k].text + ' |最新净值:' + Mypage_proNewnav[k].text[:-11] + ' |净值日期:' + Mypage_proNewnav[k].text[7:] + ' |昨日盈亏:' + Mypage_prolastdayIncome[k].text + ' |累计盈亏:' + Mypage_proaccumIncome[k].text
            self.logger.info(result9)

        # 近期交易
        current_trade_fundName = self.dr.find_elements('xpath->//*[@id=\'app\']/div/div[3]/div[3]/div/div[3]/div/div[1]/ul/li[1]')
        current_trade_businFlag = self.dr.find_elements('xpath->//*[@id=\'app\']/div/div[3]/div[3]/div/div[3]/div/div[1]/ul/li[2]')
        current_trade_applyDate = self.dr.find_elements('xpath->//*[@id=\'app\']/div/div[3]/div[3]/div/div[3]/div/div[1]/ul/li[4]')
        current_trade_applyBalance_shares = self.dr.find_elements('xpath->//*[@id=\'app\']/div/div[3]/div[3]/div/div[3]/div/div[1]/ul/li[5]')
        current_trade_confirmDate = self.dr.find_elements('xpath->//*[@id=\'app\']/div/div[3]/div[3]/div/div[3]/div/div[1]/ul/li[6]')
        current_trade_confirmBalance_shares = self.dr.find_elements('xpath->//*[@id=\'app\']/div/div[3]/div[3]/div/div[3]/div/div[1]/ul/li[7]')
        current_trade_deductStatusStr = self.dr.find_elements('xpath->//*[@id=\'app\']/div/div[3]/div[3]/div/div[3]/div/div[1]/ul/li[8]')
        current_trade_confirmFlagStr = self.dr.find_elements('xpath->//*[@id=\'app\']/div/div[3]/div[3]/div/div[3]/div/div[1]/ul/li[9]')
        #print('您的近期交易详情如下：')
        self.logger.info('您的近期交易详情如下：')
        for k in range(0, len(current_trade_fundName)):
           # print('产品名称:',current_trade_fundName[k].text,' |业务类型:',current_trade_businFlag[k].text,' |申请时间:',current_trade_applyDate[k].text,' |申请金（份）额:',current_trade_applyBalance_shares[k].text,' |确认日期:',current_trade_confirmDate[k].text,' |确认金（份）额:',current_trade_confirmBalance_shares[k].text,' |扣款状态:',current_trade_deductStatusStr[k].text,' |确认状态:',current_trade_confirmFlagStr[k].text)
            result10 = '产品名称:'+current_trade_fundName[k].text+' |业务类型:'+current_trade_businFlag[k].text+' |申请时间:'+current_trade_applyDate[k].text+' |申请金（份）额:'+current_trade_applyBalance_shares[k].text+' |确认日期:'+current_trade_confirmDate[k].text+' |确认金（份）额:'+current_trade_confirmBalance_shares[k].text+' |扣款状态:'+current_trade_deductStatusStr[k].text+' |确认状态:'+current_trade_confirmFlagStr[k].text
            self.logger.info(result10)

    # 测试信息公告有无更新
    def test15_Information_notice(self):
        self.dr.click('link_text->信息公告')
        self.dr.click('link_text->证券投资基金公告')
        information_content = self.dr.find_elements('xpath->/html/body/div[4]/div/div[2]/ul/li/a')
        for k in range(0, len(information_content)):
            # print('公告日期：', information_content[k].text[:10],' ||  公告标题：',information_content[k].get_attribute('title'))
            result1 = '公告日期：'+ information_content[k].text[:10]+' ||  公告标题：'+information_content[k].get_attribute('title')
            self.logger.info(result1)
       # assert information_content[k].text[:10] == mydate.getLastBusiness(),'not equal'
        aimdate=information_content[k].text[:10]
        return  aimdate