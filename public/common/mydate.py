import calendar
import datetime
import time

class TimeUtil:
    # 获取当月非周六周日群组
    def getDateByTime(self):
        self.myDate = []
        t = str(time.strftime('%Y-%m-'))
        for i in range(1, 32):
            timeStr = t + str(i)
            try:
                # 字符串转换为规定格式的时间
                tmp = time.strptime(timeStr, '%Y-%m-%d')
                # 判断是否为周六、周日
                if (tmp.tm_wday != 6) and (tmp.tm_wday != 5):
                    self.myDate.append(time.strftime('%Y-%m-%d', tmp))
            except:
                print('日期越界')
        if len(self.myDate) == 0:
            self.myDate.append(time.strftime('%Y-%m-%d'))
        return self.myDate
    # 获取本月工作日群组
    def getDateByDateTime(self):
        self.myDate = []
        now = datetime.datetime.now()
        tmp = now.strftime('%Y-%m-')
        # 通过calendar获取到当月第一天的weekday，以及当月天数
        t = calendar.monthrange(now.year, now.month)
        for i in range(1, t[1]):
            dateTmp = tmp + str(i)
            myDateTmp = datetime.datetime.strptime(dateTmp, '%Y-%m-%d')
            if myDateTmp.isoweekday() != 6 and myDateTmp.isoweekday() != 7:
                self.myDate.append(myDateTmp.strftime('%Y-%m-%d'))
        if len(self.myDate) == 0:
            self.myDate.append(now.strftime('%Y-%m-%d'))
        return self.myDate
    # 获取上一工作日
    def getLastBusiness(self):
        lastworkday = ''
        date = datetime.datetime.today()  # 今天
        # print(date.today())
        w = date.weekday() + 1
        # print(w) #周日到周六对应1-7
        if w == 1:  # 如果是周一，则返回上周五
            lastworkday = (date + datetime.timedelta(days=-3)).strftime("%Y-%m-%d")
        elif 1 < w < 7:  # 如果是周二到周五，则返回昨天
            lastworkday = (date + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        elif w == 7:  # 如果是周日，返回周五
            lastworkday = (date + datetime.timedelta(days=-2)).strftime("%Y-%m-%d")
        return lastworkday
    # 获取昨日日期
    def getYesterday(self):
        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        yesterday = today - oneday
        return yesterday
