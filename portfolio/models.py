from django.db import models

class Project(models.Model):
    title = models.CharField(verbose_name = "Título", max_length=200)
    description = models.TextField(verbose_name= "Descripción")
    image = models.ImageField(verbose_name= "Imagen", upload_to ="projects")
    link_demo = models.URLField(verbose_name= "Demo", null=True, blank=True)
    link_codigo = models.URLField(verbose_name= "Código", null=True, blank=True)
    created = models.DateTimeField( verbose_name= "Fecha de creación",auto_now_add=True)
    updated = models.DateTimeField( verbose_name="Fecha de modificación",auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]
  
