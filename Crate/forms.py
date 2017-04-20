from django import forms


class ReportForm(forms.Form):
    report = forms.CharField(label="Enter your report", max_length=500, widget=forms.Textarea)


class DiscussionForm(forms.Form):
    discussion = forms.CharField(label="Enter your discussion", max_length=500, widget=forms.Textarea)
