
from django import forms;

class UploadFileForm(forms.Form):
    file = forms.FileField(label="Meta-data Spreadsheet");

class AccountSettingsForm(forms.Form):
    firstname = forms.CharField(label="First Name");
    lastname = forms.CharField(label="Last Name");
    email = forms.CharField(label="Email", required=False);
    currentpassword = forms.CharField(widget=forms.PasswordInput(), label="Current Password", required=False);
    newpassword = forms.CharField(widget=forms.PasswordInput(), label="New Password", required=False);
    newpassword_repeat = forms.CharField(widget=forms.PasswordInput(), label="New Password Again", required=False);
