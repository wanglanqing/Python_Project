# coding:utf8
from flask import Flask,jsonify,request,render_template,url_for
import requests
from get_act import *
from create_template import *

app = Flask(__name__)

@app.route('/actinfo/',methods=['POST','GET'])
def show():
    title=u'测试结果展示'
    res = {}
    if request.method=='GET':
        print 1111111111
    else:
        # ids = request.form.getlist('adzoneIds')
        # ids = request.args.get('adzoneIds')

        # ids = request.values.get('adzoneIds')
        ids = request.form.get('adzoneIds')
        print(ids.split(','))
        if len(ids) != 0:
            res_re = get_ad_simulation_info(ids.split(','))
    return  render_template("show_re.html",res=res_re, title=title)

@app.route('/create_act/', methods=['POST','GET'])
def create_act():
    if request.method=='GET':
        print 1111111111
        return render_template("create_act.html", template_adr='1111')
    else:
        template_adr= request.form.get('template_adr')
        css_adr="'" + request.form.get('css_adr') + "'"
        template_type_name=request.form.get('template_type_name')
        temlate_name=request.form.get('temlate_name')
        act_name=request.form.get('act_name')
        # 为模板类型名称
        ct = Create_template_act(template_type_name, act_name)
        # 创建模板类型，create_template_type(self, classifi, locationAdress, preview="https://img0.adhudong.com/template/201802/24/999337a35a1a9169450685cc66560a05.png",prizesNum=6)
        # ct.create_template_type(template_adr)
        # 创建模板 ct.create_template(templateName, templateStyleUrl)
        # ct.create_template(temlate_name, css_adr)
        # 创建活动，create_act(self, act_name,free_num=20, award_num=6)
        ct.create_act()
        # 创建活动关联的奖品，
        ct.create_awards()
        # ct.get_templateId()
        return render_template("create_act.html",template_adr=temlate_name)
    pass


if __name__ == '__main__':
    app.run( host="0.0.0.0", port=9000, debug=True)