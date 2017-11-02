#!/usr/bin/env python
#coding=utf-8
######################################
###  版本:v2.0
###  更新日期：2016-01-11
###  更新说明：增加了add_dim,add_category,
###　　　　　　　get_dimension_id的方法
###         增加ofdb_sql 语句
### 更新日期：2016-02017
### 更新说明：增加了add_ofmucmember，用于同步ofmucmember
######################################

import MySQLdb
import os

class TestData(object):
    '生成测试数据'

    def __init__(self):
        pass

    def open_db(self, server, db, user, passwd):
        self.db = MySQLdb.connect(server, user, passwd, db, charset='utf8')
        self.cursor = self.db.cursor()

    def close_db(self):
        self.db.close()

    def get_org_id(self, org_name):
        '根据组织名称得到组织ID'

        sql_str = u"select org_id from t_organization where org_name='" + org_name + "'"
        self.cursor.execute(sql_str)
        data = self.cursor.fetchall()
        
        n = len(data)
        if n == 1:
            return data[0][0]
        elif n == 0:
            return 0
        else:
            return -1

    def add_root_org(self, file_name):
        '生成根组织'
        num = 0
        
        conf = open(file_name)
        for line in conf:
            (uuid, org_name, parent_id, is_logical, phone, fax, manager, address, remarks, created_by, created_time, updated_by, updated_time, is_deleted, deleted_time) = [field.strip().decode('utf-8') for field in line.strip().split(',')]
            if self.get_org_id(org_name) == 0:
                sql_str = u"insert into t_organization(uuid, org_name, root_org_id, parent_id, is_logical, phone, fax, manager, address, remarks, created_by, created_time, updated_by, updated_time, is_deleted, deleted_time) value('" + uuid + "','" + org_name + "', 1," + parent_id + "," + is_logical + ",'" + phone + "','" + fax + "'," + manager + ",'" + address + "','" + remarks + "'," + created_by + ",'" + created_time + "'," + updated_by + ",'" + updated_time + "'," + is_deleted + "," + deleted_time + ")"
                try:
                    self.cursor.execute(sql_str)
                except MySQLdb.Error, e:
                    print e
                org_id = self.get_org_id(org_name)
                sql_str = u"update t_organization set root_org_id=" + str(org_id) + " where org_name='" + org_name + "'"
                act_sql_str = u"insert into hydt_bcm_act.ACT_ID_GROUP values('" + str(org_id) + "', 1 " + ",'" + org_name + "','assignment')"
                try:
                    self.cursor.execute(sql_str)
                    self.cursor.execute(act_sql_str)
                except MySQLdb.Error, e:
                    print e
                num += 1
            else:
                print "ERROR: oranization " + org_name + " is already in the system"
                continue

        self.db.commit() 
        conf.close()

    def add_org(self, file_name):
        '生成子组织'

        conf = open(file_name)
        for line in conf:
            (uuid, org_name, is_logical, phone, fax, manager, address, remarks, created_by, created_time, updated_by, updated_time, is_deleted, deleted_time, root_org_name, parent_name) = [field.strip().decode('utf-8') for field in line.strip().split(',')]
            root_org_id = self.get_org_id(root_org_name)
            parent_id = self.get_org_id(parent_name)
            print uuid
            if root_org_id == 0:
                print "ERROR: organization " + root_org_name + " is not in system"
                continue
            if parent_id == 0:
                print "ERROR: organization " + parent_name + " is not in system"
                continue
            if self.get_org_id(org_name) == 0:
                sql_str = u"insert into t_organization(uuid, org_name, root_org_id, parent_id, is_logical, phone, fax, manager, address, remarks, created_by, created_time, updated_by, updated_time, is_deleted, deleted_time) values ('" + uuid + "','" + org_name + "', " + str(root_org_id) + "," + str(parent_id) + "," + is_logical + ",'" + phone + "','" + fax + "'," + manager + ",'" + address + "','" + remarks + "'," + created_by + ",'" + created_time + "'," + updated_by + ",'" + updated_time + "'," + is_deleted + "," + deleted_time + ')'
                try:
                    self.cursor.execute(sql_str)
                    org_id = self.get_org_id(org_name)
                    act_sql_str = u"insert into hydt_bcm_act.ACT_ID_GROUP values('" + str(org_id) + "', 1 " + ",'" + org_name + "','assignment')"
                    self.cursor.execute(act_sql_str)
                except MySQLdb.Error, e:
                    print e
            else:
                print "ERROR: organization " + org_name + " is already in the system"
                continue

        self.db.commit()
        conf.close()

    def get_user_id(self, user_name):
        '根据用户名得到用户ID'

        sql_str = u"select user_id from t_user where user_name = '" + user_name + "'"
        self.cursor.execute(sql_str)
        data = self.cursor.fetchall()
        n = len(data)
        if n==1:
            return data[0][0]
        elif n==0:
            return 0
        else:
            return -1

    def add_user(self, file_name):
        '生成新用户'

        conf = open(file_name)
        for line in conf:
            (uuid, user_name, password, salt, email, office_phone, home_phone, mobile, wx, qq, home_page, user_state, login_state, force_pwd_change, pwd_err_count, remarks, created_by, created_time, updated_by, updated_time, is_deleted, deleted_time, root_org_name) = [field.strip().decode('utf-8') for field in line.split(',')]
            if self.get_user_id(user_name)==0:
                root_org_id = self.get_org_id(root_org_name)
                if root_org_id==0:
                    print "ERROR: can not find the ID for " + root_org_name
                    continue

                sql_str = u"insert into t_user(uuid, user_name, password, salt, email, office_phone, home_phone, mobile, wx, qq, home_page, user_state, login_state, force_pwd_change, pwd_err_count, remarks, created_by, created_time, updated_by, updated_time, is_deleted, deleted_time, root_org_id) values('" + uuid + "','" + user_name + "','" + password + "','" + salt + "','" + email + "','" + office_phone + "','" + home_phone + "','" + mobile + "','" + wx + "','" + qq + "'," + home_page + "," + user_state + "," + login_state + "," + force_pwd_change + "," + pwd_err_count + ",'" + remarks + "'," + created_by + ",'" + created_time + "'," + updated_by + ",'" + updated_time + "'," + is_deleted + "," + deleted_time + "," + str(root_org_id) + ")"      
                try:
                    self.cursor.execute(sql_str)
                    #hydt_bcm_act.ACT_ID_USER 
                    user_id = self.get_user_id(user_name)
                    sql_str = u"insert into hydt_bcm_act.ACT_ID_USER values('" + str(user_id) + "', 1 " + ",'" + user_name + "','" + mobile + "','" + email + "','" + password + "',NULL)"
                    self.cursor.execute(sql_str)
                except MySQLdb.Error, e:
                    print e
            else:
                print "ERROR: user " + user_name + " is already in the system"
                continue

        self.db.commit()
        conf.close()

    def add_org_user(self, file_name):
        '增加组织和用户关系'

        conf = open(file_name)
        for line in conf:   
            (org_name, user_name) = [field.strip().decode('utf-8') for field in line.split(',')]
            org_id = self.get_org_id(org_name)
            user_id = self.get_user_id(user_name)
            if org_id>0 and user_id>0 :
                sql_str = u"select org_id from t_org_user where org_id=" + str(org_id) + " and user_id=" + str(user_id)
                self.cursor.execute(sql_str)
                data = self.cursor.fetchall()
                if len(data)>0:
                    print "ERROR: org_name " + org_name + str(org_id) + " user_name " + user_name + str(user_id) + " is already in the t_org_user table"
                    continue

                sql_str = u"insert into t_org_user values (" + str(org_id) + "," + str(user_id) + ")"
                act_sql_str = u"insert into hydt_bcm_act.ACT_ID_MEMBERSHIP values (" + str(user_id) + "," + str(org_id) + ")"
                try:
                    self.cursor.execute(sql_str)
                    self.cursor.execute(act_sql_str)
                except MySQLdb.Error, e:
                    print e
            else:
                print "ERROR: organization " + org_name + " or user " + user_name + " is not in the system "
                continue

        self.db.commit()
        conf.close()

    def get_role_id(self, role_name):
        '根据角色名称得到角色ID'

        sql_str = u"select role_id from t_role where role_name='" + role_name + "'"
        self.cursor.execute(sql_str)
        data = self.cursor.fetchall()
        n = len(data)
        if n>0:
            return data[0][0]
        elif n==0:
            return 0
        else:
            return -1

    def add_role(self, file_name):
        '增加角色'

        conf = open(file_name)
        for line in conf:
            (uuid, role_name, description, is_sys, created_by, created_time, updated_by, updated_time, is_deleted, deleted_time, root_org_name) = [field.strip().decode('utf-8') for field in line.split(',')]
            if self.get_role_id(role_name)==0:
                root_org_id = self.get_org_id(root_org_name)
                if root_org_id==0:
                    print "ERROR: can not find the ID for " + root_org_name
                    continue
                sql_str = u"insert into t_role(uuid, role_name, description, is_sys, created_by, created_time, updated_by, updated_time, is_deleted, deleted_time, root_org_id) values('" + uuid + "','" + role_name + "','" + description + "'," + is_sys + "," + created_by + ",'" + created_time + "'," + updated_by + ",'" + updated_time + "'," + is_deleted + "," + deleted_time + "," + str(root_org_id) + ")"
                try:
                    self.cursor.execute(sql_str)
                except MySQLdb.Error, e:
                    print e
            else:
                print "ERROR: role " + role_name + " is already in the system"
                continue
        self.db.commit()
        conf.close()
    
    def add_user_role(self, file_name):
        '增加用户角色关系'

        conf = open(file_name)
        for line in conf:
            (user_name, role_name) = [field.strip().decode('utf-8') for field in line.split(',')]
            user_id = self.get_user_id(user_name)
            role_id = self.get_role_id(role_name)
            if user_id>0 and role_id>0:
                sql_str = u"select user_id from t_user_role where user_id=" + unicode(user_id) + " and role_id=" + unicode(role_id)
                self.cursor.execute(sql_str)
                data = self.cursor.fetchall()
                if len(data)>0 :
                    print "ERROR: user " + user_name + unicode(user_id) + " role " + role_name + unicode(role_id) + " is already in the t_user_role table"
                    continue
                sql_str = u"insert into t_user_role values(" + unicode(user_id) + "," + unicode(role_id) + ")"
                try:
                    self.cursor.execute(sql_str)
                except MySQLdb.Error, e:
                    print e
            else:
                print "ERROR: user " + user_name + " or role " + role_name + " not found in the system"
                continue
        self.db.commit()
        conf.close()
    
    def update_manager(self, file_name):
        conf = open(file_name)
        for line in conf:
            (org_name, user_name) = [field.strip().decode('utf-8') for field in line.split(',')]
            user_id = self.get_user_id(user_name)
            if user_id==0 :
                print "ERROR: can not found user " + user_name
                continue
            org_id = self.get_org_id(org_name)
            if org_id==0 :
                print "ERROR: can not found org " + org_name
                continue
            sql_str = u"update t_organization set manager=" + unicode(user_id) + " where org_name='" + org_name + "'"
            try:
                self.cursor.execute(sql_str)
            except MySQLdb.Error, e:
                print e
        self.db.commit()
        conf.close()
        
    def get_menu_id(self, menu_name):
        '根据菜单名称得到菜单ID'

        sql_str = u"select menu_id from t_menu where menu_name='" + menu_name + "'"
        self.cursor.execute(sql_str)
        data = self.cursor.fetchall()
        n = len(data)
        if n>0:
            return data[0][0]
        elif n==0:
            return 0
        else:
            return -1
        
    def add_role_menu(self, file_name):
        '增加角色-菜单关系'

        conf = open(file_name)
        for line in conf:
            (menu_name, role_name) = [field.strip().decode('utf-8') for field in line.split(',')]
            menu_id = self.get_menu_id(menu_name)
            role_id = self.get_role_id(role_name)
            if menu_id>0 and role_id>0:
                sql_str = u"select menu_id from t_role_menu where menu_id=" + unicode(menu_id) + " and role_id=" + unicode(role_id)
                self.cursor.execute(sql_str)
                data = self.cursor.fetchall()
                if len(data)>0 :
                    print "ERROR: menu " + menu_name + unicode(menu_id) + " role " + role_name + unicode(role_id) + " is already in the t_user_role table"
                    continue
                sql_str = u"insert into t_role_menu values(" + unicode(role_id) + "," + unicode(menu_id) + ")"
                try:
                    self.cursor.execute(sql_str)
                except MySQLdb.Error, e:
                    print e
            else:
                print "ERROR: menu " + menu_name + " or role " + role_name + " not found in the system"
                continue
        self.db.commit()
        conf.close()
    
    def get_res_id(self, res_name):
        '根据资源名称得到资源ID'

        sql_str = u"select res_id from t_resource where res_name='" + res_name + "'"
        self.cursor.execute(sql_str)
        data = self.cursor.fetchall()
        n = len(data)
        if n>0:
            return data[0][0]
        elif n==0:
            return 0
        else:
            return -1
        
    def add_role_res(self, file_name):
        '增加角色-资源关系'

        conf = open(file_name)
        for line in conf:
            (res_name, role_name) = [field.strip().decode('utf-8') for field in line.split(',')]
            res_id = self.get_res_id(res_name)
            role_id = self.get_role_id(role_name)
#             print res_id
#             print role_id
            if res_id>0 and role_id>0:
                sql_str = u"select res_id from t_role_res where res_id=" + unicode(res_id) + " and role_id=" + unicode(role_id)
                self.cursor.execute(sql_str)
                data = self.cursor.fetchall()
                if len(data)>0 :
                    print "ERROR: res " + res_name + unicode(res_id) + " role " + role_name + unicode(role_id) + " is already in the t_user_role table"
                    continue
                sql_str = u"insert into t_role_res values(" + unicode(role_id) + "," + unicode(res_id) + ")"
                try:
                    self.cursor.execute(sql_str)
                except MySQLdb.Error, e:
                    print e
            else:
                print "ERROR: res " + res_name + " or role " + role_name + " not found in the system"
                continue
        self.db.commit()
        conf.close()

    def add_user_shortcut_menu(self, file_name):
        '增加用户、快捷菜单关系表'

        conf = open(file_name)
        for line in conf:
            (user_name, menu_name) = [field.strip().decode('utf-8') for field in line.split(',')]
            user_id = self.get_user_id(user_name)
            menu_id = self.get_menu_id(menu_name)
            if user_id>0 and menu_id>0:
                sql_str = u"select user_id from t_user_shortcut_menu where user_id=" + unicode(user_id) + " and menu_id=" + unicode(menu_id)
                self.cursor.execute(sql_str)
                data = self.cursor.fetchall()
                if len(data)>0 :
                    print "ERROR: user " + user_name + unicode(user_id) + " role " + menu_name + unicode(menu_id) + " is already in the t_user_role table"
                    continue
                sql_str = u"insert into t_user_shortcut_menu values(" + unicode(user_id) + "," + unicode(menu_id) + ")"
                try:
                    self.cursor.execute(sql_str)
                except MySQLdb.Error, e:
                    print e
            else:
                print "ERROR: user " + user_name + " or menu " + menu_name + " not found in the system"
                continue
        self.db.commit()
        conf.close()

    def get_roomID(self, org_name):
        '根据组织名称得到组织ID'

        sql_str = u"select roomID from hydt_ofdb.ofmucroom  where naturalName='" + org_name + "'"
        print sql_str
        self.cursor.execute(sql_str)
        data = self.cursor.fetchall()
        print data
        n = len(data)
        if n == 1:
            return data[0][0]
        elif n == 0:
            return 0
        else:
            return -1
        
    def get_mobile(self, user_name):
        '根据组织名称得到组织ID'

        sql_str = u"select CONCAT(mobile,'@im.ihydt.com') from hydt_bcm.t_user  where user_name='" + user_name + "'"
        print sql_str
        self.cursor.execute(sql_str)
        data = self.cursor.fetchall()
        
        n = len(data)
        if n == 1:
            return data[0][0]
        elif n == 0:
            return 0
        else:
            return -1

    def add_ofmucmember(self, file_name):
        '增加组织和用户关系'

        conf = open(file_name)
        for line in conf:   
            (org_name, user_name) = [field.strip().decode('utf-8') for field in line.split(',')]
            roomID = self.get_roomID(org_name)
            print roomID
            mobile = self.get_mobile(user_name)
            print mobile
            if roomID>0 and mobile>0 :
                #sql_str = u"select org_id from t_org_user where org_id=" + str(org_id) + " and user_id=" + str(user_id)
                #self.cursor.execute(sql_str)
                #data = self.cursor.fetchall()
                #if len(data)>0:
                    # print "ERROR: org_name " + org_name + str(roomID) + " user_name " + mobile  + " is already in the  table"
                    #continue
                sql_str = u"insert into hydt_ofdb.ofmucmember (roomID,jid) values (" + str(roomID) + "," + "'" + str(mobile) +"'" + ")"
                print sql_str
                try:
                    self.cursor.execute(sql_str)
                    #self.cursor.execute(act_sql_str)
                except MySQLdb.Error, e:
                    print e
            else:
                #print "ERROR: organization " + org_name + " or user " + user_name + " is not in the system "
                continue

        self.db.commit()
        conf.close()
        
    def add_dim(self):
        '增加维度'
#         conf = open(file_name)
#         for line in conf:
#             (dimensionality_name, root_org_name, remarks, created_by, created_time, updated_by, updated_time) = [field.strip().decode('utf-8') for field in line.split(',')]
#             if self.get_org_id(root_org_name)==0:
        root_org_id = self.get_org_id("AUTO")
        if root_org_id==0:
            print "ERROR: method add_dim can not find the ID for AUTO"
#        continue
        sql_str1 = u"insert into t_dimensionality (dimensionality_name,root_org_id, remarks, created_by, created_time, updated_by, updated_time) values (" + u"'核心交易'" + "," + str(root_org_id) + "," + u"'初始化的维度1'" + "," + "1" + "," + "'2016-02-15 15:50:59'" + "," + "1" + "," + "'2016-02-15 15:50:59'" +  ")"
        sql_str2 = u"insert into t_dimensionality (dimensionality_name,root_org_id, remarks, created_by, created_time, updated_by, updated_time) values (" + u"'危机公关'" + "," + str(root_org_id) + "," + u"'初始化的维度 2'" + "," + "1" + "," + "'2016-02-15 15:50:59'" + "," + "1" + "," + "'2016-02-15 15:50:59'" +  ")"
        sql_str3 = u"insert into t_dimensionality (dimensionality_name,root_org_id, remarks, created_by, created_time, updated_by, updated_time) values (" + u"'表单'" + "," + str(root_org_id) + "," + u"'初始化的维度 3'" + "," + "1" + "," + "'2016-02-15 15:50:59'" + "," + "1" + "," + "'2016-02-15 15:50:59'" +  ")"
#         print sql_str1
#         print sql_str2
#         print sql_str3
        try:
            self.cursor.execute(sql_str1)
            self.cursor.execute(sql_str2)
            self.cursor.execute(sql_str3)
        except MySQLdb.Error, e:
            print e
#         else:
#             print "ERROR: method add_dim " + dimensionality_name + " is already in the system"
#             continue
        self.db.commit()
#        conf.close()
 
    def get_dimension_id(self):
        '根据维度名称得到维度ID'

        sql_str = u"select dimensionality_id from t_dimensionality where dimensionality_name in ('核心交易','危机公关','表单')" 
#        print sql_str
        self.cursor.execute(sql_str)
        data = self.cursor.fetchall()
        
        n = len(data)
        print n
        if n == 1:
            return data[0][0]
        elif n == 0:
            return 0
        else:
            return data       
        
    def add_category(self):
        '增加分类'
#         conf = open(file_name)
#         for line in conf:
#             (category_name, path, dimensionality_name, remarks, created_by, created_time, updated_by, updated_time) = [field.strip().decode('utf-8') for field in line.split(',')]
#             if self.get_dimension_id(dimensionality_name)==0: 
        dimensionality_id= self.get_dimension_id()
        if dimensionality_id==0:
            print "ERROR: method add_category can not find ('核心交易','危机公关','表单')" 
#                     continue
        sql_str1 = u"insert into t_category (category_name, path, dimension_id, remarks, created_by, created_time, updated_by, updated_time) values (" + u"'记账'" + "," +"'/group1/M00/00/00/ezk4eVaYnIaAHrG0AAATQRFycuY974.png'"+ "," + str(dimensionality_id[0][0]) + "," + u"'紫色的雨雪图片'" + "," + "1" + "," + "'2016-02-15 15:50:59'" + "," + "1" + "," + "'2016-02-15 15:50:59'" +  ")"
        sql_str2 = u"insert into t_category (category_name, path, dimension_id, remarks, created_by, created_time, updated_by, updated_time) values (" + u"'公关'" + "," +"'/group1/M00/00/00/ezk4eVaYnViASWZnAAASzDRHZFY557.png'"+ "," + str(dimensionality_id[1][0]) + "," + u"'蓝色的旋风图片'" + "," + "1" + "," + "'2016-02-15 15:50:59'" + "," + "1" + "," + "'2016-02-15 15:50:59'" +  ")"        
        sql_str3 = u"insert into t_category (category_name, path, dimension_id, remarks, created_by, created_time, updated_by, updated_time) values (" + u"'表单'" + "," +"'/group1/M00/00/00/ezk4eVaYnRKAaySmAAARNJy_O7M768.png'"+ "," + str(dimensionality_id[2][0]) + "," + u"'红色的火灾图片'" + "," + "1" + "," + "'2016-02-15 15:50:59'" + "," + "1" + "," + "'2016-02-15 15:50:59'" +  ")"        
#         print sql_str1
#         print sql_str2
#         print sql_str3
        try:
            self.cursor.execute(sql_str1)
            self.cursor.execute(sql_str2)
            self.cursor.execute(sql_str3)
        except MySQLdb.Error, e:
            print e
#             else:
#                 print "ERROR: method add_category the category_name of " + category_name + " is already in the system"
#                 continue
        self.db.commit()
#         conf.close()

    def execSql(self,filename):
        co_str=u"mysql -h 123.57.155.12 -uhydt_bcm -phydt_bcm -Dhydt_ofdb<"+filename
        os.system(co_str)



if __name__ == '__main__':
    testData = TestData()
    testData.open_db('123.57.155.12', 'hydt_bcm', 'hydt_bcm', 'hydt_bcm')
    testData.add_root_org('root_org.csv')
    testData.add_org('org.csv')
    testData.add_user('user.csv')
    testData.add_org_user('org_user.csv')
    testData.add_role('role.csv')
    testData.add_user_role('user_role.csv')
    testData.update_manager('manager.csv')
    testData.add_role_menu('role_menu.csv')
    testData.add_role_res('role_res.csv')
    testData.add_user_shortcut_menu('user_shortcut_menu.csv')

    testData.add_dim()
    testData.get_dimension_id()
    testData.add_category()
    testData.close_db()

    testData.execSql('ofgroup.sql')

                #等手动执行完insert sql，再执行该方法
    testData.open_db('123.57.155.12', 'hydt_bcm', 'hydt_bcm', 'hydt_bcm')

    testData.add_ofmucmember('org_user.csv')

    testData.close_db()
