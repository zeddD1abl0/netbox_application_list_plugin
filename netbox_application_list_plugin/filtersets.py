from netbox.filtersets import NetBoxModelFilterSet
from .models import ApplicationList


# class ApplicationListFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = ApplicationList
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)
