from django.db import models
from django.contrib.auth.models import AbstractUser, User


# class User(models.Model):
#     name = models.CharField(max_length=30)
#     password = models.CharField(max_length=59)
#     email = models.CharField(max_length=59)
#     date_of_birth = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)


# class Post(models.Model):
#     text = models.CharField(max_length=30)
#     created_at = models.DateField(auto_now_add=True)
#     likes = models.IntegerField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)


class Abstract(models. Model):
    text = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Project(Abstract):
    pass



class Task(Abstract):
    status = models.BooleanField()
    deadline = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Photo(models.Model):
    image = models.ImageField(upload_to='app_10_22/static/images')


class User(AbstractUser):
    avatar = models.ImageField(upload_to='app_10_22/static/images', default='app_10_22/static/images/default.png')
    status = models.CharField(max_length=100)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Friendship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)




