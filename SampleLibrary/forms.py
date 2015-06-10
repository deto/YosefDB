
from django import forms;

class UploadFileForm(forms.Form):
    uploadedBy = forms.CharField(label="Uploaded By");
    file = forms.FileField(label="Meta-data Spreadsheet");