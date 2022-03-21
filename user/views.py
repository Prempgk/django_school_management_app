from django.shortcuts import render,redirect,HttpResponse
from .models import user_details,loggedinperson,staffdetails,std1,std2,std3,std4,std5,std6,std7,std8,std9,std10,std11,std12,cstduse,mondaystafftimetable,ssprocess,tuesdaystafftimetable,wednesdaystafftimetable,thursdaystafftimetable,fridaystafftimetable,saturdaystafftimetable,cstaffuse,useridpassword,currentloginstaff
# Create your views here.


def individualstaffttable1(request):
    a = loggedinperson.objects.get(id=1)
    b = a.logged_id
    c = user_details.objects.get(username=b)
    d = c.School_name
    x = cstaffuse.objects.get(id=1)
    if request.method=='POST':
        day=request.POST.get('day')
        if day=='Monday':
            m1=mondaystafftimetable.objects.filter(monday1=x.cstaff)
            m2=mondaystafftimetable.objects.filter(monday2=x.cstaff)
            m3=mondaystafftimetable.objects.filter(monday3=x.cstaff)
            m4 = mondaystafftimetable.objects.filter(monday4=x.cstaff)
            m5 = mondaystafftimetable.objects.filter(monday5=x.cstaff)
            m6 = mondaystafftimetable.objects.filter(monday6=x.cstaff)
            m7 = mondaystafftimetable.objects.filter(monday7=x.cstaff)
            m8 = mondaystafftimetable.objects.filter(monday8=x.cstaff)
            return render(request,'individualstaffttable1.html',{'a':x,'p1':m1,'p2':m2,'p3':m3,'p4':m4,'p5':m5,'p6':m6,'p7':m7,'p8':m8})
        if day=='Tuesday':
            m1=tuesdaystafftimetable.objects.filter(tuesday1=x.cstaff)
            m2=tuesdaystafftimetable.objects.filter(tuesday2=x.cstaff)
            m3=tuesdaystafftimetable.objects.filter(tuesday3=x.cstaff)
            m4 = tuesdaystafftimetable.objects.filter(tuesday4=x.cstaff)
            m5 = tuesdaystafftimetable.objects.filter(tuesday5=x.cstaff)
            m6 = tuesdaystafftimetable.objects.filter(tuesday6=x.cstaff)
            m7 = tuesdaystafftimetable.objects.filter(tuesday7=x.cstaff)
            m8 = tuesdaystafftimetable.objects.filter(tuesday8=x.cstaff)
            return render(request,'individualstaffttable1.html',{'a':x,'p1':m1,'p2':m2,'p3':m3,'p4':m4,'p5':m5,'p6':m6,'p7':m7,'p8':m8})
        if day=='Wednesday':
            m1=wednesdaystafftimetable.objects.filter(wednesday1=x.cstaff)
            m2=wednesdaystafftimetable.objects.filter(wednesday2=x.cstaff)
            m3=wednesdaystafftimetable.objects.filter(wednesday3=x.cstaff)
            m4 = wednesdaystafftimetable.objects.filter(wednesday4=x.cstaff)
            m5 = wednesdaystafftimetable.objects.filter(wednesday5=x.cstaff)
            m6 = wednesdaystafftimetable.objects.filter(wednesday6=x.cstaff)
            m7 = wednesdaystafftimetable.objects.filter(wednesday7=x.cstaff)
            m8 = wednesdaystafftimetable.objects.filter(wednesday8=x.cstaff)
            return render(request,'individualstaffttable1.html',{'a':x,'p1':m1,'p2':m2,'p3':m3,'p4':m4,'p5':m5,'p6':m6,'p7':m7,'p8':m8})
        if day=='Thursday':
            m1=thursdaystafftimetable.objects.filter(thursday1=x.cstaff)
            m2=thursdaystafftimetable.objects.filter(thursday2=x.cstaff)
            m3=thursdaystafftimetable.objects.filter(thursday3=x.cstaff)
            m4 = thursdaystafftimetable.objects.filter(thursday4=x.cstaff)
            m5 = thursdaystafftimetable.objects.filter(thursday5=x.cstaff)
            m6 = thursdaystafftimetable.objects.filter(thursday6=x.cstaff)
            m7 = thursdaystafftimetable.objects.filter(thursday7=x.cstaff)
            m8 = thursdaystafftimetable.objects.filter(thursday8=x.cstaff)
            return render(request,'individualstaffttable1.html',{'a':x,'p1':m1,'p2':m2,'p3':m3,'p4':m4,'p5':m5,'p6':m6,'p7':m7,'p8':m8})
        if day=='Friday':
            m1=fridaystafftimetable.objects.filter(friday1=x.cstaff)
            m2=fridaystafftimetable.objects.filter(friday2=x.cstaff)
            m3=fridaystafftimetable.objects.filter(friday3=x.cstaff)
            m4 = fridaystafftimetable.objects.filter(friday4=x.cstaff)
            m5 = fridaystafftimetable.objects.filter(friday5=x.cstaff)
            m6 = fridaystafftimetable.objects.filter(friday6=x.cstaff)
            m7 = fridaystafftimetable.objects.filter(friday7=x.cstaff)
            m8 = fridaystafftimetable.objects.filter(friday8=x.cstaff)
            return render(request,'individualstaffttable1.html',{'a':x,'p1':m1,'p2':m2,'p3':m3,'p4':m4,'p5':m5,'p6':m6,'p7':m7,'p8':m8})
        if day=='Saturday':
            m1=saturdaystafftimetable.objects.filter(saturday1=x.cstaff)
            m2=saturdaystafftimetable.objects.filter(saturday2=x.cstaff)
            m3=saturdaystafftimetable.objects.filter(saturday3=x.cstaff)
            m4 = saturdaystafftimetable.objects.filter(saturday4=x.cstaff)
            m5 = saturdaystafftimetable.objects.filter(saturday5=x.cstaff)
            m6 = saturdaystafftimetable.objects.filter(saturday6=x.cstaff)
            m7 = saturdaystafftimetable.objects.filter(saturday7=x.cstaff)
            m8 = saturdaystafftimetable.objects.filter(saturday8=x.cstaff)
            return render(request,'individualstaffttable1.html',{'a':x,'p1':m1,'p2':m2,'p3':m3,'p4':m4,'p5':m5,'p6':m6,'p7':m7,'p8':m8})

    return render(request,'individualstaffttable1.html',{'a':x})


def teacherviewstaffttable(request):
    a = loggedinperson.objects.get(id=1)
    b = a.logged_id
    c = user_details.objects.get(username=b)
    d = c.School_name
    det = staffdetails.objects.filter(schoolname=d)
    if request.method=='POST':
        staff=request.POST.get('content')
        x=cstaffuse.objects.get(id=1)
        x.cstaff=staff
        x.save()
        return redirect('/individualstaffttable1/',individualstaffttable1)

    return render(request,'viewstaffttable.html',{'value':det})


def stdtimetable1(request):
    a=loggedinperson.objects.get(id=1)
    b=a.logged_id
    c=user_details.objects.get(username=b)
    d=c.School_name
    e=cstduse.objects.get(id=1)
    f=e.current_standard
    if f=='1st standard':
        x=std1.objects.filter(school_name=d)
        return render(request, 'stdtimetable1.html', {'values': x,'head':e})
    elif f=='2nd standard':
        x=std2.objects.filter(school_name=d)
        return render(request, 'stdtimetable1.html', {'values': x,'head':e})
    elif f=='3rd standard':
        x=std3.objects.filter(school_name=d)
        return render(request, 'stdtimetable1.html', {'values': x,'head':e})
    elif f=='4th standard':
        x=std4.objects.filter(school_name=d)
        return render(request, 'stdtimetable1.html', {'values': x,'head':e})
    elif f=='5th standard':
        x=std5.objects.filter(school_name=d)
        return render(request, 'stdtimetable1.html', {'values': x,'head':e})
    elif f=='6th standard':
        x=std6.objects.filter(school_name=d)
        return render(request, 'stdtimetable1.html', {'values': x,'head':e})
    elif f=='7th standard':
        x=std7.objects.filter(school_name=d)
        return render(request, 'stdtimetable1.html', {'values': x,'head':e})
    elif f=='8th standard':
        x=std8.objects.filter(school_name=d)
        return render(request, 'stdtimetable1.html', {'values': x,'head':e})
    elif f=='9th standard':
        x=std9.objects.filter(school_name=d)
        return render(request, 'stdtimetable1.html', {'values': x,'head':e})
    elif f=='10th standard':
        x=std10.objects.filter(school_name=d)
        return render(request, 'stdtimetable1.html', {'values': x,'head':e})
    elif f=='11th standard':
        x= std11.objects.filter(school_name=d)
        return render(request, 'stdtimetable1.html', {'values': x,'head':e})
    elif f=='12th standard':
        x=std12.objects.filter(school_name=d)
        return render(request, 'stdtimetable1.html', {'values': x,'head':e})


def teacherviewtimetable(request):
    if request.method=='POST':
        a=request.POST.get('content')
        b=cstduse.objects.get(id=1)
        b.current_standard=a
        b.save()
        return redirect('/stdtimetable1/',stdtimetable1)


    return render(request,'viewtimetable.html')

def teacherpage(request):
    if request.method=='POST':
        a=request.POST.get('content')
        if a=='View Timetable Subject Wise':
            return redirect('/teacherviewtimetable/',teacherviewtimetable)
        elif a=='View Timetable Staff Wise':
            return redirect('/teacherviewstaffttable/',teacherviewstaffttable)
    return render(request,'teacherpage.html')


def principalpage(request):
    if request.method=='POST':
        a=request.POST.get('content')
        if a=='Add Timetable Subject wise':
            return redirect('/addtimetable/',addtimetable)
        elif a=='View Timetable Subject Wise':
            return redirect('/viewtimetable/',viewtimetable)
        elif a=='Add Timetable Staff Wise':
            return redirect('/addstaffttable/',addstaffttable)
        elif a=='View Timetable Staff Wise':
            return redirect('/viewstaffttable/',viewstaffttable)

    return render(request,'principalpage.html')


def stafflogin(request):
    if request.method=='POST':
        userid=request.POST.get('userid')
        password=request.POST.get('password')
        a=currentloginstaff.objects.get(id=1)
        try:
            useridpassword.objects.get(role_id=userid,password=password)
            a.userid=userid
            a.password=password
            a.save()
            x=useridpassword.objects.get(role='Principal')
            y=useridpassword.objects.get(role='Vice Principal')
            if userid == x.role_id:
                return redirect('/principalpage/',principalpage)
            elif userid == y.role_id:
                return redirect('/principalpage/', principalpage)
            else:
                return redirect('/teacherpage/',teacherpage)
        except:
            return render(request,'stafflogin.html',{'a':True})
    return render(request,'stafflogin.html')


def deleteuserid(request,id):
    det=useridpassword.objects.filter(id=id).delete()
    return redirect('/viewuserid/',viewuserid)

def edituserid(request,id):
    det=useridpassword.objects.get(id=id)
    if request.method=='POST':
        det.role_id=request.POST.get('roleid')
        det.password=request.POST.get('password')
        det.save()
        return redirect('/viewuserid/', viewuserid)
    return render(request,'edituseridpassword.html',{'a':det})

def viewuserid(request):
    b = loggedinperson.objects.get(id=1)
    c = b.logged_id
    d = user_details.objects.get(username=c)
    a=useridpassword.objects.filter(schoolname=d.School_name)
    return render(request,'viewuseridpassword.html',{'value':a})


def Useridpassword(request):
    b = loggedinperson.objects.get(id=1)
    c = b.logged_id
    d = user_details.objects.get(username=c)
    if request.method=='POST':
        role=request.POST.get('role')
        roleid =request.POST.get('userid')
        crpassword=request.POST.get('create password')
        copassword=request.POST.get('confirm password')
        if copassword == crpassword:
            a = useridpassword()
            a.role = role
            a.role_id = roleid
            a.password = copassword
            a.schoolname = d.School_name
            a.save()
            return redirect('/viewuserid/',viewuserid)
        else:
            return render(request,'useridpassword.html',{'a':True})
    return render(request,'useridpassword.html')


def individualstaffttable(request):
    a = loggedinperson.objects.get(id=1)
    b = a.logged_id
    c = user_details.objects.get(username=b)
    d = c.School_name
    x = cstaffuse.objects.get(id=1)
    if request.method=='POST':
        day=request.POST.get('day')
        if day=='Monday':
            m1=mondaystafftimetable.objects.filter(monday1=x.cstaff)
            m2=mondaystafftimetable.objects.filter(monday2=x.cstaff)
            m3=mondaystafftimetable.objects.filter(monday3=x.cstaff)
            m4 = mondaystafftimetable.objects.filter(monday4=x.cstaff)
            m5 = mondaystafftimetable.objects.filter(monday5=x.cstaff)
            m6 = mondaystafftimetable.objects.filter(monday6=x.cstaff)
            m7 = mondaystafftimetable.objects.filter(monday7=x.cstaff)
            m8 = mondaystafftimetable.objects.filter(monday8=x.cstaff)
            return render(request,'individualstaffttable.html',{'a':x,'p1':m1,'p2':m2,'p3':m3,'p4':m4,'p5':m5,'p6':m6,'p7':m7,'p8':m8})
        if day=='Tuesday':
            m1=tuesdaystafftimetable.objects.filter(tuesday1=x.cstaff)
            m2=tuesdaystafftimetable.objects.filter(tuesday2=x.cstaff)
            m3=tuesdaystafftimetable.objects.filter(tuesday3=x.cstaff)
            m4 = tuesdaystafftimetable.objects.filter(tuesday4=x.cstaff)
            m5 = tuesdaystafftimetable.objects.filter(tuesday5=x.cstaff)
            m6 = tuesdaystafftimetable.objects.filter(tuesday6=x.cstaff)
            m7 = tuesdaystafftimetable.objects.filter(tuesday7=x.cstaff)
            m8 = tuesdaystafftimetable.objects.filter(tuesday8=x.cstaff)
            return render(request,'individualstaffttable.html',{'a':x,'p1':m1,'p2':m2,'p3':m3,'p4':m4,'p5':m5,'p6':m6,'p7':m7,'p8':m8})
        if day=='Wednesday':
            m1=wednesdaystafftimetable.objects.filter(wednesday1=x.cstaff)
            m2=wednesdaystafftimetable.objects.filter(wednesday2=x.cstaff)
            m3=wednesdaystafftimetable.objects.filter(wednesday3=x.cstaff)
            m4 = wednesdaystafftimetable.objects.filter(wednesday4=x.cstaff)
            m5 = wednesdaystafftimetable.objects.filter(wednesday5=x.cstaff)
            m6 = wednesdaystafftimetable.objects.filter(wednesday6=x.cstaff)
            m7 = wednesdaystafftimetable.objects.filter(wednesday7=x.cstaff)
            m8 = wednesdaystafftimetable.objects.filter(wednesday8=x.cstaff)
            return render(request,'individualstaffttable.html',{'a':x,'p1':m1,'p2':m2,'p3':m3,'p4':m4,'p5':m5,'p6':m6,'p7':m7,'p8':m8})
        if day=='Thursday':
            m1=thursdaystafftimetable.objects.filter(thursday1=x.cstaff)
            m2=thursdaystafftimetable.objects.filter(thursday2=x.cstaff)
            m3=thursdaystafftimetable.objects.filter(thursday3=x.cstaff)
            m4 = thursdaystafftimetable.objects.filter(thursday4=x.cstaff)
            m5 = thursdaystafftimetable.objects.filter(thursday5=x.cstaff)
            m6 = thursdaystafftimetable.objects.filter(thursday6=x.cstaff)
            m7 = thursdaystafftimetable.objects.filter(thursday7=x.cstaff)
            m8 = thursdaystafftimetable.objects.filter(thursday8=x.cstaff)
            return render(request,'individualstaffttable.html',{'a':x,'p1':m1,'p2':m2,'p3':m3,'p4':m4,'p5':m5,'p6':m6,'p7':m7,'p8':m8})
        if day=='Friday':
            m1=fridaystafftimetable.objects.filter(friday1=x.cstaff)
            m2=fridaystafftimetable.objects.filter(friday2=x.cstaff)
            m3=fridaystafftimetable.objects.filter(friday3=x.cstaff)
            m4 = fridaystafftimetable.objects.filter(friday4=x.cstaff)
            m5 = fridaystafftimetable.objects.filter(friday5=x.cstaff)
            m6 = fridaystafftimetable.objects.filter(friday6=x.cstaff)
            m7 = fridaystafftimetable.objects.filter(friday7=x.cstaff)
            m8 = fridaystafftimetable.objects.filter(friday8=x.cstaff)
            return render(request,'individualstaffttable.html',{'a':x,'p1':m1,'p2':m2,'p3':m3,'p4':m4,'p5':m5,'p6':m6,'p7':m7,'p8':m8})
        if day=='Saturday':
            m1=saturdaystafftimetable.objects.filter(saturday1=x.cstaff)
            m2=saturdaystafftimetable.objects.filter(saturday2=x.cstaff)
            m3=saturdaystafftimetable.objects.filter(saturday3=x.cstaff)
            m4 = saturdaystafftimetable.objects.filter(saturday4=x.cstaff)
            m5 = saturdaystafftimetable.objects.filter(saturday5=x.cstaff)
            m6 = saturdaystafftimetable.objects.filter(saturday6=x.cstaff)
            m7 = saturdaystafftimetable.objects.filter(saturday7=x.cstaff)
            m8 = saturdaystafftimetable.objects.filter(saturday8=x.cstaff)
            return render(request,'individualstaffttable.html',{'a':x,'p1':m1,'p2':m2,'p3':m3,'p4':m4,'p5':m5,'p6':m6,'p7':m7,'p8':m8})

    return render(request,'individualstaffttable.html',{'a':x})



def viewstaffttable(request):
    a = loggedinperson.objects.get(id=1)
    b = a.logged_id
    c = user_details.objects.get(username=b)
    d = c.School_name
    det = staffdetails.objects.filter(schoolname=d)
    if request.method=='POST':
        staff=request.POST.get('content')
        x=cstaffuse.objects.get(id=1)
        x.cstaff=staff
        x.save()
        return redirect('/individualstaffttable/',individualstaffttable)

    return render(request,'viewstaffttable.html',{'value':det})


def selectstaff(request):
    x = loggedinperson.objects.get(id=1)
    y = x.logged_id
    z = user_details.objects.get(username=y)
    a = ssprocess.objects.get(id=1)
    e = staffdetails.objects.filter(specialization=a.subject, schoolname=z.School_name)
    if request.method=='POST':
        staff=request.POST.get('staffname')
        action=request.POST.get('content')
        standard=a.standard
        period=a.period
        day=a.day
        if day == 'Monday' and period == '1st Period':
            if action=='Save':
                det=mondaystafftimetable.objects.get(standard=standard)
                det.monday1=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=mondaystafftimetable.objects.get(standard=standard)
                det.monday1=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Monday' and period == '2nd Period':
            if action=='Save':
                det=mondaystafftimetable.objects.get(standard=standard)
                det.monday2=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=mondaystafftimetable.objects.get(standard=standard)
                det.monday2=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Monday' and period == '3rd Period':
            if action == 'Save':
                det = mondaystafftimetable.objects.get(standard=standard)
                det.monday3 = staff
                det.save()
                return redirect('/addstaffttable/', addstaffttable)
            if action == 'Finish':
                det = mondaystafftimetable.objects.get(standard=standard)
                det.monday3 = staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Monday' and period == '4th Period':
            if action == 'Save':
                det = mondaystafftimetable.objects.get(standard=standard)
                det.monday4 = staff
                det.save()
                return redirect('/addstaffttable/', addstaffttable)
            if action == 'Finish':
                det = mondaystafftimetable.objects.get(standard=standard)
                det.monday4 = staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Monday' and period == '5th Period':
            if action == 'Save':
                det = mondaystafftimetable.objects.get(standard=standard)
                det.monday5 = staff
                det.save()
                return redirect('/addstaffttable/', addstaffttable)
            if action == 'Finish':
                det = mondaystafftimetable.objects.get(standard=standard)
                det.monday5 = staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Monday' and period == '6th Period':
            if action == 'Save':
                det = mondaystafftimetable.objects.get(standard=standard)
                det.monday6 = staff
                det.save()
                return redirect('/addstaffttable/', addstaffttable)
            if action == 'Finish':
                det = mondaystafftimetable.objects.get(standard=standard)
                det.monday6 = staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Monday' and period == '7th Period':
            if action == 'Save':
                det = mondaystafftimetable.objects.get(standard=standard)
                det.monday7 = staff
                det.save()
                return redirect('/addstaffttable/', addstaffttable)
            if action == 'Finish':
                det = mondaystafftimetable.objects.get(standard=standard)
                det.monday7 = staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Monday' and period == '8th Period':
            if action == 'Save':
                det = mondaystafftimetable.objects.get(standard=standard)
                det.monday8 = staff
                det.save()
                return redirect('/addstaffttable/', addstaffttable)
            if action == 'Finish':
                det = mondaystafftimetable.objects.get(standard=standard)
                det.monday8 = staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Tuesday' and period == '1st Period':
            if action=='Save':
                det=tuesdaystafftimetable.objects.get(standard=standard)
                det.tuesday1=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=tuesdaystafftimetable.objects.get(standard=standard)
                det.tuesday1=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Tuesday' and period == '2nd Period':
            if action == 'Save':
                det = tuesdaystafftimetable.objects.get(standard=standard)
                det.tuesday2 = staff
                det.save()
                return redirect('/addstaffttable/', addstaffttable)
            if action == 'Finish':
                det = tuesdaystafftimetable.objects.get(standard=standard)
                det.tuesday2 = staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Tuesday' and period == '3rd Period':
            if action == 'Save':
                det = tuesdaystafftimetable.objects.get(standard=standard)
                det.tuesday3 = staff
                det.save()
                return redirect('/addstaffttable/', addstaffttable)
            if action == 'Finish':
                det = tuesdaystafftimetable.objects.get(standard=standard)
                det.tuesday3 = staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Tuesday' and period == '4th Period':
            if action == 'Save':
                det = tuesdaystafftimetable.objects.get(standard=standard)
                det.tuesday4 = staff
                det.save()
                return redirect('/addstaffttable/', addstaffttable)
            if action == 'Finish':
                det = tuesdaystafftimetable.objects.get(standard=standard)
                det.tuesday4 = staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Tuesday' and period == '5th Period':
            if action == 'Save':
                det = tuesdaystafftimetable.objects.get(standard=standard)
                det.tuesday5 = staff
                det.save()
                return redirect('/addstaffttable/', addstaffttable)
            if action == 'Finish':
                det = tuesdaystafftimetable.objects.get(standard=standard)
                det.tuesday5 = staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Tuesday' and period == '6th Period':
            if action == 'Save':
                det = tuesdaystafftimetable.objects.get(standard=standard)
                det.tuesday6 = staff
                det.save()
                return redirect('/addstaffttable/', addstaffttable)
            if action == 'Finish':
                det = tuesdaystafftimetable.objects.get(standard=standard)
                det.tuesday6 = staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Tuesday' and period == '7th Period':
            if action=='Save':
                det=tuesdaystafftimetable.objects.get(standard=standard)
                det.tuesday7=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=tuesdaystafftimetable.objects.get(standard=standard)
                det.tuesday7=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Tuesday' and period == '8th Period':
            if action=='Save':
                det=tuesdaystafftimetable.objects.get(standard=standard)
                det.tuesday8=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=tuesdaystafftimetable.objects.get(standard=standard)
                det.tuesday8=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Wednesday' and period == '1st Period':
            if action=='Save':
                det=wednesdaystafftimetable.objects.get(standard=standard)
                det.wednesday1 = staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=wednesdaystafftimetable.objects.get(standard=standard)
                det.wednesday1 =staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Wednesday' and period == '2nd Period':
            if action=='Save':
                det=wednesdaystafftimetable.objects.get(standard=standard)
                det.wednesday2=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=wednesdaystafftimetable.objects.get(standard=standard)
                det.wednesday2=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Wednesday' and period == '3rd Period':
            if action=='Save':
                det=wednesdaystafftimetable.objects.get(standard=standard)
                det.wednesday3=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=wednesdaystafftimetable.objects.get(standard=standard)
                det.wednesday3=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Wednesday' and period == '4th Period':
            if action=='Save':
                det=wednesdaystafftimetable.objects.get(standard=standard)
                det.wednesday4=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=wednesdaystafftimetable.objects.get(standard=standard)
                det.wednesday4=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Wednesday' and period == '5th Period':
            if action=='Save':
                det=wednesdaystafftimetable.objects.get(standard=standard)
                det.wednesday5=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=wednesdaystafftimetable.objects.get(standard=standard)
                det.wednesday5=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Wednesday' and period == '6th Period':
            if action=='Save':
                det=wednesdaystafftimetable.objects.get(standard=standard)
                det.wednesday6=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=wednesdaystafftimetable.objects.get(standard=standard)
                det.wednesday6=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Wednesday' and period == '7th Period':
            if action=='Save':
                det=wednesdaystafftimetable.objects.get(standard=standard)
                det.wednesday7=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=wednesdaystafftimetable.objects.get(standard=standard)
                det.wednesday7=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Wednesday' and period == '8th Period':
            if action=='Save':
                det=wednesdaystafftimetable.objects.get(standard=standard)
                det.wednesday8=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=wednesdaystafftimetable.objects.get(standard=standard)
                det.wednesday8=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Thursday' and period == '1st Period':
            if action=='Save':
                det=thursdaystafftimetable.objects.get(standard=standard)
                det.thursday1=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=thursdaystafftimetable.objects.get(standard=standard)
                det.thursday1=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Thursday' and period == '2nd Period':
            if action=='Save':
                det=thursdaystafftimetable.objects.get(standard=standard)
                det.thursday2=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=thursdaystafftimetable.objects.get(standard=standard)
                det.thursday2=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Thursday' and period == '3rd Period':
            if action=='Save':
                det=thursdaystafftimetable.objects.get(standard=standard)
                det.thursday3=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=thursdaystafftimetable.objects.get(standard=standard)
                det.thursday3=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Thursday' and period == '4th Period':
            if action=='Save':
                det=thursdaystafftimetable.objects.get(standard=standard)
                det.thursday4=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=thursdaystafftimetable.objects.get(standard=standard)
                det.thursday4=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Thursday' and period == '5th Period':
            if action=='Save':
                det=thursdaystafftimetable.objects.get(standard=standard)
                det.thursday5=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=thursdaystafftimetable.objects.get(standard=standard)
                det.thursday5=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Thursday' and period == '6th Period':
            if action=='Save':
                det=thursdaystafftimetable.objects.get(standard=standard)
                det.thursday6=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=thursdaystafftimetable.objects.get(standard=standard)
                det.thursday6=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Thursday' and period == '7th Period':
            if action=='Save':
                det=thursdaystafftimetable.objects.get(standard=standard)
                det.thursday7=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=thursdaystafftimetable.objects.get(standard=standard)
                det.thursday7=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Thursday' and period == '8th Period':
            if action=='Save':
                det=thursdaystafftimetable.objects.get(standard=standard)
                det.thursday8=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=thursdaystafftimetable.objects.get(standard=standard)
                det.thursday8=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Friday' and period == '1st Period':
            if action=='Save':
                det=fridaystafftimetable.objects.get(standard=standard)
                det.friday1=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=fridaystafftimetable.objects.get(standard=standard)
                det.friday1=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Friday' and period == '2nd Period':
            if action=='Save':
                det=fridaystafftimetable.objects.get(standard=standard)
                det.friday2=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=tuesdaystafftimetable.objects.get(standard=standard)
                det.friday2=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Friday' and period == '3rd Period':
            if action=='Save':
                det=fridaystafftimetable.objects.get(standard=standard)
                det.friday3=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=tuesdaystafftimetable.objects.get(standard=standard)
                det.friday3=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Friday' and period == '4th Period':
            if action=='Save':
                det=fridaystafftimetable.objects.get(standard=standard)
                det.friday4=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=tuesdaystafftimetable.objects.get(standard=standard)
                det.friday4=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Friday' and period == '5th Period':
            if action=='Save':
                det=fridaystafftimetable.objects.get(standard=standard)
                det.friday5=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=tuesdaystafftimetable.objects.get(standard=standard)
                det.friday5=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Friday' and period == '6th Period':
            if action=='Save':
                det=fridaystafftimetable.objects.get(standard=standard)
                det.friday6=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=tuesdaystafftimetable.objects.get(standard=standard)
                det.friday6=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Friday' and period == '7th Period':
            if action=='Save':
                det=fridaystafftimetable.objects.get(standard=standard)
                det.friday7=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=tuesdaystafftimetable.objects.get(standard=standard)
                det.friday7=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Friday' and period == '8th Period':
            if action=='Save':
                det=fridaystafftimetable.objects.get(standard=standard)
                det.friday8=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=tuesdaystafftimetable.objects.get(standard=standard)
                det.friday8=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Saturday' and period == '1st Period':
            if action=='Save':
                det=saturdaystafftimetable.objects.get(standard=standard)
                det.saturday1=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=saturdaystafftimetable.objects.get(standard=standard)
                det.saturday1=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Saturday' and period == '2nd Period':
            if action=='Save':
                det=saturdaystafftimetable.objects.get(standard=standard)
                det.saturday2=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=saturdaystafftimetable.objects.get(standard=standard)
                det.saturday2=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Saturday' and period == '3rd Period':
            if action=='Save':
                det=saturdaystafftimetable.objects.get(standard=standard)
                det.saturday3=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=saturdaystafftimetable.objects.get(standard=standard)
                det.saturday3=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Saturday' and period == '4th Period':
            if action=='Save':
                det=saturdaystafftimetable.objects.get(standard=standard)
                det.saturday4=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=saturdaystafftimetable.objects.get(standard=standard)
                det.saturday4=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Saturday' and period == '5th Period':
            if action=='Save':
                det=saturdaystafftimetable.objects.get(standard=standard)
                det.saturday5=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=saturdaystafftimetable.objects.get(standard=standard)
                det.saturday5=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Saturday' and period == '6th Period':
            if action=='Save':
                det=saturdaystafftimetable.objects.get(standard=standard)
                det.saturday6=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=saturdaystafftimetable.objects.get(standard=standard)
                det.saturday6=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Saturday' and period == '7th Period':
            if action=='Save':
                det=saturdaystafftimetable.objects.get(standard=standard)
                det.saturday7=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=saturdaystafftimetable.objects.get(standard=standard)
                det.saturday7=staff
                det.save()
                return HttpResponse('Hi')
        if day == 'Saturday' and period == '8th Period':
            if action=='Save':
                det=saturdaystafftimetable.objects.get(standard=standard)
                det.saturday8=staff
                det.save()
                return redirect('/addstaffttable/',addstaffttable)
            if action=='Finish':
                det=saturdaystafftimetable.objects.get(standard=standard)
                det.saturday8=staff
                det.save()
                return HttpResponse('Hi')
    return render(request,'selectstaff.html',{'a':a,'value':e})


def addstaffttable(request):
    x = loggedinperson.objects.get(id=1)
    y = x.logged_id
    z = user_details.objects.get(username=y)
    if request.method == 'POST':
        standard = request.POST.get('standard')
        day = request.POST.get('day')
        period = request.POST.get('period')
        subject = request.POST.get('subject')
        if day == 'Monday':
            det=mondaystafftimetable.objects.get(standard=standard)
            det.schoolname=z.School_name
            det.save()
            a=ssprocess.objects.get(id=1)
            a.standard=standard
            a.subject=subject
            a.day=day
            a.period=period
            a.save()
            return redirect('/selectstaff/',selectstaff)

        if day == 'Tuesday':
            det = tuesdaystafftimetable.objects.get(standard=standard)
            det.schoolname = z.School_name
            det.save()
            a = ssprocess.objects.get(id=1)
            a.standard = standard
            a.subject = subject
            a.day = day
            a.period = period
            a.save()
            return redirect('/selectstaff/', selectstaff)

        if day == 'Wednesday':
            det = wednesdaystafftimetable.objects.get(standard=standard)
            det.schoolname = z.School_name
            det.save()
            a = ssprocess.objects.get(id=1)
            a.standard = standard
            a.subject = subject
            a.day = day
            a.period = period
            a.save()
            return redirect('/selectstaff/', selectstaff)

        if day == 'Thursday':
            det = thursdaystafftimetable.objects.get(standard=standard)
            det.schoolname = z.School_name
            det.save()
            a = ssprocess.objects.get(id=1)
            a.standard = standard
            a.subject = subject
            a.day = day
            a.period = period
            a.save()
            return redirect('/selectstaff/', selectstaff)

        if day == 'Friday':
            det = fridaystafftimetable.objects.get(standard=standard)
            det.schoolname = z.School_name
            det.save()
            a = ssprocess.objects.get(id=1)
            a.standard = standard
            a.subject = subject
            a.day = day
            a.period = period
            a.save()
            return redirect('/selectstaff/', selectstaff)

        if day == 'Saturday':
            det = saturdaystafftimetable.objects.get(standard=standard)
            det.schoolname = z.School_name
            det.save()
            a = ssprocess.objects.get(id=1)
            a.standard = standard
            a.subject = subject
            a.day = day
            a.period = period
            a.save()
            return redirect('/selectstaff/', selectstaff)

    return render(request,'addstaffttable.html')

def stdtimetable(request):
    a=loggedinperson.objects.get(id=1)
    b=a.logged_id
    c=user_details.objects.get(username=b)
    d=c.School_name
    e=cstduse.objects.get(id=1)
    f=e.current_standard
    if f=='1st standard':
        x=std1.objects.filter(school_name=d)
        return render(request, 'stdtimetable.html', {'values': x,'head':e})
    elif f=='2nd standard':
        x=std2.objects.filter(school_name=d)
        return render(request, 'stdtimetable.html', {'values': x,'head':e})
    elif f=='3rd standard':
        x=std3.objects.filter(school_name=d)
        return render(request, 'stdtimetable.html', {'values': x,'head':e})
    elif f=='4th standard':
        x=std4.objects.filter(school_name=d)
        return render(request, 'stdtimetable.html', {'values': x,'head':e})
    elif f=='5th standard':
        x=std5.objects.filter(school_name=d)
        return render(request, 'stdtimetable.html', {'values': x,'head':e})
    elif f=='6th standard':
        x=std6.objects.filter(school_name=d)
        return render(request, 'stdtimetable.html', {'values': x,'head':e})
    elif f=='7th standard':
        x=std7.objects.filter(school_name=d)
        return render(request, 'stdtimetable.html', {'values': x,'head':e})
    elif f=='8th standard':
        x=std8.objects.filter(school_name=d)
        return render(request, 'stdtimetable.html', {'values': x,'head':e})
    elif f=='9th standard':
        x=std9.objects.filter(school_name=d)
        return render(request, 'stdtimetable.html', {'values': x,'head':e})
    elif f=='10th standard':
        x=std10.objects.filter(school_name=d)
        return render(request, 'stdtimetable.html', {'values': x,'head':e})
    elif f=='11th standard':
        x= std11.objects.filter(school_name=d)
        return render(request, 'stdtimetable.html', {'values': x,'head':e})
    elif f=='12th standard':
        x=std12.objects.filter(school_name=d)
        return render(request, 'stdtimetable.html', {'values': x,'head':e})


def viewtimetable(request):
    if request.method=='POST':
        a=request.POST.get('content')
        b=cstduse.objects.get(id=1)
        b.current_standard=a
        b.save()
        return redirect('/stdtimetable/',stdtimetable)


    return render(request,'viewtimetable.html')

def addtimetable(request):
    x=loggedinperson.objects.get(id=1)
    y=x.logged_id
    z=user_details.objects.get(username=y)
    if request.method=='POST':
        std=request.POST.get('standard')
        day=request.POST.get('day')
        per=request.POST.get('period')
        sub=request.POST.get('subject')
        if std=='1st standard':
            if day=='Monday':
                detail=std1.objects.get(period=per)
                detail.Monday=sub
                detail.school_name=z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Tuesday':
                detail = std1.objects.get(period=per)
                detail.Tuesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Wednesday':
                detail = std1.objects.get(period=per)
                detail.Wednesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Thursday':
                detail = std1.objects.get(period=per)
                detail.Thursday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Friday':
                detail = std1.objects.get(period=per)
                detail.Friday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Saturday':
                detail = std1.objects.get(period=per)
                detail.saturday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)

        if std=='2nd standard':
            if day=='Monday':
                detail=std2.objects.get(period=per)
                detail.Monday=sub
                detail.school_name=z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Tuesday':
                detail = std2.objects.get(period=per)
                detail.Tuesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Wednesday':
                detail = std2.objects.get(period=per)
                detail.Wednesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Thursday':
                detail = std2.objects.get(period=per)
                detail.Thursday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Friday':
                detail = std2.objects.get(period=per)
                detail.Friday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Saturday':
                detail = std2.objects.get(period=per)
                detail.saturday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)

        if std=='3rd standard':
            if day=='Monday':
                detail=std3.objects.get(period=per)
                detail.Monday=sub
                detail.school_name=z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Tuesday':
                detail = std3.objects.get(period=per)
                detail.Tuesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Wednesday':
                detail = std3.objects.get(period=per)
                detail.Wednesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Thursday':
                detail = std3.objects.get(period=per)
                detail.Thursday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Friday':
                detail = std3.objects.get(period=per)
                detail.Friday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Saturday':
                detail = std3.objects.get(period=per)
                detail.saturday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)

        if std=='4th standard':
            if day=='Monday':
                detail=std4.objects.get(period=per)
                detail.Monday=sub
                detail.school_name=z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Tuesday':
                detail = std4.objects.get(period=per)
                detail.Tuesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Wednesday':
                detail = std4.objects.get(period=per)
                detail.Wednesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Thursday':
                detail = std4.objects.get(period=per)
                detail.Thursday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Friday':
                detail = std4.objects.get(period=per)
                detail.Friday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Saturday':
                detail = std4.objects.get(period=per)
                detail.saturday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)

        if std=='5th standard':
            if day=='Monday':
                detail=std5.objects.get(period=per)
                detail.Monday=sub
                detail.school_name=z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Tuesday':
                detail = std5.objects.get(period=per)
                detail.Tuesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Wednesday':
                detail = std5.objects.get(period=per)
                detail.Wednesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Thursday':
                detail = std5.objects.get(period=per)
                detail.Thursday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Friday':
                detail = std5.objects.get(period=per)
                detail.Friday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Saturday':
                detail = std5.objects.get(period=per)
                detail.saturday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)

        if std=='6th standard':
            if day=='Monday':
                detail=std6.objects.get(period=per)
                detail.Monday=sub
                detail.school_name=z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Tuesday':
                detail = std6.objects.get(period=per)
                detail.Tuesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Wednesday':
                detail = std6.objects.get(period=per)
                detail.Wednesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Thursday':
                detail = std6.objects.get(period=per)
                detail.Thursday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Friday':
                detail = std6.objects.get(period=per)
                detail.Friday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Saturday':
                detail = std6.objects.get(period=per)
                detail.saturday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)

        if std=='7th standard':
            if day=='Monday':
                detail=std7.objects.get(period=per)
                detail.Monday=sub
                detail.school_name=z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Tuesday':
                detail = std7.objects.get(period=per)
                detail.Tuesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Wednesday':
                detail = std7.objects.get(period=per)
                detail.Wednesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Thursday':
                detail = std7.objects.get(period=per)
                detail.Thursday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Friday':
                detail = std7.objects.get(period=per)
                detail.Friday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Saturday':
                detail = std7.objects.get(period=per)
                detail.saturday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)

        if std=='8th standard':
            if day=='Monday':
                detail=std8.objects.get(period=per)
                detail.Monday=sub
                detail.school_name=z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Tuesday':
                detail = std8.objects.get(period=per)
                detail.Tuesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Wednesday':
                detail = std8.objects.get(period=per)
                detail.Wednesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Thursday':
                detail = std8.objects.get(period=per)
                detail.Thursday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Friday':
                detail = std8.objects.get(period=per)
                detail.Friday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Saturday':
                detail = std8.objects.get(period=per)
                detail.saturday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)

        if std=='9th standard':
            if day=='Monday':
                detail=std9.objects.get(period=per)
                detail.Monday=sub
                detail.school_name=z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Tuesday':
                detail = std9.objects.get(period=per)
                detail.Tuesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Wednesday':
                detail = std9.objects.get(period=per)
                detail.Wednesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Thursday':
                detail = std9.objects.get(period=per)
                detail.Thursday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Friday':
                detail = std9.objects.get(period=per)
                detail.Friday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Saturday':
                detail = std9.objects.get(period=per)
                detail.saturday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)

        if std=='10th standard':
            if day=='Monday':
                detail=std10.objects.get(period=per)
                detail.Monday=sub
                detail.school_name=z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Tuesday':
                detail = std10.objects.get(period=per)
                detail.Tuesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Wednesday':
                detail = std10.objects.get(period=per)
                detail.Wednesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Thursday':
                detail = std10.objects.get(period=per)
                detail.Thursday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Friday':
                detail = std10.objects.get(period=per)
                detail.Friday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Saturday':
                detail = std10.objects.get(period=per)
                detail.saturday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)

        if std=='11th standard':
            if day=='Monday':
                detail=std11.objects.get(period=per)
                detail.Monday=sub
                detail.school_name=z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Tuesday':
                detail = std11.objects.get(period=per)
                detail.Tuesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Wednesday':
                detail = std11.objects.get(period=per)
                detail.Wednesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Thursday':
                detail = std11.objects.get(period=per)
                detail.Thursday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Friday':
                detail = std11.objects.get(period=per)
                detail.Friday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Saturday':
                detail = std11.objects.get(period=per)
                detail.saturday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)

        if std=='12th standard':
            if day=='Monday':
                detail=std12.objects.get(period=per)
                detail.Monday=sub
                detail.school_name=z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Tuesday':
                detail = std12.objects.get(period=per)
                detail.Tuesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Wednesday':
                detail = std12.objects.get(period=per)
                detail.Wednesday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Thursday':
                detail = std12.objects.get(period=per)
                detail.Thursday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Friday':
                detail = std12.objects.get(period=per)
                detail.Friday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
            elif day=='Saturday':
                detail = std12.objects.get(period=per)
                detail.saturday = sub
                detail.school_name = z.School_name
                name = request.POST.get('content')
                if name == 'Save':
                    detail.save()
                elif name == 'Finish':
                    detail.save()
                    return redirect('/viewtimetable/',viewtimetable)
    return render(request,'addtimetable.html')

def delete(request,id):
    det=staffdetails.objects.filter(id=id).delete()
    return redirect('/viewstaff/',viewstaff)


def edit(request,id):
    det=staffdetails.objects.get(id=id)
    if request.method=='POST':
        det.staffname=request.POST.get('staffname')
        det.qualification=request.POST.get('qualification')
        det.specialization=request.POST.get('specialization')
        det.workexperience=request.POST.get('experience')
        det.schoolname=request.POST.get('schoolname')
        det.roles=request.POST.get('roles')
        det.responsibilities=request.POST.get('responsibilities')
        det.mobilenumber=request.POST.get('mobilenumber')
        det.Address=request.POST.get('address')
        det.joiningdate=request.POST.get('joiningdate')
        det.save()
        return redirect('/viewstaff/',viewstaff)
    return render(request,'editstaffpage.html',{'a':det})


def viewstaff(request):
    a = loggedinperson.objects.get(id=1)
    b = a.logged_id
    c=user_details.objects.get(username=b)
    d=c.School_name
    det=staffdetails.objects.filter(schoolname=d)
    return render(request,'viewstaffpage.html',{'values':det})

def staffdetail(request):
    a = loggedinperson.objects.get(id=1)
    b = a.logged_id
    x = user_details.objects.get(username=b)
    if request.method=='POST':
        det=staffdetails()
        det.staffname=request.POST.get('staffname')
        det.qualification=request.POST.get('qualification')
        det.specialization=request.POST.get('specialization')
        det.workexperience=request.POST.get('experience')
        det.schoolname=request.POST.get('school')
        det.roles=request.POST.get('role')
        det.responsibilities=request.POST.get('responsibilities')
        det.mobilenumber=request.POST.get('mobile number')
        det.Address=request.POST.get('address')
        det.joiningdate=request.POST.get('joiningdate')
        det.save()
    return render(request, 'addstaffpage.html', {'values': x})





def userpage(request):
    a=loggedinperson.objects.get(id=1)
    b=a.logged_id
    if request.method=='POST':
        a=request.POST.get('content')
        if a=='Add staffs and roles':
            return redirect('/staffdetail/',staffdetail)
        elif a=='View Staff details':
            return redirect('/viewstaff/',viewstaff)
        elif a=='Add Timetable Subject wise':
            return redirect('/addtimetable/',addtimetable)
        elif a=='View Timetable Subject Wise':
            return redirect('/viewtimetable/',viewtimetable)
        elif a=='Add Timetable Staff Wise':
            return redirect('/addstaffttable/',addstaffttable)
        elif a=='View Timetable Staff Wise':
            return redirect('/viewstaffttable/',viewstaffttable)
        elif a=='Create User Id and Password':
            return redirect('/useridpassword/',Useridpassword)
        elif a=='View User Id and Password':
            return redirect('/viewuserid/',viewuserid)
    return render(request,'userpage.html')




def userlogin(request):
    a=loggedinperson.objects.get(id=1)
    if request.method=='POST':
        Username=request.POST.get('username')
        Password=request.POST.get('password')
        try:
            user_details.objects.get(username=Username,password=Password)
            a.logged_id=Username
            a.password=Password
            a.save()
            return redirect('/userpage/',userpage)
        except:
            return render(request,'userlogin.html',{'a':True})
    return render(request,'userlogin.html')

def userregister(request):
    if request.method == 'POST':
        password = request.POST.get('crpassword')
        password1 = request.POST.get('copassword')
        if (password == password1):
            a=user_details()
            a.username=request.POST.get('name')
            a.mail_id=request.POST.get('mail')
            a.mob_no=request.POST.get('Mobno')
            a.School_name=request.POST.get('schoolname')
            a.address=request.POST.get('address')
            a.password=request.POST.get('copassword')
            a.save()
            return redirect('/login/',userlogin)
        else:
            return render(request, 'userregister.html', {'values': 'check confirm password'})


    return render(request,'userregister.html')

def home(request):
    if request.method=='POST':
        a = request.POST.get('content')
        if (a == 'Admin Login'):
            return redirect('/login/', userlogin)
        elif (a == 'Admin Register'):
            return redirect('/registerpage/', userregister)
        elif (a=='Staff Login'):
            return redirect('/stafflogin/',stafflogin)

    return render(request,'homepage.html')
