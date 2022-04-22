from django_filters import rest_framework as filters

from logistic.models import Stock


class StockViewSetFilter(filters.FilterSet):
    products = filters.CharFilter(field_name='products__title', lookup_expr='contains', distinct=True  )


    class Meta:
        model = Stock
        fields = [ 'products']