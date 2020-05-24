from django.contrib import admin
from .models import Book, Category, Tag, Recommend, Author, Bimg, Press
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'img', 'introduction', 'press', 'title', 'recommend', 'author', 'price',
                    'time', 'bnum', 'bclick')

    # 文章列表里显示想要的字段

    list_per_page = 50
    # 满50条数据就自动分页

    ordering = ('time',)
    # 后台数据列表排列方式

    list_display_links = ('id', 'title')
    # 设置哪些字段可以点击进入编辑界面

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    ordering = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Press)
class PressAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Bimg)
class BimgAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url')