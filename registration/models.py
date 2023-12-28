from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
# class Purpose(models.Model):
#     purpose=models.CharField(max_length=250)
#     def __str__(self):
#         return self.purpose

class Order(models.Model):
    GENDER_CHOICES=[
        ('Male','Male'),
        ('Female','Female'),
    ]
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=255)
    materials_provide = models.ManyToManyField(Material)
