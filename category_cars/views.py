# from rest_framework import response, status, generics
from rest_framework.permissions import AllowAny, IsAdminUser
# from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from category_cars.models import Category
from category_cars.serializers import CategorySerializer


# Новый метод. Все методы CRUD уже определены
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser, ]


#
# # class CreateCategory(APIView):
# #     def post(self, request):
# #         serializer = CategorySerializer(data=request.data)
# #         if serializer.is_valid(raise_exception=True):
# #             serializer.save()
# #             return response.Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# # Второй метод
# class CreateCategory(generics.CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsAdminUser, ]
#
#
# class ListCategory(generics.ListAPIView):
#     permission_classes = [AllowAny, ]
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# # class DetailCategory(generics.RetrieveAPIView):
# #     permission_classes = [AllowAny, ]
# #     queryset = Category.objects.all()
# #     serializer_class = CategorySerializer
#
#
# class UpdateCategory(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsAdminUser, ]
