from django import forms


class VoteMenuFormV1(forms.Form):
    votes = forms.JSONField()
