from django import forms

from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from .models import ApplicationList


class ApplicationListForm(NetBoxModelForm):

    class Meta:
        model = ApplicationList
        fields = ('name', 'version', 'is_licensed', 'license_key', 'tags')
