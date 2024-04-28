from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=255)
    contacto_nombre = models.CharField(max_length=255)
    contacto_email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    cif = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_empresa

class Factura(models.Model):
    cliente = models.ForeignKey('Usuario', on_delete=models.CASCADE, related_name='facturas')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    pagada = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Factura {self.id} - {self.cliente.username}"

class LineaFactura(models.Model):
    factura = models.ForeignKey('Factura', on_delete=models.CASCADE, related_name='lineas_factura')
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True, related_name='lineas_factura')
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre} a {self.precio_unitario} cada uno"

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario
