from  django.urls import path
from .views import GetSensorDataView,RetrieveDataView,QueryData
 
urlpatterns=[
    path("getdata",GetSensorDataView.as_view(),name="sensor-data"),
    path("listdata",RetrieveDataView.as_view(),name="data-list"),
    path("querydata/<date_created>",QueryData.as_view(),name="querydata")
]