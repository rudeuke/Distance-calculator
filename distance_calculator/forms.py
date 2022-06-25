from django import forms


class numberOfPointsForm(forms.Form):
    numberOfPoints = forms.IntegerField(
        label="Number of points", min_value=2, max_value=50, required=True, initial=2)
