from django.db import models

# Create your models here.

class HaberKategori(models.Model):
	kategori_adi = models.CharField(max_length=20)


class Haber(models.Model):
	baslik = models.CharField(max_length=50)
	onyazi = models.CharField(max_length=150)
	anayazi = models.TextField()
	kategori = models.ForeignKey(HaberKategori)
	resim1 = models.CharField(max_length=200)
	resim2 = models.CharField(max_length=200)
	resim3 = models.CharField(max_length=200)
	resim4 = models.CharField(max_length=200)
	resim5 = models.CharField(max_length=200)
	resim6 = models.CharField(max_length=200)
	tarih = models.DateTimeField(editable=False)
	vidyo_url = models.CharField(max_length=200)

