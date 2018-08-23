from django.contrib import admin
from switch.models import Vocabulary
# Register your models here.



class VocabularyAdmin(admin.ModelAdmin):
	list_display	=	('id','vocab','inputdate')
	ordering		=	('vocab',)



admin.site.register(Vocabulary,VocabularyAdmin)