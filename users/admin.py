from django.contrib import admin
from users.models import Video, Tiktoker

class VideoAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('video_caption', 'video_url')
    search_fields = ('video_caption', 'video_url')
    list_filter = ('video_caption', 'video_url')

class TiktokerADmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('username', 'following_count', 'followers_count', 'likes_count')


admin.site.register(Video, VideoAdmin)
admin.site.register(Tiktoker, TiktokerADmin)