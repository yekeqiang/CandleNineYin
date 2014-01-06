#-*- coding: UTF-8 -*
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.contrib.auth.models import User,Group,GroupManager
# Create your models here.



class Company(models.Model):
    company_name=models.CharField("company_name",unique=True,db_index=True,max_length=100)

    class Meta:
        ordering=['company_name']

    def __unicode__(self):
        return self.company_name





class Department(models.Model):
    department_name=models.CharField("department_name",unique=True,db_index=True,max_length=100)
    company=models.ForeignKey(Company,null=True,blank=True)

    class Meta:
        ordering=['department_name']

    def __unicode__(self):
        return self.department_name




class LeopardGroup(models.Model):
    #group_name = models.CharField(max_length=50,unique=True)
    group=models.ForeignKey(Group,null=True)
    group_name=models.CharField("group_name",max_length=100)

    def __unicode__(self):
        return self.group_name




class Idc(models.Model):
    idc_name=models.CharField("idc_name",max_length=50,unique=True)
    def __unicode__(self):
        return self.idc_name

class IP(models.Model):
    hostname=models.CharField(max_length=50, unique=True)
    ip = models.IPAddressField(unique=True)
    idc = models.ForeignKey(Idc, null=True, blank=True)
    group = models.ManyToManyField(Group, null=True, blank=True)
    port = models.IntegerField(default='22')
    os = models.CharField(max_length=20, default='linux', verbose_name='Operating System')

    #snmp related
    alert_limit = models.IntegerField(default=5)
    snmp_alert_limit = models.IntegerField(default=5)
    asset_collection = models.BooleanField(default=True,verbose_name='enable asset collection')
    status_monitor_on = models.BooleanField(default=True)
    snmp_on = models.BooleanField(default=True)
    snmp_version = models.CharField(max_length=10,default='2c')
    snmp_community_name = models.CharField(max_length=50,default='public')
    snmp_security_level = models.CharField(max_length=50,default='auth')
    snmp_auth_protocol = models.CharField(max_length=50,default='MD5')
    snmp_user = models.CharField(max_length=50,default='triaquae_snmp')
    snmp_pass = models.CharField(max_length=50,default='my_pass')

    system_load_warning = models.IntegerField(default=0,blank=True,verbose_name="load >")
    system_load_critical = models.IntegerField(default=0,blank=True)
    cpu_idle_warning = models.IntegerField(default=0,blank=True, verbose_name = "cpuIdle% < ")
    cpu_idle_critical= models.IntegerField(default=0,blank=True)
    mem_usage_warning = models.IntegerField(default=0,blank=True, verbose_name="memoryUsage% >")
    mem_usage_critical = models.IntegerField(default=0,blank=True)
    def __unicode__(self):
        return self.ip


class LeopardUser(models.Model):

    USER_STATUS = (
      (0, "active"),
      (1, "deactive"),
    )
    #user=models.CharField("user_name",unique=True,db_index=True,max_length=100)
    user = models.ForeignKey(User,null=True)
    user_name=models.CharField("user_name",max_length=100)
    first_name=models.CharField("first_name",max_length=100)
    last_name=models.CharField("last_name",max_length=100)
    telphone=models.CharField("telphone",max_length=20,default='Null')
    email=models.EmailField()
    department=models.ManyToManyField(Department,null=True,blank=True)
    group=models.ManyToManyField(LeopardGroup,null=True,blank=True)
    #ip = models.ManyToManyField(IP,null=True,blank=True)
    ip=models.CharField("ip",max_length=50)
    user_status=models.IntegerField(choices=USER_STATUS,default=0)
    def __unicode__(self):
        return '%s' % self.user

class LeopardUserAdmin(admin.ModelAdmin):
    list_display = ('user_name','first_name','last_name','telphone',
                    'email','ip','user_status')
    list_filter = ('user_name',)
    filter_horizontal = ('department',)


class CustomUser(models.Model):
    user_name=models.CharField("user_name",max_length=100)
    email=models.EmailField()
    telphone=models.CharField("telphone",max_length=20,default='Null')



class Lineofbusiness(models.Model):
    businesss_name=models.CharField("business_name",unique=True,db_index=True,max_length=200) #业务线
    businesss_desc=models.CharField("business_desc",max_length=800,default='Null')

    def __unicode__(self):
        return self.businesss_name





class Product(models.Model):
    product_name=models.CharField("product_name",unique=True,db_index=True,max_length=200) #产品线
    product_desc=models.CharField("product_desc",max_length=800,default='Null')
    business=models.ForeignKey('Lineofbusiness',null=True,blank=True)
    product_user=models.ManyToManyField(LeopardUser,null=True,blank=True)

    def __unicode__(self):
        return self.product_name







class Jigui(models.Model):
    jigui_num=models.CharField("jigui_num",max_length=50)
    idc_name=models.ForeignKey(Idc,null=True,blank=True)


class Opsystem(models.Model):
    ops_name=models.CharField("ops_name",max_length=500)
    ops_version=models.CharField("ops_version",max_length=500)

    #def __unicode__(self):
    #    return u'%s-%s' % (self.ops_name, self.ops_version) #原因为不能把字典转换成string的错误
#



class Host(models.Model):
    host_name=models.CharField("host_name",unique=True,db_index=True,max_length=200)
    host_ip=models.IPAddressField("host_ip",unique=True,db_index=True)
    host_mac=models.CharField("host_mac",unique=True,max_length=250)
    idc=models.ForeignKey(Idc, null=True, blank=True)
    jigui=models.ForeignKey(Jigui,null=True,blank=True)
    host_mem=models.CharField("host_mem",max_length=1000)
    host_cpu=models.CharField("host_cpu",max_length=1000)
    host_disk=models.CharField("host_disk",max_length=2000)
    ops_version=models.ForeignKey(Opsystem,null=True,blank=True,related_name='opsversion')
    ops_name=models.ForeignKey(Opsystem,null=True,blank=True,related_name='opsname')
    host_isonline=models.BooleanField("host_isonline")
    host_isalive=models.BooleanField("host_isalive")
    create_time=models.DateTimeField("create_time",auto_created=True)
    modified_time=models.DateTimeField(default=datetime.now)
    host_manager=models.ManyToManyField(LeopardUser,null=True,blank=True)


    class Meta:
        ordering=['modified_time']



    def __unicode__(self):
        return  self.host_name





class App(models.Model):
   #
   #APP_STATUS = (
   #   (0, "running"),
   #   (1, "deading"),
   #)
   #
   #APP_ONLINE_STATUS = (
   #    (0,"online"),
   #    (1,"offline"),
   #)

    app_real_name=models.CharField("app_real_name",unique=True,db_index=True,max_length=200) #应用的部署名
    app_alis_name=models.CharField("app_alis_name",max_length=500) #应用的中文别名
    app_run_path=models.CharField("app_run_path",max_length=500)   #应用生产运行路径
    app_temp_backup_path=models.CharField("app_temp_backup_path",max_length=1000) #应用的临时备份目录
    app_nas_backup_path=models.CharField("app_nas_backup_path",max_length=2000)   #应用的永久备份目录
    app_mpsp_log_path=models.CharField("app_mpsp_log_path",max_length=2000)                 #应用的生产简单日志目录
    app_log4j_log_path=models.CharField("app_log4j_log_path",max_length=2000)  #应用详细日志目录
    app_nas_log_path=models.CharField("app_nas_log_path",max_length=2000)         #应用的备份目录
    app_isOnline=models.BooleanField("app_isOnline")                           #应用是否在线
    app_isalive=models.BooleanField("app_isalive")                        #应用是否存活
    app_mem_baseline=models.CharField("app_mem_baseline",max_length=1000) #应用的内存基线指标
    app_cpu_baseline=models.CharField("app_cpu_baseline",max_length=1000) #应用cpu基线指标
    app_tps_baseline=models.CharField("app_tps_baseline",max_length=1000) #应用的tps性能基线指标
    app_script_path=models.TextField("app_script_path",max_length=1000)                   #应用脚本路径
    app_service_ip=models.CharField("app_service_ip",max_length=300)                     #应用服务IP
    app_phy_ip=models.ForeignKey("Host",null=True,blank=True)                                  #应用物理IP
    app_service_port=models.CharField("app_service_port",max_length=300)                 #应用服务端口
    app_manager=models.ManyToManyField(LeopardUser,null=True,blank=True,related_name='appmanager')            #应用维护者
    app_developer=models.ManyToManyField(LeopardUser,null=True,blank=True,related_name='appdeveloper')          #应用开发者
    app_visit=models.CharField("app_visit",max_length=1000)                         #该应用访问的IP和端口列表
    online_time=models.DateTimeField("online_ime", auto_now=True)  #上线时间
    change_time=models.DateTimeField("change_time", auto_now=True)  #变更时间
    deploy_count=models.IntegerField("deploy_count")

    class Meta:
        ordering=['change_time']

    def __unicode__(self):
        return self.app_real_name





class Deployreason(models.Model):
    reason_name=models.CharField("reason_name",max_length=600)




class Deployapp(models.Model):
    deploy_order=models.CharField("deploy_order",unique=True,db_index=True,max_length=200)                        #部署工单号
    deploy_name=models.CharField("deploy_name",unique=True,db_index=True,max_length=250)                         #部署工单名
    deploy_desc=models.TextField("deploy_desc",max_length=3000)                         #工单详细说明
    deploy_type=models.CharField("deploy_type",max_length=3000)                         #工单类型
    deploy_user=models.ForeignKey(LeopardUser,null=True,blank=True,related_name='deploy_user')                               #部署人员
    developer=models.ManyToManyField(LeopardUser,null=True,blank=True,related_name='developer')                                 #上线开发人员
    producter=models.ManyToManyField(LeopardUser,null=True,blank=True,related_name='producter')                                 #产品人员，需求人员
    deploy_time=models.DateTimeField("deploy_time",auto_now=True)       #部署开始时间
    order_time=models.DateTimeField("order_time",auto_created=True)     #工单到达时间
    modified_time=models.DateTimeField(auto_created=True)               #修改时间工单
    order_isdelay=models.BooleanField("order_isdelay")                  #工单是否延迟
    order_isexam=models.BooleanField("order_isexam")                    #工单是否特批
    order_issucess=models.BooleanField("order_issucess")                #上线是否成功
    fail_reason=models.ManyToManyField(Deployreason,null=True,blank=True)  #上线失败原因分类
    order_failreason=models.TextField("order_failreason")               #上线失败详细原因
    exam_user=models.CharField("exam_user",max_length=256)                               #特批人员列表
    order_istest=models.BooleanField("order_istest")                    #工单是否测试
    exam_report=models.TextField("exam_report",max_length=3000)                         #特批说明
    deploy_time_consum=models.CharField("deploy_time_consum",max_length=3000)           #上线耗时
    company=models.ForeignKey("Company",null=True,blank=True)                                #工单所属公司
    lineofbusiness=models.ManyToManyField(Lineofbusiness,null=True,blank=True)                  #工单所属业务线
    product=models.ManyToManyField(Product,null=True,blank=True)                                #工单所属产品
    deploy_applist=models.TextField("deploy_applist",max_length=5000)                   #应用部署列表
    deploy_emaillist=models.TextField("deploy_emaillist",max_length=5000)               #上线成功后，邮件发送列表
    deploy_phonelist=models.TextField("deploy_phonelist",max_length=5000)               #上线成功后，短信发送列表
    deploy_isdiff=models.BooleanField("deploy_isdiff")                  #上线是否产生差异
    deploy_diffdesc=models.TextField("deploy_diffdesc",max_length=5000)                 #上线差异的详细描述
    app_isadd=models.BooleanField("app_isadd")                          #上线是否新增应用
    app_addlist=models.CharField("app_addlist",max_length=3000)                         #新增应用清单
    app_isword=models.BooleanField("app_isword")                        #是否有部署文档
    app_isbackup=models.BooleanField("app_isbackup")                    #是否应用备份
    app_islogbackup=models.BooleanField("app_islogbackup")              #日志是否备份
    busi_isaffect=models.BooleanField("busi_isaffect")                  #是否影响业务
    busi_affecttime=models.CharField("busi_affecttime",max_length=100)                 #业务影响时间
    deploy_timedesc=models.TextField("deploy_timedesc",max_length=3000)                 #部署耗时太多说明
    app_maintainmanual=models.BooleanField("app_maintainmanual")        #是否有维护文档
    deploy_busilist=models.TextField("deploy_busilist",max_length=3000)                 #上线涉及业务

    class Meta:
        ordering=['modified_time']



class Contact(models.Model):
    subject=models.CharField('subject',max_length=1000)
    email=models.EmailField('email',max_length=500,default='Null')
    message = models.TextField('message')



#将models加入到admin管理中
admin.site.register(LeopardUser,LeopardUserAdmin)
admin.site.register(Host)
admin.site.register(App)
admin.site.register(Department)
admin.site.register(Lineofbusiness)
admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Opsystem)
admin.site.register(Idc)
admin.site.register(Jigui)
admin.site.register(Deployapp)
admin.site.register(Group)
admin.site.register(Deployreason)
admin.site.register(IP)
#admin.site.register(Contact)




