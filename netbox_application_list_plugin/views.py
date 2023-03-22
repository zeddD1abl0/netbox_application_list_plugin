from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables


class ApplicationListView(generic.ObjectView):
    queryset = models.ApplicationList.objects.all()


class ApplicationListListView(generic.ObjectListView):
    queryset = models.ApplicationList.objects.all()
    table = tables.ApplicationListTable


class ApplicationListEditView(generic.ObjectEditView):
    queryset = models.ApplicationList.objects.all()
    form = forms.ApplicationListForm


class ApplicationListDeleteView(generic.ObjectDeleteView):
    queryset = models.ApplicationList.objects.all()


