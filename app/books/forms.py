from django import forms


class BooksFilterForm(forms.Form):
    ordering = forms.ChoiceField(
        required=False,
        choices=[
            ["author", "authors"],
            ["-author", "authors^"],
            ["year", "years"],
            ["year", "years^"],
        ],
    )
