from.import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('login/',views.userlogin),
    path('registerpage/',views.userregister),
    path('userpage/',views.userpage),
    path('staffdetail/',views.staffdetail),
    path('viewstaff/',views.viewstaff),
    path('edit/<int:id>/',views.edit),
    path('delete/<int:id>/',views.delete),
    path('addtimetable/',views.addtimetable),
    path('viewtimetable/',views.viewtimetable),
    path('stdtimetable/',views.stdtimetable),
    path('addstaffttable/',views.addstaffttable),
    path('selectstaff/',views.selectstaff),
    path('viewstaffttable/',views.viewstaffttable),
    path('individualstaffttable/',views.individualstaffttable),
    path('useridpassword/',views.Useridpassword),
    path('viewuserid/',views.viewuserid),
    path('useridedit/<int:id>/',views.edituserid),
    path('useridelete/<int:id>/',views.deleteuserid),
    path('stafflogin/',views.stafflogin),
    path('principalpage/',views.principalpage),
    path('teacherpage/',views.teacherpage),
    path('teacherviewtimetable/',views.teacherviewtimetable),
    path('stdtimetable1/',views.stdtimetable1),
    path('teacherviewstaffttable/',views.teacherviewstaffttable),
    path('individualstaffttable1/',views.individualstaffttable1)
]
