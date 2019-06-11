# -*- coding: utf-8 -*-#
#  @Time    :2019/3/10  
#  @Author  :jun
#  @Email   :1044622996@qq.com      
#  @File    : ketangpai.py
#  @Software: PyCharm

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.ketangpai.com/')

# 定位方式:class_name

driver.find_element_by_class_name('active').click()  # 元素：首页
driver.find_element_by_class_name('reg-btn').click()  # 元素：免费注册
driver.find_element_by_class_name('login').click()  # 元素：登录
driver.find_element_by_class_name('regist').click()  # 元素：注册
driver.find_element_by_class_name('studend').click()  # 元素：注册课堂派--学生
driver.find_element_by_class_name('teacher').click()  # 元素：注册课堂派--老师/助教
driver.find_element_by_class_name('btn-btn').click()  # 元素：学生注册--注册为学生
driver.find_element_by_class_name('active').click()  # 元素：登录--账号登录
driver.find_element_by_class_name('auto-login').click()  # 元素：账号登录--勾选自动下次登录
driver.find_element_by_class_name('forget').click()  # 元素：账号登录--忘记密码
driver.find_element_by_class_name('qr-sj').click()  # 元素：账号登录--右下角二维码样式
driver.find_element_by_class_name('txt1').click()  # 话题--发起话题--标题
driver.find_element_by_class_name('wangEditor-txt').click()  # 话题--发起话题--内容
driver.find_element_by_class_name('sure').click()  # 话题--发起话题--确认
driver.find_element_by_class_name('down-btn').click()  # 话题--资料-下载
driver.find_element_by_class_name('foldertext').click()  # 话题--资料-查看文件夹

# 定位方式 partial_link_text

driver.find_element_by_partial_link_text('移动端').click()  # 元素：首页--移动端
driver.find_element_by_partial_link_text('手机短信登录').click()  # 元素：登录--手机短信登录
driver.find_element_by_partial_link_text('微信登录').click()  # 元素：登录--微信登录
driver.find_element_by_partial_link_text('关于我们').click()  # 首页底部--关于我们
driver.find_element_by_partial_link_text('联系我们').click()  # 首页底部--联系我们
driver.find_element_by_partial_link_text('服务条款').click()  # 首页底部--服务条款
driver.find_element_by_partial_link_text('浏览器下载').click()  # 首页底部--浏览器下载
driver.find_element_by_partial_link_text('更新动态').click()  # 首页底部--更新动态
driver.find_element_by_partial_link_text('更新动态').click()  # 首页底部--更新动态
driver.find_element_by_partial_link_text('申请机构版').click()  # 首页--解决方案--申请机构版
driver.find_element_by_partial_link_text('本地化部署').click()  # 首页--解决方案--本地化部署

# 定位方式 name

driver.find_element_by_name('mailtel').click()  # 元素 学生注册--邮箱/手机
driver.find_element_by_name('pass').click()  # 元素 学生注册--密码
driver.find_element_by_name('name').click()  # 元素 学生注册--姓名
driver.find_element_by_name('id').click()  # 元素 学生注册--学号
driver.find_element_by_name('school').click()  # 元素 学生注册--学校
driver.find_element_by_name('verify').click()  # 元素 学生注册--验证码
driver.find_element_by_name('account').click()  # 元素：登录--账号
driver.find_element_by_name('pass').click()  # 元素：账号登录--密码
driver.find_element_by_name('tel').click()  # 元素：手机短信登录登录--手机号
driver.find_element_by_name('yzm').click()  # 元素：手机短信登录--验证码

# 定位方式：xpath

driver.find_element_by_xpath('//img[@class="qrcode lightBorder"]')  # 微信登录--二维码
driver.find_element_by_xpath('//a[contains(text(),"课堂").click() and @class = "active"]')  # 登录之后，左上角隐藏--课堂
driver.find_element_by_xpath('//b[contains(text(),"私信").click() and @class = "fl"]')  # 登录之后，左上角隐藏--私信
driver.find_element_by_xpath('//span[contains(text(),"Python全栈第13期")]').click()  # 登录之后，左上角隐藏--Python全栈第13期
driver.find_element_by_xpath('//div[@class="ktcon1 cl"]').click()  # 登录之后，加入班级
driver.find_element_by_xpath('//li[@class ="ktli1"]/child::a').click()  # 登录之后，班级排序
driver.find_element_by_xpath('//li[@class ="ktli2"]/child::a').click()  # 登录之后，归档管理
driver.find_element_by_xpath('//a[@class ="jumptoclass"]').click()  # 登录之后，Python全栈第13期
driver.find_element_by_xpath('//a[@class ="kdmore on"]').click()  # 登录之后，竖行三个点
driver.find_element_by_xpath('//li[@class ="kdli2"]/child::a"]').click()  # 登录之后，竖行三个点--归档
driver.find_element_by_xpath('//li[@class ="kdli3"]/child::a').click()  # 登录之后，竖行三个点--退课
driver.find_element_by_xpath('//a[contains(text(),"元素定位练习")]').click()  # 登录之后，作业
driver.find_element_by_xpath('//span[@class ="hy"]').click()  # 登录之后，成员139
driver.find_element_by_xpath('//li[@class ="all"]').click()  # 登录之后，成员139--全部学生
driver.find_element_by_xpath('//a[@class ="groupdetaillink"]').click()  # 登录之后，成员139--学生分组
driver.find_element_by_xpath('//div[@class ="fixeddetail"]').click()  # 登录之后，成员139--学生分组--查看详情
driver.find_element_by_xpath('//div[@class ="changeactivity"]').click()  # 登录之后，成员139--学生分组--查看详情--切换分组
driver.find_element_by_xpath('//span[contains(text(),"B")]').click()  # 登录之后，成员139--学生分组--查看详情--B组
driver.find_element_by_xpath('//div[@class ="stuquitgroup"]').click()  # 登录之后，成员139--学生分组--查看详情--退出小组
driver.find_element_by_xpath('//div[@class ="selectbox allselect"]').click()  # 登录之后，成员139--学生分组--查看详情--全勾选
driver.find_element_by_xpath('//div[@class ="btnbox groupsendmsg"]').click()  # 登录之后，成员139--学生分组--查看详情--群发私信
driver.find_element_by_xpath('//div[@class ="input-box"]').click()  # 登录之后，成员139--学生分组--查看详情--群发私信--输入框
driver.find_element_by_xpath('//a[@class ="send"]').click()  # 登录之后，成员139--学生分组--查看详情--群发私信--发送
driver.find_element_by_xpath('//a[@class ="send"]/preceding-sibling::a').click()  # 登录之后，成员139--学生分组--查看详情--群发私信--取消
driver.find_element_by_xpath('//span[contains(text(),"条讨论")]').click()  # 作业--0条讨论
driver.find_element_by_xpath(
    '//a[@href = "/Homework/handup/homeworkid/MDAwMDAwMDAwMLR2z5eHqb-y.html" and @class = "sc-btn"]').click()   # 作业--上传作业
driver.find_element_by_xpath('//a[@class = "tj-btn"]').click()  # 作业--提交
driver.find_element_by_xpath('//span[@class = "s2"]').click()  # 作业--留言
driver.find_element_by_xpath('//a[@class = "togglesee"]').click()  # 作业--查看提交日志
driver.find_element_by_xpath('//input[@name = "file"]').click()  # 作业--上传作业
driver.find_element_by_xpath('//span[contains(text(),"话题")]').click()  # 作业--话题
driver.find_element_by_xpath('//span[contains(text(),"发起新话题")]').click()  # 作业--发起话题
driver.find_element_by_xpath('//a[contains(text(),"1-21课程调查，接口实战上完！请问你的学习的如何？")]').click()  # 作业--查看话题
driver.find_element_by_xpath('//a[contains(text(),"课堂详情")]').click()  # 课堂详情
driver.find_element_by_xpath('//a[contains(text(),"个人设置")]').click()  # 个人设置
driver.find_element_by_xpath('//a[contains(text(),"我的VIP")]').click()  # 我的VIP
driver.find_element_by_xpath('//a[contains(text(),"退出账户")]').click()  # 退出账户
driver.find_element_by_xpath('//a[contains(text(),"上传文档")]').click()  # 文库--上传文档
driver.find_element_by_xpath('//li[contains(text(),"历年试卷")]').click()  # 文库--类型
driver.find_element_by_xpath('//a[contains(text(),"课程资源库")]').click()  # 课程资源库--课程资源库
