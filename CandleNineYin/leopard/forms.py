#-*- coding: UTF-8 -*
__author__ = 'yexiaobai<yekeqiang@gmail.com>'

from django import forms
#from django.db import models
from CandleNineYin.leopard.models import *


class CompanyForm(forms.ModelForm):
    company_name = forms.CharField("company_name")



    class Meta:
        model=Company


class DepartmentForm(forms.ModelForm):
    department_name = forms.CharField("department_name")
    company_name = forms.CharField("company_name")


    class Meta:
        model=Department


class LeopardUserForm(forms.ModelForm):
    user_name = forms.CharField("user_name")
    telphone = forms.CharField("telphpne")
    email = forms.EmailField("email")
    #department_name = forms.CharField("department_name")
    #group_name=forms.CharField("group_name")
    ip=forms.CharField("ip")


    class Meta:
        model=LeopardUser


class LineofbusinessForm(forms.ModelForm):
    businesss_name = forms.CharField("business_name") #业务线表单
    businesss_desc = forms.CharField("business_desc", widget=forms.Textarea)


    class Meta:
        model=Lineofbusiness


class ProductForm(forms.ModelForm):
    product_name = forms.CharField("product_name") #产品线
    product_desc = forms.CharField("product_desc", widget=forms.Textarea)
    business_name = forms.CharField('business_name')
    product_user = forms.CharField('user_name')

    class Meta:
        model=Product

class IdcForm(forms.ModelForm):
    idc_name = forms.CharField("idc_name")

    class Meta:
        model=Idc


class JiguiForm(forms.ModelForm):
    jigui_num = forms.CharField("jigui_num")
    idc_name = forms.CharField("idc_name")

    class Meta:
        model=Jigui


class OpsystemForm(forms.ModelForm):
    ops_name = forms.CharField("ops_name")
    ops_version = forms.CharField("ops_version")

    class Meta:
        model=Opsystem


class HostForm(forms.ModelForm):
    host_name = forms.CharField("host_name")
    host_ip = forms.IPAddressField("host_ip")
    host_mac = forms.CharField("host_mac")
    idc = forms.CharField("Idc_name")
    jigui = forms.CharField("Jigui_num")
    host_mem = forms.CharField("host_mem")
    host_cpu = forms.CharField("host_cpu")
    host_disk = forms.CharField("host_disk")
    ops_version = forms.CharField("ops_version")
    ops_name = forms.CharField("osp_name")
    host_isonline = forms.BooleanField("host_isonline")
    host_isalive = forms.BooleanField("host_isalive")
    host_manager = forms.CharField("host_manager")

    class Meta:
        model=Host


class AppForm(forms.ModelForm):
    app_real_name = forms.CharField("app_real_name") #应用的部署名
    app_alis_name = forms.CharField("app_alis_name") #应用的中文别名
    app_run_path = forms.CharField("app_run_path")   #应用生产运行路径
    app_temp_backup_path = forms.CharField("app_temp_backup_path") #应用的临时备份目录
    app_nas_backup_path = forms.CharField("app_nas_backup_path")   #应用的永久备份目录
    app_mpsp_log_path = forms.CharField("app_mpsp_log_path")                 #应用的生产简单日志目录
    app_log4j_log_path = forms.CharField("app_log4j_log_path")  #应用详细日志目录
    app_nas_log_path = forms.CharField("app_nas_log_path")         #应用的备份目录
    app_isOnline = forms.BooleanField("app_isOnline")                           #应用是否在线
    app_isalive = forms.BooleanField("app_isalive")                        #应用是否存活
    app_mem_baseline = forms.CharField("app_mem_baseline", widget=forms.Textarea) #应用的内存基线指标
    app_cpu_baseline = forms.CharField("app_cpu_baseline", widget=forms.Textarea) #应用cpu基线指标
    app_tps_baseline = forms.CharField("app_tps_baseline", widget=forms.Textarea) #应用的tps性能基线指标
    app_script_path = forms.CharField("app_script_path")                   #应用脚本路径
    app_service_ip = forms.CharField("app_service_ip")                     #应用服务IP
    app_phy_ip = forms.CharField("host_ip")                                  #应用物理IP
    app_service_port = forms.CharField("app_service_port")                 #应用服务端口
    app_manager = forms.CharField("appmanager")            #应用维护者
    app_developer = forms.CharField("appdeveloper")          #应用开发者
    app_visit = forms.CharField("app_visit", widget=forms.Textarea)                         #该应用访问的IP和端口列表
    online_time = forms.DateTimeField("online_ime")  #上线时间
    change_time = forms.DateTimeField("change_time")  #变更时间

    class Meta:
        model=App


class DeployreasonForm(forms.ModelForm):
    reason_name = forms.CharField("reason_name")

    class Meta:
        model = Deployreason


class DeployappForm(forms.ModelForm):
    deploy_order = forms.CharField("deploy_order")                       #部署工单号
    deploy_name = forms.CharField("deploy_name")                         #部署工单名
    deploy_desc = forms.CharField("deploy_desc", widget=forms.Textarea)                         #工单详细说明
    deploy_type = forms.CharField("deploy_type")                         #工单类型
    deploy_user = forms.CharField("deploy_user")                               #部署人员
    developer = forms.CharField("developer")                                 #上线开发人员
    producter = forms.CharField("producter")                                 #产品人员，需求人员
    deploy_time = forms.DateTimeField("deploy_time")       #部署开始时间
    order_time = forms.DateTimeField("order_time")     #工单到达时间
    order_isdelay = forms.BooleanField("order_isdelay")                  #工单是否延迟
    order_isexam = forms.BooleanField("order_isexam")                    #工单是否特批
    order_issucess = forms.BooleanField("order_issucess")                #上线是否成功
    order_failreason = forms.CharField("order_failreason", widget=forms.Textarea)               #上线失败原因
    exam_user = forms.CharField("exam_user", widget=forms.Textarea)                               #特批人员列表
    order_istest = forms.BooleanField("order_istest")                    #工单是否测试
    exam_report = forms.CharField("exam_report", widget=forms.Textarea)                         #特批说明
    deploy_time_consum = forms.CharField("deploy_time_consum")           #上线耗时
    company = forms.CharField("company_name")                                #工单所属公司
    lineofbusiness = forms.CharField("business_name")                  #工单所属业务线
    product = forms.CharField("product_name")                                #工单所属产品
    deploy_applist = forms.CharField("deploy_applist", widget=forms.Textarea)                   #应用部署列表
    deploy_emaillist = forms.CharField("deploy_emaillist", widget=forms.Textarea)               #上线成功后，邮件发送列表
    deploy_phonelist = forms.CharField("deploy_phonelist", widget=forms.Textarea)               #上线成功后，短信发送列表
    deploy_isdiff = forms.BooleanField("deploy_isdiff")                  #上线是否产生差异
    deploy_diffdesc = forms.CharField("deploy_diffdesc")                 #上线差异的详细描述
    app_isadd = forms.BooleanField("app_isadd")                          #上线是否新增应用
    app_addlist = forms.CharField("app_addlist", widget=forms.Textarea)                         #新增应用清单
    app_isword = forms.BooleanField("app_isword")                        #是否有部署文档
    app_isbackup = forms.BooleanField("app_isbackup")                    #是否应用备份
    app_islogbackup = forms.BooleanField("app_islogbackup")              #日志是否备份
    busi_isaffect = forms.BooleanField("busi_isaffect")                  #是否影响业务
    busi_affecttime = forms.CharField("busi_affecttime")                 #业务影响时间
    deploy_timedesc = forms.CharField("deploy_timedesc", widget=forms.Textarea)                 #部署耗时太多说明
    app_maintainmanual = forms.BooleanField("app_maintainmanual")        #是否有维护文档
    deploy_busilist = forms.CharField("deploy_busilist")                 #上线涉及业务

    class Meta:
        model = Deployapp

class ContactForm(forms.ModelForm):
    subject = forms.CharField(max_length=200)
    email = forms.EmailField(required=False,label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message=self.cleaned_data['message']
        num_words=len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")

    class Meta:
        model = Contact

