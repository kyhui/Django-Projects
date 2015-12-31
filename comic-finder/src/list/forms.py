from django import forms
from .models import Manga

class AddManga(forms.ModelForm):
	class Meta:
		model = Manga
		fields = ['name','chapter']

	def clean_chapter(self):
		chapter =  self.cleaned_data.get('chapter')
		if chapter < 1:
			raise forms.ValidationError("Please put in a chapter greater than 0")
		return chapter

class ContactForm(forms.Form):
	full_name = forms.CharField();
	email = forms.EmailField();
	message = forms.CharField();