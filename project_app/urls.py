from django.urls import path
from . import views

urlpatterns=[
    path('',views.default,name="default"),
    path('form/',views.form,name="form"),
    path('insertData/',views.insertData,name="form"),
    path("dbConnection/",views.dbConnectionTest,name="dbTest"),
    path("10001/",views.processSeries10001,name="10001"),
    path("allData/",views.processAllDatapoints,name="allData")
]