from django.db import models

class documento(models.Model):
    id= models.AutoField(primary_key=True)
    fechayhora = models.CharField(max_length=200, verbose_name='titulo')
    documento = models.FileField(upload_to='documentos/', verbose_name='documento', null=True)
    descripcion = models.TextField(verbose_name='descripcion',null=True)

    def __str__(self):
        fila = "Titulo: "+ self.fechayhora + "-" + "Descripción: " +self.descripcion
        return fila
    
    def delete(self,using=None, keep_parents=False):
        self.documento.storage.delete(self.documento.name)
        super().delete()
       