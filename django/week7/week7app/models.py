from django.db import models

class Company(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  type = models.CharField(max_length=255)
  employee = models.IntegerField()

  def insert(self):
    company1 = Company(name="Google",address="Address1",type="IT",employee=100000)
    company2 = Company(name="Boeing",address="Address2",type="Manufacturing",employee=50000)
    company3 = Company(name="Microsoft",address="Address3",type="IT",employee=450000)
    company4 = Company(name="Starbucks",address="Address4",type="F&B",employee=90000)
    companyList = [company1,company2,company3,company4]
    for x in companyList:
        x.save()
