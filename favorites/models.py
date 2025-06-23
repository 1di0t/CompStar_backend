
from django.db import models
from django.conf import settings

class Region(models.Model):
    code = models.IntegerField(primary_key=True, unique=True, help_text="지역 코드 (예: 서울 100)")
    name = models.CharField(max_length=50, help_text="지역 이름 (예: 서울)")

class SubRegion(models.Model):
    code = models.IntegerField(primary_key=True, unique=True, help_text="세부 지역 코드 (예: 강남 1001)")
    name = models.CharField(max_length=50, help_text="세부 지역 이름 (예: 강남)")
    parent_region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='subregions')

class Category(models.Model):
    code = models.IntegerField(primary_key=True, unique=True, help_text="업종 코드 (예: 한식 2001)")
    name = models.CharField(max_length=50, help_text="업종 이름 (예: 한식)")

class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorites')
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    sub_region = models.ForeignKey(SubRegion, on_delete=models.PROTECT) # 필드명 수정
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']