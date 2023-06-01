from django.contrib import admin
from .models import Page, Comment


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'added_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'added_on')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'added_on', 'approved')
    list_filter = ('approved', 'added_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)