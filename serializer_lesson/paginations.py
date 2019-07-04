from rest_framework.pagination import PageNumberPagination

class UserPaginationClass(PageNumberPagination):
    page_size = 3