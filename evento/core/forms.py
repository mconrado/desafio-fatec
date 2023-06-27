from django import forms


class CoreForm(forms.Form):
    aluno = forms.CharField(label='Aluno')
    professores = (('greg', 'Gregório'), ('orlando', 'Orlando'))
    professor = forms.ChoiceField(choices=professores)
