from django.urls import path
from .import views
app_name='storeapp'
urlpatterns = [
    path('',views.dept,name='dept'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('new/',views.new,name='new'),
    path('order/',views.order,name='order'),
    path('logout/',views.logout,name='logout'),
    path('confirm/',views.confirm,name='confirm'),
    path('<slug:c_slug>/',views.dept,name='products_by_department'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodetail')
]