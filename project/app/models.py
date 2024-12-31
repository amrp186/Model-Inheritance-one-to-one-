from django.db import models

# Create your models here.
class Aadhar(models.Model):
    aadhar = models.IntegerField(primary_key=True)
    def __str__(self):
      return str(self.aadhar)


class Students(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField()
    stu_contact = models.IntegerField()
    aadhar_no = models.OneToOneField(Aadhar,on_delete=models.PROTECT,to_field='aadhar')
    def __str__(self):
       return self.stu_name