# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 15:03
# @Author  : wanglanqing

import requests
from utils.db_info import *

class Create_template_act(object):
    def __init__(self,templateTypeName, act_name):
        self.s = requests.session()
        self.s.get('http://api.admin.adhudong.com/login/login_in.htm?name=test&pwd=qq')
        self.templateTypeName=templateTypeName
        self.act_name=act_name
        self.db = DbOperations()

    def create_template_type(self, locationAdress, preview="https://img0.adhudong.com/template/201802/24/999337a35a1a9169450685cc66560a05.png",prizesNum=6,classifi=1):
        '''
        name：模板类型名称
        classifi: 模板分类，抽奖（1）、签到（2）、聚合页（3）,
        prizesNum: 要求奖品数量,
        locationAdress: 代码地址,
        preview: 模板预览图
        '''
        json_body = {
            'name': self.templateTypeName,
            'classifi': classifi,
            'prizesNum': prizesNum,
            'locationAdress': locationAdress,
            'preview': preview
        }
        post_url = "http://api.admin.adhudong.com/template/typeInsert.htm"
        re = self.s.post(post_url, data=json_body)
        if re.status_code==200:
            print('create_template_type,成功了')

    def create_template(self,templateName,templateStyleUrl, positionId=1):
        templateTypeId=self.get_templateTypeId()
        post_url ="http://api.admin.adhudong.com/template/modefy.htm"
        json_body = {
            "positionId": positionId,
            "templateTypeId": templateTypeId, #模板id
            "templateName": templateName, #模板名称
            "templateStyleUrl": templateStyleUrl, #模板样式地址，css
            "templateStyleImage":"https://img3.adhudong.com/template/201802/25/2c6f4700db7982447348db4d0960e3ad.png"
        }
        re = self.s.post(post_url, data=json_body)
        print(re.text)
        if re.status_code ==200:
            print('create_template,成功了')

    def get_templateTypeId(self):
        sql = "select id from voyager.template_type where name='" + self.templateTypeName + "'"
        re = self.db.execute_sql(sql)
        if len(re)!= 1:
            print('名称有问题')
        else:
            templateTypeId = int(re[0][0])
            return templateTypeId

    def get_templateId(self):
        sql = "select id from voyager.base_template_info where template_type_id='" + str(self.get_templateTypeId()) + "'"
        re = self.db.execute_sql(sql)
        if len(re)!= 1:
            print('get_templateId有问题')
        else:
            templateId = int(re[0][0])
            return templateId

    def create_act(self,free_num=20, award_num=6):
        #创建活动sql, act_name,award_num,free_num,template_id
        templateId=self.get_templateId()
        act_sql="""
        INSERT INTO voyager.base_act_info (act_type,act_name,banner_image_url,cover_image_url,award_num,free_num,begin_time,end_time,act_rule_info,`STATUS`,update_time,create_time,template_id,expand1,expand2,expand3,expand4,expand5,expand6,expand7,expand8,expand9,change_times
        )VALUES(
                1,
                {0},
                'https://img4.adhudong.com/award/201802/22/089c376e9519c85ab8ce5fced7c9ea49.jpg',
                NULL,
                {1},
                {2},
                NULL,
                NULL,
                '<p>参与活动即有机会获得大奖。活动为概率中奖，奖品数量有限，祝君好运。</p><p>惊喜一：1000元现金</p><p>惊喜二：500元现金</p><p>惊喜三：200元现金</p><p>惊喜四：100元现金</p><p>惊喜五：50元现金</p><p>惊喜六：幸运奖</p><p>重要声明：</p><p>1、实物类奖品将在活动结束后5-10个工作日内安排发货，请耐心等待</p><p>2、卡券类奖品使用规则详见卡券介绍页</p><p>3、通过非法途径获得奖品的，主办方有权不提供奖品1</p>',
                1,
                now(),
                now(),
                {3},
                1,
                NULL,
                NULL,
                NULL,
                NULL,
                NULL,
                NULL,
                NULL,
                NULL,
                NULL
            );""".format(self.act_name, award_num, free_num, templateId)
        print(act_sql)
        try:
            self.db.execute_sql(act_sql)
            self.db.mycommit()
        except:
            self.db.myrollback()

    def get_actId(self):
        sql = "select id from voyager.base_act_info where act_name='" + self.act_name + "'"
        print(sql)
        re = self.db.execute_sql(sql)
        if len(re)!= 1:
            print('活动名称有问题')
        else:
            act_id = int(re[0][0])
            return act_id

    def create_awards(self):
        act_id = str(self.get_actId())
        # act_id = str(self.get_actId('淘粉吧转盘0228'))
        #创建奖品的sql
        award_ths =    ''',0,15,1,now(),now(),'谢谢参与','https://img0.adhudong.com/association/201802/22/10bf5888ea77ea198db1dbadc663b05f.jpg',
                  6,NULL,NULL,NULL,'<p>商品详情的信息</p>','<p>&nbsp;1.实物类奖品将在活动结束后5-10个工作日内安排发货，请耐心等待；</p><p>2.卡券类奖品使用规则详见卡券介绍页&nbsp;</p>')'''
        award_onemore= ''',0,15,2,now(),now(),'再抽一次奖品','https://img4.adhudong.com/association/201802/22/49b99fca05649598059cc2dc733509f4.jpg',
                  5,NULL,NULL,NULL,'<p>商品详情的信息</p>','<p>&nbsp;1.实物类奖品将在活动结束后5-10个工作日内安排发货，请耐心等待；</p><p>2.卡券类奖品使用规则详见卡券介绍页&nbsp;</p>')'''
        award_lucky1=  ''',0,70,3,now(),now(),'百元现金红包','https://img3.adhudong.com/association/201802/22/2c6f4700db7982447348db4d0960e3ad.png',
                7,NULL,NULL,NULL,'<p>商品详情的信息</p>','<p>&nbsp;1.实物类奖品将在活动结束后5-10个工作日内安排发货，请耐心等待；</p><p>2.卡券类奖品使用规则详见卡券介绍页&nbsp;</p>')'''
        award_lucky2=   ''',0,0,4,now(),now(),'20G流量','https://img2.adhudong.com/association/201802/22/d1c54c0eb8259f992f500015f67f8907.png',
                7,NULL,NULL,NULL,'<p>商品详情的信息</p>','<p>&nbsp;1.实物类奖品将在活动结束后5-10个工作日内安排发货，请耐心等待；</p><p>2.卡券类奖品使用规则详见卡券介绍页&nbsp;</p>')'''
        award_lucky3 =  ''',0,0,5,now(),now(),'第3个大奖品','https://img0.adhudong.com/association/201802/22/a4a40a28a4b21c1b50011102f07801a0.png',
                7,NULL,NULL,NULL,'<p>商品详情的信息</p>','<p>&nbsp;1.实物类奖品将在活动结束后5-10个工作日内安排发货，请耐心等待；</p><p>2.卡券类奖品使用规则详见卡券介绍页&nbsp;</p>')'''
        award_lucky4 =  ''',0,0,6,now(),now(),'第4个奖品','https://img0.adhudong.com/association/201802/22/a4a40a28a4b21c1b50011102f07801a0.png',
                7,NULL,NULL,NULL,'<p>商品详情的信息</p>','<p>&nbsp;1.实物类奖品将在活动结束后5-10个工作日内安排发货，请耐心等待；</p><p>2.卡券类奖品使用规则详见卡券介绍页&nbsp;</p>')'''
        award_list = [award_ths, award_onemore, award_lucky1, award_lucky2, award_lucky3, award_lucky4]
        for award in award_list:
            award_sql = '''INSERT INTO act_award (
                act_id,
                award_id,
                award_rate,
                priority,
                update_time,
                create_time,
                show_copy,
                award_icon,
                act_award_type,
                begin_time,
                end_time,
                award_num,
                award_details,
                award_get_instructions
            )
            VALUES (''' + act_id + award
            print(award_sql)
            try:
                self.db.execute_sql(award_sql)
                self.db.mycommit()
            except:
                self.db.myrollback()

    def __del__(self):
        self.db.close_cursor()
        self.db.close_db()

if __name__=='__main__':
    #为模板类型名称
    ct = Create_template_act('淘粉吧转盘0301',"淘粉吧转盘0301")
    #创建模板类型，create_template_type(self, classifi, locationAdress, preview="https://img0.adhudong.com/template/201802/24/999337a35a1a9169450685cc66560a05.png",prizesNum=6)
    ct.create_template_type('https://display.adhudong.com/new/rotary_table_pink.html')
    #创建模板 ct.create_template(templateName, templateStyleUrl)
    ct.create_template('淘粉吧转盘_0301',"https://display.adhudong.com/activity/favicon.ico")
    #创建活动，    create_act(self, act_name,free_num=20, award_num=6)
    ct.create_act()
    #创建活动关联的奖品，
    ct.create_awards()



    # def create_act(self ):
    #     '''
    #     :return:
    #     '''
    #     post_url = "http://api.admin.adhudong.com/act/modefy.htm"
    #     headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    #     json_body ={
    #         "freeNum": 8,
    #         "status": 1,
    #         "awardNum": 3,
    #         "expand1": 1,
    #         "templateId": 229,
    #         "awardList": [{
    #             "id": "rc-award-1519523150433-85",
    #             "priority": 1,
    #             "awardId": "null",
    #             "awardRate": 70,
    #             "awardGetInstructions": "<p>&nbsp;1.实物类奖品将在活动结束后5-10个工作日内安排发货，请耐心等待；</p><p>2.卡券类奖品使用规则详见卡券介绍页&nbsp;</p>",
    #             "actAwardType": 7,
    #             "awardIcon": "https://img1.adhudong.com/association/201802/25/3b667fbd84149001a1c35071350e5c21.png",
    #             "showCopy": "大礼包奖品",
    #             "awardDetails": "<p>商品详情：</p><p>1.</p>"
    #         }, {
    #             "id": "rc-award-1519523102290-44",
    #             "priority": 3,
    #             "awardRate": 15,
    #             "awardId": "null",
    #             "awardGetInstructions": "<p>&nbsp;1.实物类奖品将在活动结束后5-10个工作日内安排发货，请耐心等待；</p><p>2.卡券类奖品使用规则详见卡券介绍页&nbsp;</p>",
    #             "actAwardType": 6,
    #             "awardIcon": "https://img0.adhudong.com/association/201802/25/10bf5888ea77ea198db1dbadc663b05f.jpg",
    #             "showCopy": "谢谢参与",
    #             "awardDetails": "<p>商品详情：</p><p>1.为虚拟商品</p><p>2.奖品不兑付</p>"
    #         }, {
    #             "id": "rc-award-1519523076018-70",
    #             "actAwardType": 5,
    #             "awardRate": 15,
    #             "awardId": "null",
    #             "priority": 2,
    #             "showCopy": "再抽一次",
    #             "awardIcon": "https://img4.adhudong.com/association/201802/25/49b99fca05649598059cc2dc733509f4.jpg",
    #             "awardDetails": "<p>商品详情：</p><p>1.萨德</p><p>2.萨德</p>",
    #             "awardGetInstructions": "<p>&nbsp;1.实物类奖品将在活动结束后5-10个工作日内安排发货，请耐心等待；</p><p>2.卡券类奖品使用规则详见卡券介绍页&nbsp;</p>"
    #         }],
    #         "actName": "从list6",
    #         "changeTimes": 2,
    #         "bannerImageUrl": "https: //img3.adhudong.com/award/201802/25/9867c921ca0178820b8a37c677876223.jpg",
    #         "actRuleInfo": "<p>参与活动即有机会获得大奖。活动为概率中奖，奖品数量有限，祝君好运。</p><p>惊喜一：1000元现金</p><p>惊喜二：500元现金</p><p>惊喜三：200元现金</p><p>惊喜四：100元现金</p><p>惊喜五：50元现金</p><p>惊喜六：幸运奖</p><p>重要声明：</p><p>1、实物类奖品将在活动结束后5-10个工作日内安排发货，请耐心等待</p><p>2、卡券类奖品使用规则详见卡券介绍页</p><p>3、通过非法途径获得奖品的，主办方有权不提供奖品</p>"
    #     }
    #     res = self.s.post(post_url, data=json_body,headers=headers)
    #     # res = self.s.get(post_url, params=json_body)
    #     print(res.url)
    #     print(res.text)