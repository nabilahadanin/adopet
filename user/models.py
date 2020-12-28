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

class Donasi(models.Model):
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
    kondisi_kesehatan = models.CharField(max_length = 500)
    lokasi_perawatan = models.CharField(max_length = 100)
    biaya_perawatan = models.CharField(max_length = 50, default = "")
    verifikasi = models.BooleanField(default = False)

class Testimoni(models.Model):
    NILAI = [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ]
    nama_user = models.CharField(max_length = 50, default="admin")
    nilai_user = models.CharField(max_length = 50, choices = NILAI)
    komentar_user = models.CharField(max_length = 400)

class Artikel(models.Model):
    TAG = [
        ("Anjing", "Anjing"),
        ("Artikel", "Artikel"),
        ("Kucing", "Kucing"),
        ("Makanan", "Makanan")
    ]
    judul_artikel = models.CharField(max_length = 50)
    isi_artikel = models.CharField(max_length = 500)
    tag_artikel = models.CharField(max_length = 50)
    verifikasi_artikel = models.BooleanField(default = False)

class Pendonasian(models.Model):
    METODE = [
        ("gopay", "Gopay"),
        ("jenius", "Jenius"),
        ("linkaja", "Linkaja"),
        ("ovo", "OVO"),
        ("bca", "BCA"),
        ("bni", "BNI"),
        ("bri", "BRI"),
        ("mandiri", "Mandiri"),
        ("visa", "Visa")
    ]

    id_donasi = models.CharField(max_length = 50, default = "")
    nominal_donasi = models.CharField(max_length = 50)
    metode_donasi = models.CharField(max_length = 50, choices = METODE)
    nama_pendonasi = models.CharField(max_length = 50)
    hp_email = models.CharField(max_length = 50)
    dukungan = models.CharField(max_length = 500)
    anonim_donasi =  models.BooleanField(default = False)

class Forum(models.Model):
    id_adopt = models.CharField(max_length = 50, default ="")
    judul_forum = models.CharField(max_length = 50)
    isi_forum = models.CharField(max_length = 500)

class ReplyForum(models.Model):
    id_forum = models.CharField(max_length = 50, default ="")
    reply_forum = models.CharField(max_length = 500)

class HistoryChat(models.Model):
    pengirim = models.CharField(max_length = 500, default ="")
    penerima = models.CharField(max_length = 500, default ="")
    datetimep = models.DateTimeField(auto_now=True)
    pesan = models.CharField(max_length = 999)