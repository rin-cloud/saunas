from django.db import models

# Create your models here.
class SaunaInfo(models.Model):
    sauna_id = models.AutoField(primary_key=True)  # AutoFieldは自動的にインクリメントされる整数を提供します。
    user_id = models.IntegerField()  # 外部キーとして他のモデルを参照する場合はForeignKeyを使用します。
    store_name = models.CharField(max_length=255)
    cold_bath_rating = models.IntegerField()
    sauna_rating = models.IntegerField()
    indoor_outdoor_rating = models.IntegerField()
    access = models.CharField(max_length=255)
    sauna_review = models.CharField(max_length=255)
    store_image = models.BinaryField()

class Favorite(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()  # Userモデルを参照する外部キー
    sauna_id = models.IntegerField()  # Saunaモデルを参照する外部キー
