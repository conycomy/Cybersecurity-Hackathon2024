from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1:8000/api
    #path('', views.index),
    #path('', views.input_view),
    
    # 127.0.0.1:8000/api/predict
    path('predict/', views.predict, name='predict'),
]   