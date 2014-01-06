from django.conf.urls import patterns, include, url
from CandleNineYin.leopard.views import *
#from CandleNineYin.leopard.contact import contact
#from leopard import contact
#from CandleNineYin. import

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'CandleNineYin.views.home', name='home'),
    #url(r'^CandleNineYin/', include('CandleNineYin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',login),
    url(r'^login/', login),
    url(r'^register/', register),
    url(r'^adduser/',createUser),
    url(r'^deployapplist/', deployapplist),
    #url(r'^$', homepage),
    url('^index/$', account_auth),
    url('^showDashboard$', showDashboard),
    url(r'^search-company-form/', company_result_search),
    url(r'^company-result/', company_result_search),
    url(r'^contact_form/', contact),
    url(r'current_datatime/', current_datetime),
    url(r'company_list/', company_list),
        #url(r'^adduser/', AddUser),

)
