from django.db import models

# Create your models here.
class contactModelForm(models.Model):
    id_name = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20 )
    roll = models.IntegerField()
    address = models.TextField()
    Accept_the_terms_and_conditions = models.BooleanField()
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField()
    file_upload = models.FileField(upload_to='files/')
    float_field = models.FloatField()
    integer_Number = models.IntegerField()
    null_boolean_field = models.BooleanField(null= True, blank = True)
    positive_big_integer_field = models.PositiveBigIntegerField()
    slug_field = models.SlugField()
    text_field = models.TextField()
    url_field = models.URLField()















