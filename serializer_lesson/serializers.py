import re

from rest_framework import serializers

from serializer_lesson.models import ProductCategory, Product, User

# 序列化链表
class ProductCategorySerializer(serializers.ModelSerializer):
    children=serializers.SerializerMethodField()
    def get_children(self,instance):
        children=ProductCategory.objects.filter(parent=instance)
        children_set=[ProductCategorySerializer(instance=child).data for  child in children]
        return children_set

    class Meta:
        model=ProductCategory
        exclude=()

# 序列化
class ProductSerializer(serializers.ModelSerializer):
    category=serializers.SerializerMethodField()
    def get_category(self,instance):
        return ProductCategorySerializer(instance=instance.type).data

    class Meta:
        model=Product
        exclude=()

class UserSerializer(serializers.ModelSerializer):
    def validate_telephone(self, value):
        pattern="^1[0-9]{10}$"
        if not re.match(pattern,value):
            raise serializers.ValidationError('Your telephone is invalid')
        return value
    def validate(self, attrs):
        return attrs

    class Meta:
        model=User
        exclude=('salt',)
