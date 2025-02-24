from django import forms
from django.forms import ModelForm
from .models import *


class ChatmessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ["body"]
        widgets = {
            "body": forms.TextInput(
                attrs={
                    "placeholder": "Add message here...",
                    "class": "p-4 text-black",
                    "maxlength": "255",
                    "autofocus": True,
                }
            )
        }
