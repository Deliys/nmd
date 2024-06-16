from django import forms

from .models import Autor, DocSorpbd, Owner

class DocSorpbdForm(forms.ModelForm):

    individual_owners = forms.ModelMultipleChoiceField(
        queryset=Owner.objects.filter(owner_types=True),
        widget=forms.SelectMultiple,
    )

    print(individual_owners.queryset)

    organization_owners = forms.ModelMultipleChoiceField(
        queryset=Owner.objects.filter(owner_types=False),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = DocSorpbd
        fields = ['registration_certificate_number', 'database_name', 'request_number', 'requestdate', 'registrationdate', 'authors', 'individual_owners', 'organization_owners']

    def __init__(self, *args, **kwargs):

        super(DocSorpbdForm, self).__init__(*args, **kwargs)

        self.fields['authors'].queryset = Autor.objects.all()

from django import forms


class SearchForm(forms.Form):
    TABLE_CHOICES = [
        ('Dissertation', 'Dissertation'),
        ('DocSorpbd', 'DocSorpbd'),
        ('SoftwareRegistrationCertificate', 'SoftwareRegistrationCertificate'),
    ]

    FIELD_CHOICES = {

        'Dissertation': ['title', 'speciality_codes', 'science_fields', 'organization', 'location'],
        'DocSorpbd': ['database_name', 'request_number', 'registration_certificate_number'],
        'SoftwareRegistrationCertificate': ['software_name', 'request_number', 'certificate_number'],
    }
    table = forms.ChoiceField(choices=TABLE_CHOICES)
    field = forms.ChoiceField(choices=[])
    search_text = forms.CharField(max_length=100)