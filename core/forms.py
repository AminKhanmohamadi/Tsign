from django import forms

from core.models import File , Folder
from core.validators import validate_file


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name' , 'file' , 'file_type']
        file = forms.FileField(validators=[validate_file])