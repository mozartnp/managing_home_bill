from django import forms

from backend.apps.custom_user.models import CustomUserModels, TeamModel

class TeamChoiceForms(forms.ModelForm):
    team = forms.ModelChoiceField(label="Grupo", queryset=None)

    class Meta:
        model = CustomUserModels
        fields = [
            "team"
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TeamChoiceForms, self).__init__(*args, **kwargs)
        self.fields['team'].queryset = self.user.team.all()