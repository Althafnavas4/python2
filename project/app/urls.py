from django.urls import path
from . import views

urlpatterns=[
    path('fun1',views.fun1),
    path('fun2/<int:a>/<int:b>',views.fun2),
    path('task/<int:salary>/<int:year>',views.task),
    path('task1/<city>',views.task1),
    path('task2/<int:num>',views.task2),
    path('task3/<day>',views.task3),
    path('task4/<int:cost>',views.task4),
    path('task5/<int:unit>',views.task5),
    path('demo',views.demo),
    path('display',views.display),
    path('user_reg',views.user_reg),
]