import json
import uuid
import hashlib

from django.core.exceptions import ObjectDoesNotExist
from django import views
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from rest_framework.exceptions import ValidationError

from rest_framework import mixins, generics, permissions
# Create your views here.
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.renderers import HTMLFormRenderer, BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from permissions import ProductPermissionAny
from serializer_lesson.models import ProductCategory, User, Product
from serializer_lesson.parsers import P1902Parser
from serializer_lesson.renderers import P1902Renderer
from serializer_lesson.serializers import ProductCategorySerializer, UserSerializer, ProductSerializer


# class ProductCategoryView(views.View):
#     def get(self,request,pk=None,*args,**kwargs):
#         if pk is None:
#             catagories=ProductCategory.objects.filter(parent=None)
#             objs=ProductCategorySerializer(instance=catagories,many=True)
#             # for c in catagories:
#             #     m=ProductCategorySerializer(instance=c)
#             #     catagory_set.append(m.data)
#             return JsonResponse(json.loads(json.dumps(objs.data),strict=False),safe=False)
#
#         else:
#             try:
#                 category=ProductCategory.objects.get(pk=pk)
#                 pm=ProductCategorySerializer(instance=category)
#                 return JsonResponse(pm.data)
#             except ObjectDoesNotExist:
#                 return HttpResponseBadRequest()
#
#     def post(self,request,pk=None,*args,**kwargs):
#         if pk is None:
#             m=ProductCategorySerializer(data={'name':request.POST['name'],
#                                               'title':request.POST['title']})
#             if not m.is_valid():
#                 return HttpResponseBadRequest()
#             c=m.save()
#             return JsonResponse(m.data)
#         return HttpResponseBadRequest()

class ProductCategoryView(generics.ListAPIView,
               generics.CreateAPIView,
               generics.RetrieveAPIView,
               generics.UpdateAPIView,
               generics.DestroyAPIView):
    permission_classes = (ProductCategoryView,)
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.filter(parent=None)
# class UserView(views.View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse("SUCCESS")
#     def post(self,request,*args,**kwargs):
#         serializer=UserSerializer(data={
#             'telephone': request.POST['telephone',''],
#             'nick_name': request.POST['nick_name',''],
#             'password': request.POST['password',''],
#         })
#
#         try:
#             serializer.is_valid(raise_exception=True)
#         except ValidationError as e:
#             return HttpResponseBadRequest(str(e))
#
#         else:
#             salt=uuid.uuid4().hex
#             password=hashlib.md5((serializer.data['password']+salt).encode('utf-8')).hexdigest()
#             model=serializer.save(password=password,salt=salt)
#             # model.password=password
#             # model.salt=salt
#             # model.save(force_update=True)
#             return HttpResponse('SUCCESS')
# User
# class UserView(APIView):
#     parser_classes = (JSONParser,FormParser,MultiPartParser,P1902Parser)
#     renderer_classes = (P1902Renderer,BrowsableAPIRenderer,HTMLFormRenderer,JSONRenderer)
#     def get(self,request,pk=None,format=None):
#         if not pk:
#             users=User.objects.all()
#             user_set=UserSerializer(instance=users,many=True)
#             return Response(user_set.data)
#         else:
#             user=User.objects.get(pk=pk)
#             return Response(UserSerializer(instance=user).data)
#
#     def post(self,request,format=None):
#         from rest_framework.request import Request
#         assert isinstance(request,Request)
#         serializer=UserSerializer(data=request.data)
#         try:
#             serializer.is_valid(raise_exception=True)
#         except ValidationError as e:
#             return HttpResponseBadRequest(str(e))
#         else:
#             salt=uuid.uuid4().hex
#             password=hashlib.md5((serializer.validated_data['password']+salt).encode('utf-8')).hexdigest()
#             model=serializer.save(password=password,salt=salt)
#             return Response(serializer.validated_data)


# # 使用Mixins类
# class UserView(mixins.ListModelMixin,
#                mixins.CreateModelMixin,
#                mixins.RetrieveModelMixin,
#                mixins.UpdateModelMixin,
#                mixins.DestroyModelMixin,
#                generics.GenericAPIView):
#
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get(self,request,pk=None,*args,**kwargs):
#         if pk is None:
#             return self.list(request,*args,**kwargs)
#         else:
#             return self.retrieve(request,*args,**kwargs)
#
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
#
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
#
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)
#
#     def perform_create(self, serializer):
#         salt=uuid.uuid4().hex
#         password=hashlib.md5((serializer.validated_data['password']+salt).encode("utf-8")).hexdigest()
#

# 使用Generic class-based views
# 创建列表视图
class UserListView(generics.ListAPIView,
                   generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        salt=uuid.uuid4().hex
        password=hashlib.md5((serializer.validated_data['password']+salt).encode("utf-8")).hexdigest()
        serializer.save(password=password,salt=salt)

# 创建详情视图
class UserDetailView(generics.RetrieveAPIView,
                     generics.UpdateAPIView,
                     generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductView(generics.ListAPIView,
               generics.CreateAPIView,
               generics.RetrieveAPIView,
               generics.UpdateAPIView,
               generics.DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (ProductPermissionAny,)


# 将列表视图与详情视图绑定
class UserView(generics.ListAPIView,
               generics.CreateAPIView,
               generics.RetrieveAPIView,
               generics.UpdateAPIView,
               generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,ProductPermissionAny)

    def get(self,request,pk=None,*args,**kwargs):
        if pk is None:
            return generics.ListAPIView.get(self,request,*args,**kwargs)
            # super(generics.ListAPIView).get(request,*args,**kwargs)
        else:
            return generics.RetrieveAPIView.get(self,request,*args,**kwargs)
            # super(generics.RetrieveAPIView.get(self,request,*args,**kwargs))

    def perform_create(self, serializer):
        salt=uuid.uuid4().hex
        password=hashlib.md5((serializer.validated_data['password'] + salt).encode("utf-8")).hexdigest()
        serializer.save(password=password, salt=salt)










