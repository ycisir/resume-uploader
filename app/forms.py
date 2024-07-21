from django import forms
from app.models import Resume

class ResumeForm(forms.ModelForm):
	class Meta:
		model = Resume
		fields = '__all__'