from django.urls import path
from api.views import PostList,PostDetail,Customerdetail,CustomerdetailList
# from django.views.generic import TemplateView

app_name="api"
urlpatterns =[
    path("<int:pk>/",PostDetail.as_view(),name="detailcreate"),
    path("",PostList.as_view(),name="listcreate"),
    path("customer/<int:pk>",Customerdetail.as_view(),name="customer_list"),
    path("customer/",CustomerdetailList.as_view(),name="customer_list_user"),
    # path("<slug:>/",PostDetail.as_view(),name="detailcreate"),
    # path("",TemplateView.as_view(template_name="api/index.html")),
]
