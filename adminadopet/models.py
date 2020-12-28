from django.db import models
from user.models import Donasi
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class PostDonasi(models.Model):
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

    nama_hewan = Donasi.nama_hewan
    jenis_hewan = Donasi.jenis_hewan
    jenis_kelamin_hewan = Donasi.jenis_kelamin_hewan
    usia_hewan = Donasi.usia_hewan
    domisili_hewan = Donasi.domisili_hewan
    keterangan = Donasi.keterangan
    kategori = Donasi.kategori
    kondisi_kesehatan = Donasi.kondisi_kesehatan
    lokasi_perawatan = Donasi.lokasi_perawatan
    biaya_perawatan = Donasi.biaya_perawatan
