from django.db import models

# Create your models here.
class Strategy(models.Model):
    name = models.CharField(max_length=200)  # 策略名称
    is_initialized = models.BooleanField(default=False)  # 是否初始化
    is_running = models.BooleanField(default=False)  # 是否运行
    parameters = models.JSONField()  # 参数列表，使用 JSONField 存储

    class Meta:
        app_label = 'homeapp'  # 将 'homeapp' 替换为你的应用名