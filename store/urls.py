from django.urls import path
from . import views
urlpatterns=[
    path('home',views.home),
    path('login',views.login),
    path('log',views.log),
    path('signup',views.signup),
    path('sig',views.sig),
    path('delete',views.delete),
    path('del/<int:id>',views.dele),
    path('about',views.about),
    path('categories',views.categories),
    path('best',views.best),
    path('contact',views.contact),
    path('author',views.authors),
    path('au',views.au),
    path('disp',views.disp),
    path('delet/<int:id>',views.delet),
    path('shop',views.shop),
    path('hop',views.hop),
    path('boo',views.boo),
    path('remove/<int:id>',views.remove),
    path('cart',views.car),
    path('buy',views.buy),
    path('admin',views.admin),
    
]