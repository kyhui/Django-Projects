from django.contrib import admin
from .forms import AddManga
from .models import Manga

class MangaAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "chapter", "updated"]
	form = AddManga

admin.site.register(Manga, MangaAdmin)