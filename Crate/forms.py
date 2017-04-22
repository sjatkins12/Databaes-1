from django import forms

from Crate.models import Discussion


class ReportForm(forms.Form):
    report = forms.CharField(label="Enter your report", max_length=500, widget=forms.Textarea)


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['comment']
