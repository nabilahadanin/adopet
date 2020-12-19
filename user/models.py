from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Hewan(models.Model):
    KATEGORI_HEWAN = [
        ("Kucing", "Kucing"),
        ("Anjing", "Anjing"),
        ("Kelinci", "Kelinci"),
        ("Burung", "Burung"),
        ("Ikan", "Ikan"),
        ("Hewan Pengerat", "Pengerat"),
        ("Unggas", "Unggas"),
        ("Reptil", "Reptil"),
        ("Lainnya", "Lainnya")
    ]

    JENIS_KELAMIN_HEWAN = [
        ("Jantan", "Jantan"),
        ("Betina", "Betina")
    ]

    nama_hewan = models.CharField(max_length = 50)
    jenis_hewan = models.CharField(max_length = 50)
    jenis_kelamin_hewan = models.CharField(max_length = 50, choices = JENIS_KELAMIN_HEWAN)
    usia_hewan = models.CharField(max_length = 50)
    domisili_hewan = models.CharField(max_length = 50)
    keterangan = models.CharField(max_length = 500, default = "")
    kategori = models.CharField(max_length = 50, choices = KATEGORI_HEWAN)
    kondisi_fisik_hewan = models.CharField(max_length = 500)
    kondisi_psikis_hewan = models.CharField(max_length = 500)
    mahar_adopsi = models.CharField(max_length = 500, default = "")

class FotoHewan(models.Model):
    foto = models.ImageField(upload_to='static/images/')
    hewan = models.ForeignKey(Hewan, on_delete=models.CASCADE)

class RequestAdopsi(models.Model):
    id_hewan = models.CharField(max_length = 50)
    nama_hewan = models.CharField(max_length = 50)
    nama_pengadopsi = models.CharField(max_length = 50)
    nomor_hp = models.CharField(max_length = 14)
    email_pengadopsi = models.CharField(max_length = 50)
    alamat_pengadopsi = models.CharField(max_length = 200)