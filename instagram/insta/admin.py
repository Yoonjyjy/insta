from django.contrib import admin
from .models import Post, Comment, User, Like
# 모델들을 데려옴

@admin.register(Post) # 데코레이터 decorater
class PostAdmin(admin.ModelAdmin) :
    list_display = ('user', 'image', 'caption', 'created', 'updated', 'like_count') # 튜플로 묶어줌
    list_filter = ['caption'] # 필터를 캡션의 내용으로 하겠다!
    search_fields = ['caption'] # 검색도 캡션의 내용으로 하겠다!
    fields = ['user', 'image', 'caption'] # 글 작성 시 필요한 것들

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin) :
    list_display = ('post', 'user', 'content')
    fields = ['post', 'user', 'content']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin) :
    list_display = ('user', 'post')
    fields = ['user', 'post']

@admin.register(User)
class UserAdmin(admin.ModelAdmin) :
    pass # 장고에서 알아서 해줄 것이기 때문에 패스(아까 상속을 받아와서)