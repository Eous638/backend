from django.contrib import admin
from .models import Place, Tour
# Register your models here.

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    fields = ('title','title_en', 'description','description_en', 'latitude', 'longitude', 'ordering', 'image', 'tour', 'icon')
    
@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    fields = ('title','title_en', 'description', 'description_en','image')
    
