# -*- coding:utf-8 -*-
'''
Created on 2016-10-19
获取tjpu教务系统绩点信息
@author: jbw
'''

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib
import urllib2
import re
import cookielib
import sys
import os
import string
import random
from bs4 import BeautifulSoup


class TJPUSpider:
    # 模拟登录tjpu教务系统

    def __init__(self):
        self.baseURL = ""
        self.enable = True
        self.charaterset = "gb2312"
        string = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36"
        self.headers = {'User-Agent': string}
        self.cookie = cookielib.CookieJar()
        self.hander = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.hander)

    # 验证码处理
    def getCheckCode(self):
        # 验证码连接
        checkcode_url = "http://jwpt.tjpu.edu.cn//validateCodeAction.do"
        #request = urllib2.Request(checkcode_url, headers=self.headers)
        #picture = self.opener.open(request).read()
        # 将验证码写入本地（默认与源文件在同一文件夹下）,用urlretrieve方法
        urllib.request.urlretrieve(checkcode_url,"check_code.jpg")
        #local = open("checkcode.jpg", "wb")
        #local.write(picture)
        #local.close()
        # 手工输入验证码
        txt_check = raw_input(str("请输入验证码:"))
        return txt_check

    # 模拟登陆
    def login(self, userid, userpwd):
        # 获取验证码
        txt_check = self.getCheckCode()
        postData = {"zjh": userid, "mm": userpwd, "v_yzm": txt_check}
        data = urllib.urlencode(postData)

        request_url = "http://jwpt.tjpu.edu.cn/loginAction.do"
        request_login = urllib2.Request(request_url, headers=self.headers)
        response = self.opener.open(request_login, data)
        content = response.read().decode('gbk').encode('utf-8')
        # print(content)
        bsObj = BeautifulSoup(content)
        if bsObj.find("title").get_text() == "URP综合教务系统 - 登录":
            print "登录失败！请检查学号、密码或验证码后重新登录！"
            return False
        else:
            print "登录成功！欢迎观临天津工业大学" + bsObj.find("title").get_text().strip() + "系统!"
            return True

    # 登录成功后爬取成绩数据
    def processData(self):
        request_url = "http://jwpt.tjpu.edu.cn/gradeLnAllAction.do?type=ln&oper=qbinfo&lnxndm=2015-2016%D1%A7%C4%EA%B4%BA(%C1%BD%D1%A7%C6%DA)"
        request_grades = urllib2.Request(request_url, headers=self.headers)
        response = self.opener.open(request_grades)
        content = response.read().decode("gbk").encode("utf-8")
        print "-----------------------以下是您的成绩记录---------------------------"
        self.showData(content)
        # print content

    # 数据的显示
    def showData(self, html_content):
        credit_list = []
        grade_list = []
        bsObj = BeautifulSoup(html_content)
        grades_html_list = bsObj.findAll("tr", {"class": "odd"})
        print "您一共有" + str(len(grades_html_list)) + "条成绩记录！"
        # print grades_html_list[0]
        for i in grades_html_list:
            #course_obj = BeautifulSoup(str(i))
            td_tag_list = i.findAll("td", {"align": "center"})

            print "课程名：" + td_tag_list[2].get_text().strip() + "-----" + "学分:" + str(td_tag_list[4].get_text().strip()) + "-----" + "成绩:" + str(td_tag_list[6].get_text().strip())

            if "CET" in str(td_tag_list[2].get_text().strip()) :
                print "四六级成绩不算做学分绩内！"
            elif str(td_tag_list[6].get_text().strip()) == "通过":
                print "通过的成绩算作100.0分！"
                credit_list.append(float(td_tag_list[4].get_text().strip()))
                grade_list.append(100.0)
            elif float(td_tag_list[6].get_text().strip()) == 0.0:
                print str(td_tag_list[2].get_text().strip()) + "这门课程未修！不算做学分绩计算内！"
            else:
                credit_list.append(float(td_tag_list[4].get_text().strip()))
                grade_list.append(float(td_tag_list[6].get_text().strip()))

        self.calculateGPA(credit_list, grade_list)

    # 计算平均学分绩的方法，传入学分列表和成绩列表作为参数
    def calculateGPA(self, creditlst, gradelst):
        # print creditlst
        # print gradelst
        product_sum = credit_sum = 0.0
        for i in range(len(creditlst)):
            product_sum = product_sum + creditlst[i] * gradelst[i]
            credit_sum = credit_sum + creditlst[i]
        print "您的百分制绩点为：" + str(product_sum / credit_sum)


if "__main__" == __name__:
    userid = raw_input(str("请输入学号:"))
    userpwd = raw_input(str("请输入密码:"))
    gpa_spider = TJPUSpider()
    if(gpa_spider.login(userid, userpwd)):
        gpa_spider.processData()
