from rest_framework import serializers
from .models import Strategy


class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ['id', 'name', 'is_initialized', 'is_running', 'parameters']
        # 或使用 '__all__' 自动包含所有模型字段
        # fields = '__all__'
