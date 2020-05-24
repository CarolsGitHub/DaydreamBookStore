
from django.conf.urls import url
from apps.user import views
from apps.user.views import LoginView, UserInfoView, UserOrderView, AddressView, LogoutView

urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^register_handle$', views.register_handle, name='register_handle'),
    url(r'^login$', LoginView.as_view(), name='login'),
    url(r'^logout$', LogoutView.as_view(), name='logout'), # 注销登录
    url(r'^$', UserInfoView.as_view(), name='user'), # 用户中心-信息页
    url(r'^order$', UserOrderView.as_view(), name='order'), # 用户中心-订单页
    url(r'^address$', AddressView.as_view(), name='address'), # 用户中心-地址页


]
