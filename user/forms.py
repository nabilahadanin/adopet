from django import forms
from django.forms import ModelForm
from .models import Hewan, RequestAdopsi, Donasi, Testimoni, Artikel, Pendonasian, Forum, ReplyForum, HistoryChat

class FormAdopt(forms.ModelForm):
    class Meta:
        model = Hewan
        fields = (
            'nama_hewan', 'jenis_hewan', 'jenis_kelamin_hewan', 'usia_hewan', 
            'domisili_hewan', 'keterangan', 'kategori', 'kondisi_fisik_hewan',
            'kondisi_psikis_hewan', 'mahar_adopsi',
        )
        widgets = {
            'nama_hewan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nama_hewan'}), 
            'jenis_hewan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'jenis_hewan'}), 
            'jenis_kelamin_hewan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'jenis_kelamin_hewan'}),
            'usia_hewan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'usia_hewan'}),
            'domisili_hewan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'domisili_hewan'}), 
            'keterangan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'keterangan'}), 
            'kategori': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'kategori'}), 
            'kondisi_fisik_hewan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'kondisi_fisik_hewan'}),
            'kondisi_psikis_hewan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'kondisi_psikis_hewan'}), 
            'mahar_adopsi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'mahar_adopsi'}),
        }

class FormFoto(forms.Form):
    foto = forms.ImageField()

class FormRequestAdopsi(forms.ModelForm):
    class Meta:
        model = RequestAdopsi
        fields = (
            'id_hewan',
            'nama_hewan',
            'nama_pengadopsi', 
            'nomor_hp', 
            'email_pengadopsi', 
            'alamat_pengadopsi', 
        )
        widgets = {
            'nama_pengadopsi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nama_pengadopsi'}), 
            'nomor_hp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nomor_hp'}), 
            'email_pengadopsi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email_pengadopsi'}),
            'alamat_pengadopsi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alamat_pengadopsi'}), 
        }

class FormDonasi(forms.ModelForm):
    class Meta:
        model = Donasi
        fields = (
            'nama_hewan', 'jenis_hewan', 'jenis_kelamin_hewan', 'usia_hewan', 
            'domisili_hewan', 'keterangan', 'kategori', 'kondisi_kesehatan',
            'lokasi_perawatan', 'biaya_perawatan'
        )
        widgets = {
            'nama_hewan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nama_hewan'}), 
            'jenis_hewan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'jenis_hewan'}), 
            'jenis_kelamin_hewan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'jenis_kelamin_hewan'}),
            'usia_hewan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'usia_hewan'}),
            'domisili_hewan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'domisili_hewan'}), 
            'keterangan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'keterangan'}), 
            'kategori': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'kategori'}), 
            'kondisi_kesehatan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'kondisi_kesehatan'}),
            'lokasi_perawatan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'lokasi_perawatan'}), 
            'biaya_perawatan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'biaya_perawatan'}),
        }
class FormTestimoni(forms.ModelForm):
    class Meta:
        model = Testimoni
        fields = (
            'nama_user', 'nilai_user', 'komentar_user'
        )
        widgets = {
            'nama_user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'komentar_user'}),
            'nilai_user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nilai_user'}), 
            'komentar_user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'komentar_user'}), 
        }

class FormRequestArtikel(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = (
            'judul_artikel', 'isi_artikel', 'tag_artikel'
        )
        widgets = {
            'judul_artikel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'judul artikel'}),
            'isi_artikel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'isi artikel'}),
            'tag_artikel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tag artikel'}),
        }

class FormPendonasian(forms.ModelForm):
    class Meta: 
        model = Pendonasian
        fields = (
            'id_donasi','nominal_donasi', 'metode_donasi', 'nama_pendonasi', 'hp_email', 'dukungan'
        )
        widgets = {
            'nominal_donasi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nominal donasi'}),
            'metode_donasi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'metode donasi'}),
            'nama_pendonasi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nama pendonasi'}),
            'hp_email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'hp atau email'}),
            'dukungan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'dukungan'}),
        }

class FormForum(forms.ModelForm):
    class Meta:
        model = Forum
        fields = (
            'id_adopt', 'judul_forum', 'isi_forum'
        )
        widgets = {
            'judul_forum' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'judul forum'}),
            'isi_forum' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'isi forum'}),
        }

class FormReply(forms.ModelForm):
    class Meta:
        model = ReplyForum
        fields = (
            'id_forum', 'reply_forum'
        )
        widgets = {
            'reply_forum': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tuliskan reply disini'}),
        }

class FormHistoryChat(forms.ModelForm):
    class Meta:
        model = HistoryChat
        fields = (
            'pengirim', 'penerima', 'pesan'
        )
        widgets = {
            'pesan': forms.TextInput(attrs={'class': 'form-control'}),
        }