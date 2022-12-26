from django.db import models

# Create your models here.
class User_Role(models.Model):
    role_id=models.IntegerField(primary_key=True)


class User(models.Model):
    username=models.CharField(max_length=200,primary_key=True)
    password=models.CharField(max_length=200)
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    country=models.CharField(max_length=200)
    ph_no=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    role_id=models.ForeignKey(User_Role,on_delete=models.CASCADE)

class President(models.Model):
    username_p=models.ForeignKey(User,on_delete=models.CASCADE)

class Team_Leader(models.Model):
    username_l=models.ForeignKey(User,primary_key=True,on_delete=models.CASCADE)
    username_p=models.ForeignKey(President,on_delete=models.CASCADE)

class Team(models.Model):
    team_id=models.IntegerField(primary_key=True)
    team_name=models.CharField(max_length=100)
    team_kpi=models.FloatField()
    username_l=models.ForeignKey(Team_Leader,on_delete=models.CASCADE)


class Team_Member(models.Model):
    username_M=models.ForeignKey(User,on_delete=models.CASCADE,primary_key=True)
    team_id=models.ForeignKey(Team,on_delete=models.RESTRICT)

class Task(models.Model):
    id=models.IntegerField(primary_key=True)
    task_name=models.CharField(max_length=100)
    task_desc=models.CharField(max_length=500)
    due_date=models.DateField()
    status=models.CharField(max_length=200)
    org_name=models.CharField(max_length=100)
    org_no=models.CharField(max_length=12)
    org_email=models.EmailField()
    location=models.CharField(max_length=200)
    sdg_no=models.CharField(max_length=15)
    username_L=models.ForeignKey(Team_Leader,on_delete=models.CASCADE)
    username_M=models.ForeignKey(Team_Member,on_delete=models.CASCADE)










