from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser) :
    profile = models.ImageField()   # 프로필은 이미지 사진을 의미

class Post(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 유저가 지워질 때 포스트도 지워짐(?)
    image = models.ImageField()
    caption = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # 좋아요 수를 세어주는 걸 만들 것임
    @property
    def like_count(self) :
        return self.like_set.count() # like의 수를 세어서 넘겨줌
        # like_set은 모델의 Like의 포스트에서 걔한테 접근할 수 있는 이름의 초기값(?), 바꿀 수도 있음

    class Meta :
        ordering = ['-updated'] # 최신 기준으로 정렬시킴

    def __str__(self) :
        return '%s - %s' % (self.id, self.user)

class Comment(models.Model) :
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

class Like(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)