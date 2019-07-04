# from django.http import JsonResponse
# from django.test import TestCase
# import os
# import django
# # Create your tests here.
# from serializer_lesson.models import ProductCategory
# from serializer_lesson.serializers import ProductCategorySerializer
#
#
# def digui(obj):
#     obj=ProductCategory.objects.get(pk=obj)
#     parent=obj.parent
#     if parent is None:
#         obj=ProductCategory.objects.filter(parent=None)
#         parent=ProductCategorySerializer(instance=obj)
#         return JsonResponse(parent.data)
#     else:
#         obj=ProductCategory.objects.get(parent=parent)
#         return digui(obj)
#
# s=digui('NY1234')
#
# print(s)
