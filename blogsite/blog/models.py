from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.utils.text import slugify


User = get_user_model()

# Create your models here.
class Post(models.Model):
    # post relations & identity
    uuid = models.UUIDField(default=uuid.uuid4, editable=False , unique=True)
    slug = models.SlugField(blank=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag", related_name="posts", blank=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)



    # details
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to="post_images/", blank=True, null=True)



    # seo
    meta_title = models.CharField(max_length=250, blank=True)
    meta_description = models.TextField(blank=True)



    # dates & times
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)



    # permissions
    status = models.BooleanField(default=True)
    allow_comments = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)



class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name