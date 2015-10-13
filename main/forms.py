from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div
from crispy_forms.bootstrap import FormActions
from main.models import Cereal, Manufacturer


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)

    # args (arguments) are variables, eg, val
    # key-word args (kwargs) are variables and a value, eg val2="something"
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/contact_view/'
        self.helper.layout = Layout(
                Div('name', 'email', 'phone',
                    css_class='col-md-6 col-lg-6'),
                Div('message', css_class='col-md-6 col-lg-6')
            )
        self.helper.layout.append(
            FormActions(
                Submit('submit', 'Submit', css_class="btn-primary")
                )
            )


class UserSignUp(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

    def __init__(self, *args, **kwargs):
        super(UserSignUp, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/signup/'
        self.helper.layout = Layout(
                    'first_name',
                    'last_name',
                    'username',
                    'email',
                    'password',
                    )
        self.helper.layout.append(
            FormActions(
                Submit('submit', 'Create New User', css_class="btn-primary")
                )
            )


class CerealEditForm(forms.ModelForm):
    class Meta:
        model = Cereal
        # fields = '__all__'
        # if I don't want all fields: fields = ['name', 'county', 'state'] etc
        fields = ['name',
                  'manuf',
                  'cer_type',
                  'calories',
                  'protein',
                  'fat',
                  'sodium',
                  'fiber',
                  'carbs',
                  'sugars',
                  'potassium',
                  'vits_mins',
                  'ss_weight',
                  'cups_per_s',
                  ]

    def __init__(self, *args, **kwargs):
        super(CerealEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/cereal_edit/%s/' % self.instance.pk
        self.helper.layout.append(
            FormActions(
                Submit('save_changes', 'Save Changes',
                       css_class="btn-primary"),
                )
            )


class CerealCreateForm(forms.ModelForm):
    class Meta:
        model = Cereal
        fields = ['name',
                  'manuf',
                  'cer_type',
                  'calories',
                  'protein',
                  'fat',
                  'sodium',
                  'fiber',
                  'carbs',
                  'sugars',
                  'potassium',
                  'vits_mins',
                  'ss_weight',
                  'cups_per_s',
                  ]
        labels = {
                  'name': 'Cereal Name',
                  'manuf': 'Manufacturer',
                  'cer_type': 'Hot (H) or Cold (C) Cereal',
                  'calories': 'Calories',
                  'protein': 'Protein',
                  'fat': 'Fat',
                  'sodium': 'Sodium',
                  'fiber': 'Fiber',
                  'carbs': 'Carbohydrates',
                  'sugars': 'Sugars',
                  'potassium': 'Potassium',
                  'vits_mins': 'Vitamins and Minerals',
                  'ss_weight': 'Serving Size Weight',
                  'cups_per_s': 'Serving Size Volume (cups)',
                  }

    def __init__(self, *args, **kwargs):
        super(CerealCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/cereal_create/'
        self.helper.layout = Layout(
                Div('name', 'manuf', 'cer_type', 'ss_weight', 'cups_per_s',
                    css_class='col-md-6 col-lg-6'),
                Div('calories', 'protein', 'fat', 'sodium', 'fiber',
                    css_class='col-md-3 col-lg-3'),
                Div('carbs', 'sugars', 'potassium', 'vits_mins',
                    css_class='col-md-3 col-lg-3')
            )
        self.helper.layout.append(
            FormActions(
                Submit('submit_new_cereal', 'Submit new cereal',
                       css_class="btn-primary button-padding"),
                )
            )


class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(UserLogin, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/signup/'
        self.helper.layout = Layout(
                    'username',
                    'password',
                    )
        self.helper.layout.append(
            FormActions(
                Submit('submit', 'Log In', css_class="btn-primary")
                )
            )
