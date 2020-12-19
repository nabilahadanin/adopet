from django import forms

from .models import Hewan, RequestAdopsi

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