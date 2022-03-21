from django.db import models

# Create your models here.
class user_details(models.Model):
    username = models.CharField(max_length=20)
    mail_id = models.CharField(max_length=50)
    mob_no = models.CharField(max_length=10)
    School_name = models.CharField(max_length=500)
    address = models.CharField(max_length=1000)
    password = models.CharField(max_length=20)

class loggedinperson(models.Model):
    logged_id=models.CharField(max_length=20)
    password=models.CharField(max_length=16)


class staffdetails(models.Model):
    staffname=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    specialization=models.CharField(max_length=20)
    workexperience=models.IntegerField()
    schoolname=models.CharField(max_length=500)
    roles=models.CharField(max_length=100)
    responsibilities=models.CharField(max_length=1000)
    mobilenumber=models.CharField(max_length=10)
    Address=models.CharField(max_length=1000)
    joiningdate=models.DateField()

class std1(models.Model):
    period = models.CharField(max_length=20)
    Monday = models.CharField(max_length=30)
    Tuesday = models.CharField(max_length=30)
    Wednesday = models.CharField(max_length=30)
    Thursday = models.CharField(max_length=30)
    Friday = models.CharField(max_length=30)
    Saturday = models.CharField(max_length=30)
    school_name=models.CharField(max_length=500,default=None)

class std2(models.Model):
    period = models.CharField(max_length=20)
    Monday = models.CharField(max_length=30)
    Tuesday = models.CharField(max_length=30)
    Wednesday = models.CharField(max_length=30)
    Thursday = models.CharField(max_length=30)
    Friday = models.CharField(max_length=30)
    Saturday = models.CharField(max_length=30)
    school_name=models.CharField(max_length=500)


class std3(models.Model):
    period = models.CharField(max_length=20)
    Monday = models.CharField(max_length=30)
    Tuesday = models.CharField(max_length=30)
    Wednesday = models.CharField(max_length=30)
    Thursday = models.CharField(max_length=30)
    Friday = models.CharField(max_length=30)
    Saturday = models.CharField(max_length=30)
    school_name=models.CharField(max_length=500)


class std4(models.Model):
    period = models.CharField(max_length=20)
    Monday = models.CharField(max_length=30)
    Tuesday = models.CharField(max_length=30)
    Wednesday = models.CharField(max_length=30)
    Thursday = models.CharField(max_length=30)
    Friday = models.CharField(max_length=30)
    Saturday = models.CharField(max_length=30)
    school_name=models.CharField(max_length=500)


class std5(models.Model):
    period = models.CharField(max_length=20)
    Monday = models.CharField(max_length=30)
    Tuesday = models.CharField(max_length=30)
    Wednesday = models.CharField(max_length=30)
    Thursday = models.CharField(max_length=30)
    Friday = models.CharField(max_length=30)
    Saturday = models.CharField(max_length=30)
    school_name=models.CharField(max_length=500)

class std6(models.Model):
    period = models.CharField(max_length=20)
    Monday = models.CharField(max_length=30)
    Tuesday = models.CharField(max_length=30)
    Wednesday = models.CharField(max_length=30)
    Thursday = models.CharField(max_length=30)
    Friday = models.CharField(max_length=30)
    Saturday = models.CharField(max_length=30)
    school_name=models.CharField(max_length=500)

class std7(models.Model):
    period = models.CharField(max_length=20)
    Monday = models.CharField(max_length=30)
    Tuesday = models.CharField(max_length=30)
    Wednesday = models.CharField(max_length=30)
    Thursday = models.CharField(max_length=30)
    Friday = models.CharField(max_length=30)
    Saturday = models.CharField(max_length=30)
    school_name=models.CharField(max_length=500)

class std8(models.Model):
    period = models.CharField(max_length=20)
    Monday = models.CharField(max_length=30)
    Tuesday = models.CharField(max_length=30)
    Wednesday = models.CharField(max_length=30)
    Thursday = models.CharField(max_length=30)
    Friday = models.CharField(max_length=30)
    Saturday = models.CharField(max_length=30)
    school_name=models.CharField(max_length=500)

class std9(models.Model):
    period = models.CharField(max_length=20)
    Monday = models.CharField(max_length=30)
    Tuesday = models.CharField(max_length=30)
    Wednesday = models.CharField(max_length=30)
    Thursday = models.CharField(max_length=30)
    Friday = models.CharField(max_length=30)
    Saturday = models.CharField(max_length=30)
    school_name=models.CharField(max_length=500)


class std10(models.Model):
    period = models.CharField(max_length=20)
    Monday = models.CharField(max_length=30)
    Tuesday = models.CharField(max_length=30)
    Wednesday = models.CharField(max_length=30)
    Thursday = models.CharField(max_length=30)
    Friday = models.CharField(max_length=30)
    Saturday = models.CharField(max_length=30)
    school_name=models.CharField(max_length=500)

class std11(models.Model):
    period = models.CharField(max_length=20)
    Monday = models.CharField(max_length=30)
    Tuesday = models.CharField(max_length=30)
    Wednesday = models.CharField(max_length=30)
    Thursday = models.CharField(max_length=30)
    Friday = models.CharField(max_length=30)
    Saturday = models.CharField(max_length=30)
    school_name=models.CharField(max_length=500)

class std12(models.Model):
    period = models.CharField(max_length=20)
    Monday = models.CharField(max_length=30)
    Tuesday = models.CharField(max_length=30)
    Wednesday = models.CharField(max_length=30)
    Thursday = models.CharField(max_length=30)
    Friday = models.CharField(max_length=30)
    Saturday = models.CharField(max_length=30)
    school_name=models.CharField(max_length=500)

class cstduse(models.Model):
    current_standard=models.CharField(max_length=20)


class mondaystafftimetable(models.Model):
    standard=models.CharField(max_length=20)
    monday1=models.CharField(max_length=20)
    monday2=models.CharField(max_length=20)
    monday3 = models.CharField(max_length=20)
    monday4 = models.CharField(max_length=20)
    monday5 = models.CharField(max_length=20)
    monday6 = models.CharField(max_length=20)
    monday7 = models.CharField(max_length=20)
    monday8 = models.CharField(max_length=20)
    schoolname = models.CharField(max_length=100,default=None)

class tuesdaystafftimetable(models.Model):
    standard=models.CharField(max_length=20)
    tuesday1=models.CharField(max_length=20)
    tuesday2=models.CharField(max_length=20)
    tuesday3 = models.CharField(max_length=20)
    tuesday4 = models.CharField(max_length=20)
    tuesday5 = models.CharField(max_length=20)
    tuesday6 = models.CharField(max_length=20)
    tuesday7 = models.CharField(max_length=20)
    tuesday8 = models.CharField(max_length=20)
    schoolname = models.CharField(max_length=100)

class wednesdaystafftimetable(models.Model):
    standard=models.CharField(max_length=20)
    wednesday1=models.CharField(max_length=20)
    wednesday2=models.CharField(max_length=20)
    wednesday3 = models.CharField(max_length=20)
    wednesday4 = models.CharField(max_length=20)
    wednesday5 = models.CharField(max_length=20)
    wednesday6 = models.CharField(max_length=20)
    wednesday7 = models.CharField(max_length=20)
    wednesday8 = models.CharField(max_length=20)
    schoolname = models.CharField(max_length=100)

class thursdaystafftimetable(models.Model):
    standard=models.CharField(max_length=20)
    thursday1=models.CharField(max_length=20)
    thursday2=models.CharField(max_length=20)
    thursday3 = models.CharField(max_length=20)
    thursday4 = models.CharField(max_length=20)
    thursday5 = models.CharField(max_length=20)
    thursday6 = models.CharField(max_length=20)
    thursday7 = models.CharField(max_length=20)
    thursday8 = models.CharField(max_length=20)
    schoolname = models.CharField(max_length=100)


class fridaystafftimetable(models.Model):
    standard=models.CharField(max_length=20)
    friday1=models.CharField(max_length=20)
    friday2=models.CharField(max_length=20)
    friday3 = models.CharField(max_length=20)
    friday4 = models.CharField(max_length=20)
    friday5 = models.CharField(max_length=20)
    friday6 = models.CharField(max_length=20)
    friday7 = models.CharField(max_length=20)
    friday8 = models.CharField(max_length=20)
    schoolname = models.CharField(max_length=100)

class saturdaystafftimetable(models.Model):
    standard=models.CharField(max_length=20)
    saturday1=models.CharField(max_length=20)
    saturday2=models.CharField(max_length=20)
    saturday3 = models.CharField(max_length=20)
    saturday4 = models.CharField(max_length=20)
    saturday5 = models.CharField(max_length=20)
    saturday6 = models.CharField(max_length=20)
    saturday7 = models.CharField(max_length=20)
    saturday8 = models.CharField(max_length=20)
    schoolname = models.CharField(max_length=100)



class ssprocess(models.Model):
    standard=models.CharField(max_length=20)
    period=models.CharField(max_length=20)
    day=models.CharField(max_length=20)
    subject=models.CharField(max_length=30)

class cstaffuse(models.Model):
    cstaff=models.CharField(max_length=50)

class useridpassword(models.Model):
    role=models.CharField(max_length=20)
    role_id=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    schoolname=models.CharField(max_length=100,default=None)

class currentloginstaff(models.Model):
    userid=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
