from django import forms

from .models import Hewan

class FormAdopt(forms.ModelForm):
    class Meta:
        model = Hewan
        fields = [
            'nama_hewan', 'jenis_hewan', 'jenis_kelamin_hewan', 'usia_hewan', 
            'domisili_hewan', 'keterangan', 'kategori', 'kondisi_fisik_hewan',
            'kondisi_psikis_hewan', 'mahar_adopsi'
        ]

class FormFoto(forms.Form):
    foto = forms.ImageField()
