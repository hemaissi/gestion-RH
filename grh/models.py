from django.db import models
from django.contrib import admin
import uuid

class Commune(models.Model):
    nom_com = models.CharField(max_length=200, null=True)
    codep_com = models.CharField(max_length=200)

    id_com = models.AutoField(primary_key=True)  
    def __str__(self):
        return self.nom_com

class Employee(models.Model): 
    nom_emp = models.CharField(max_length=200, null=True)
    preno_emp = models.CharField(max_length=200)
    daten_emp = models.CharField(max_length=200)
    adre_emp = models.CharField(max_length=200)

    id_com = models.ForeignKey(Commune, on_delete=models.CASCADE, null=True)  
    id_emp = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nom_emp

class Service(models.Model):
    nom_ser = models.CharField(max_length=200, null=True)

    id_ser = models.AutoField(primary_key=True)
    def __str__(self):
        return self.nom_ser

class Travailler(models.Model):
    id_ser = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    id_emp = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('id_ser', 'id_emp')

    def __str__(self):
        return f"{self.id_ser} - {self.id_emp}"
