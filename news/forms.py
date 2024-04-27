# -*- coding: utf-8 -*-
from django import forms

from .models import News


class NewsForm(forms.ModelForm):
    # Define tags field
    tags = forms.CharField(required=False)

    class Meta:
        model = News
        fields = ["title", "text", "image"]

    def clean_tags(self):
        # Retrieve tags from cleaned data
        tags_input = self.cleaned_data.get("tags", "")
        # Split the input string into a list of tags
        tags_list = [
            tag.strip() for tag in tags_input.split(",") if tag.strip()
        ]

        return tags_list
