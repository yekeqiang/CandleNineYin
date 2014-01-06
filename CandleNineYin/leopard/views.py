# Create your views here.
# -*- coding: utf-8 -*-
#from django.views.generic.list import ListView
#from CandleNineYin.leopard.models import Lineofbusiness
from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse
from CandleNineYin.leopard.models import Company,LeopardUser
from CandleNineYin.leopard.forms import ContactForm,LeopardUserForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from datetime import datetime
from django.template import Template,Context
from django.template.loader import get_template
from django.contrib import auth
from django.contrib.auth.decorators import login_required
#from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_protect
#from django.utils


def logout_view(request):
    user = request.user
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponse("%s logged out!" % user)

def register(request):
    if request.user is not None:
        logout_view(request)
    t = get_template("add_user.html")
    html = t.render(Context())
    return HttpResponse(html)

#def AddUser(request):
#    if request.method == 'POST':
#        #form = UserCreationForm(request.POST)
#        #form = LeopardUserForm(request.POST)
#        form = User.objects.create_user(request.POST)
#        #form = User.objects.create_user('ykqqiang','esperyong@gmail.com','123456')
#        #form=LeopardUser.objects.create_user(request.POST)
#
#
#
#        if form.is_active():
#            form.is_staff=True
#            new_user = form.save()
#            return render_to_response("add_user_success.html")
#        else:
#        #    #form = UserCreationForm()
#            #form = LeopardUserForm()
#            form=User.objects.create_user(request.POST)
#
#    return render_to_response("add_user.html", {
#        'form': form,
#
#    })

def createUser(request):
    if request.method == 'POST':
    #username = request
       username = request.REQUEST.get('username',None)
       #username = request.
       email = request.REQUEST.get('email',None)
       password = request.REQUEST.get('password',None)

       #TODO: check if already existed
       if username and email and password:
          u = User.objects.create_user(username,email,password)
          #if created:
             # user was created
             # set the password here
          #u.set_passwd(password)
          #else:
             # user was retrieved
             #u= User.objects.create_user(username,email,password)

       else:
          #request was empty
          #return render_to_response("add_user.html",{
          #    'username': username,
          #    'email': email,
          #    'password': password,
          #
          #
          #})
            return render_to_response("add_user.html")



    return render_to_response("add_user_success.html")

def changepwd(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    u = User.objects.get(username_exact=username)

    #newpasswd=u.set_password(request.POST.get('password'))
    newpasswd = u.ser_passwd(password)
    u.save()
    return HttpResponseRedirect('/showDashboard')


#@csrf_protect
def login(request):
    if request.user is not None:
        logout_view(request)
    t = get_template("login.html")
    html = t.render(Context())
    return HttpResponse(html)


#@csrf_protect
def account_auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    leopard_user = auth.authenticate(username=username,password=password)
    if leopard_user is not None:
        if leopard_user.is_active:
            auth.login(request,leopard_user)
            auth.login(request,leopard_user)
            return HttpResponseRedirect('/showDashboard')
        else:
            return render_to_response('login.html',{'login_err':'你的账户失效了，请联系管理人员重新激活！'})
    else:
        return render_to_response('login.html',{'login_err':'用户名或密码输入错误，请从新输入！'})


@login_required
def showDashboard(request):
    return render_to_response('index.html',{'user':request.user})


@login_required
def company_result_search(request):
    #if 'q' in request.GET and request.GET['q']:
    #    q=request.GET['q']
    #    companys = Company.objects.filter(company_name__icontains=q)
    #    return render_to_response('company_search_result.html',
    #        {'companys':companys,'query':q})
    #    #message='You searched fot: %r' % request.GET['search_company']
    #else:
    #    #message='You submitted an empty form.'
    #    #return HttpResponse('Please submit a search term')
    #    return render_to_response('search_company_form.html', {'error': True})

    #error = False
    errors=[]
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
            #error = True
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
            #error=True
        else:
            company = Company.objects.filter(company_name__icontains=q)
            return render_to_response('company_search_result.html',
                {'company': company, 'query': q})
    return render_to_response('search_company_form.html',{'errors': errors})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', '`noreply@example.com`_'),
                ['`siteowner@example.com`_'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject':'上线完成通知'}
        )
    return render_to_response('contact_form.html', {'form': form})

@login_required
def current_datetime(request):
    current_date = datetime.now()
    return render_to_response('current_datetime.html', locals())

@login_required
def homepage(request):
    return render_to_response('index.html')

@login_required
def company_list(request):
   if not request.user.is_authenticated():
        #return render_to_response('login_error.html')
        return HttpResponseRedirect('/login/?next=%s' % request.path)
   else:
        companys=Company.objects.order_by('company_name')
        return render_to_response('company_list.html',{'companys':companys})


def deployapplist(request):
    return render_to_response('deployapplist.html')