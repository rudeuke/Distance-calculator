from django import forms


class numberOfPointsForm(forms.Form):
    numberOfPoints = forms.IntegerField(
        label="Number of points", min_value=2, max_value=50, required=True, initial=2)


class pointForm(forms.Form):
    pointLatitude = forms.FloatField(
        label="Latitude", min_value=-90, max_value=90, initial=0.0, widget=forms.NumberInput(attrs={'step': '0.1'}))
    pointLongitude = forms.FloatField(
        label="Longitude", min_value=-180, max_value=180, initial=0.0, widget=forms.NumberInput(attrs={'step': '0.1'}))
