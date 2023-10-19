from django.db import models

# Create your models here.
class Teacher(models.Model):
    tname=models.CharField(max_length=50)
    subject=models.CharField(max_length=100)
    

    def __str__(self):
        return self.tname
    
class Student(models.Model):
    sname=models.CharField(max_length=50)
    group=models.CharField(max_length=100)
    teachers=models.ManyToManyField("Teacher", related_name='students')

    def __str__(self):
        return self.sname
    
class Certificate(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issued_date = models.DateField(auto_now_add=True)

 