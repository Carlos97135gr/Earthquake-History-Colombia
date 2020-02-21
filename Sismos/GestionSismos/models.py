from django.db import models

# Create your models here.
class Departamento(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45,null=False,blank=False)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return str(self.id_departamento)+'-'+self.nombre
    
class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45,null=False,blank=False)
    fk_departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cuidad'
        verbose_name_plural = 'Cuidades'

    def __str__(self):
        return str(self.id_ciudad)+'-'+self.nombre
    
class Tipo_Magnitud(models.Model):
    id_tipo_magnitud = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45,null=False,blank=False)

    class Meta:
        verbose_name = 'Tipo de magnitud'
        verbose_name_plural = 'Tipo de magnitudes'

    def __str__(self):
        return str(self.id_tipo_magnitud)+'-'+self.nombre

class Epicentro(models.Model):
    id_epicentro = models.AutoField(primary_key=True)
    lalitud = models.CharField(max_length=45,null=False,blank=False)
    longitud = models.CharField(max_length=45,null=False,blank=False)
    profundidad = models.CharField(max_length=45,null=False,blank=False)
    fecha = models.DateField(null=False,blank=False)
    hora = models.DateTimeField(null=False,blank=False)
    valor_magnitud = models.CharField(max_length=45,null=False,blank=False)
    fk_ciudad=models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fk_tipo_magnitud=models.ForeignKey(Tipo_Magnitud, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_epicentro)+'-'+self.fk_ciudad.nombre
    
class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45,null=False,blank=False)
    apellido = models.CharField(max_length=45,null=False,blank=False)
    identificacion = models.CharField(max_length=45,null=False,blank=False)

    def __str__(self):
        return str(self.id_persona)+'-'+self.nombre
    
class Registro_Afectado(models.Model):
    id_registro = models.AutoField(primary_key=True)
    estado_persona = models.CharField(max_length=45,null=False,blank=False)
    fk_epicentro=models.ForeignKey(Epicentro, on_delete=models.CASCADE)
    fk_persona=models.ForeignKey(Persona, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Registro de afectado'
        verbose_name_plural = 'Registro de afectados'

    def __str__(self):
        return str(self.id_registro)+'-'+self.estado_persona+'-'+self.fk_persona.nombre+'-'+self.fk_epicentro.fk_ciudad.nombre