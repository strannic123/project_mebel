from django.contrib import admin
from .models import CategoryModel, PostModel, PostImageModel

admin.site.register(CategoryModel)
admin.site.register(PostModel)
admin.site.register(PostImageModel)
