from django import forms
from . import models, parser_ts, parser_rezka

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('rezka.ag', 'rezka.ag'),
        ('ts.kg', 'ts.kg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]
    def parser_data(self):
        if self.data['media_type'] == 'ts.kg':
            ts_films = parser_ts.parsing_ts()
            for i in ts_films:
                models.TsModel.objects.create(**i)
        elif self.data['media_type'] == 'rezka.ag':
            rezka_films = parser_rezka.parsing_rezka()
            for i in rezka_films:
                models.RezkaModel.objects.create(**i)