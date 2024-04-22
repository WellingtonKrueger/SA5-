from django.db import models
 
# Create your models here.
class Employee(models.Model):  
    Codigoproduto = models.CharField(max_length=20)  
    Nome = models.CharField(max_length=40)  
    Codigobarras = models.CharField(max_length=20)
    Preco = models.CharField(max_length=10) 
   
    class Meta:  
        db_table = "tblemployee"
