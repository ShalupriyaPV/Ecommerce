from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('shop', views.shop),
    path('about', views.about),
    path('style', views.style),
    path('singlepost', views.singlepost),
    path('products',views.products),
    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('productedit<int:id>',views.productedit,name='edit'),
    path('productdelete<int:id>',views.productdelete,name='delete'),
    path('signup',views.signup),
    path('login',views.loginpage,name='login'),
    path('logout',views.logoutpage,name='logoutpage'),
    path('items<int:id>',views.items,name='items'),
    path('cart',views.cart,name='cart'),
    path('viewcart', views.viewcart,name='viewcart'),
    path('cartdelete<int:id>',views.cartdelete,name='delete'),
    path('buynow',views.buynow, name='buynow'),
    path('addres', views.addres , name='addres'),
    path('addredit' , views.addredit , name='addredit'),
    path('addrdelete', views.addrdelete , name='addrdelete'),
    path('order', views.orders, name='order'),

    # path('addtocart',views.addtocart,name='addtocart'),
]

