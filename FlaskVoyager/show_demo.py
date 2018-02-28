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
    return  render_template("show_re.html",res=res, title=title)

@app.route('/create_act/', methods=['POST','GET'])
def create_act():
    if request.method=='GET':
        print 1111111111
    else:
        template_adr=requests.get('template_adr')
        css_adr=requests.get('css_adr')
        template_type_name=requests.get('template_type_name')
        temlate_name=requests.get('temlate_name')
        act_name=requests.get('act_name')
        print(template_adr)
    return render_template("create_act.html",res='ok' )
    pass


if __name__ == '__main__':
    app.run( host="0.0.0.0", port=9000, debug=True)