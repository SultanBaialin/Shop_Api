from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response
from rest_framework.decorators import action

from .models import Product
from . import serializers
from .permission import IsAuthor


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ProductListSerializer
        return serializers.ProductSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [permissions.IsAuthenticated(), IsAuthor()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    # api/v1/product/id/
    # @action(['DELETE'], detail=True)
    # def review_delete(self, request, pk):
    #     product = self.get_object()  # Product.object.get(id=pk)
    #     user = request.user
    #     if product.reviews.filter(owner=user).exists():
    #         return response.Response('You didn\'t reviewed this product', status=400)
    #     review = product.reviews.get(owner=user)
    #     review.delete()
    #     return response.Response('Successfully deleted', status=204)