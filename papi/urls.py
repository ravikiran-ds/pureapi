from django.conf.urls import url
from .views import (sample,
                    StuDataDetail,
                    StuDataList,
                    StuDataPost,
                    StuDataDelete,
                    StuDataUpdate)

app_name="papi"

urlpatterns=[url(r'^$',sample,name="trial"),
            url(r'detail/(?P<id>\d+)',StuDataDetail.as_view()),
            url(r'list',StuDataList.as_view()),
            url(r'post',StuDataPost.as_view()),
            url(r'delete/(?P<id>\d+)',StuDataDelete.as_view()),
            url(r'update/(?P<id>\d+)',StuDataUpdate.as_view()),

    ]
