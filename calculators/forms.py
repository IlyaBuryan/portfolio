from django import forms


class ZCriteriaForm(forms.Form):
    perc_1 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'input_field'}), label="1-st %")
    sample_1 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'input_field'}), label="1-st sample")
    perc_2 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'input_field'}), label="2-d %")
    sample_2 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'input_field'}), label="2-d sample")

    def clean(self):
        cleaned_data = super().clean()
        perc_1 = cleaned_data['perc_1']
        perc_2 = cleaned_data['perc_2']
        sample_1 = cleaned_data['sample_1']
        sample_2 = cleaned_data['sample_2']

        if (perc_1 < 0 or perc_1 > 100) or (perc_2 < 0 or perc_2 > 100):
            self.add_error('perc_1', 'Input error. \"%\" must be from 0 to 100')
        if perc_1 == perc_2:
            self.add_error('perc_1', 'Input error. \"%\" must not be equal')
        if sample_1 < 0 or sample_2 < 0:
            self.add_error('perc_1', 'Input error. \"Sample\" must be >0')


class SampleForm(forms.Form):
    prob = forms.CharField(widget=forms.RadioSelect(
        choices=[
            ('80%', '80%'),
            ('90%', '90%'),
            ('95%', '95%'),
            ('99%', '99%'),
        ]),
        required='required',
        label='Probability')
    sample = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'input_field'}), label="Sample")
    u = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'input_field', 'value': '50'}),
                         label="%")
    gen_sample = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'input_field', 'value': '140000000'}),
                                  label="General population")

    def clean(self):
        cleaned_data = super().clean()

        sample = cleaned_data['sample']
        u = cleaned_data['u']
        gen_sample = cleaned_data['gen_sample']

        if gen_sample < sample:
            self.add_error('sample', 'The sample is lesser than GP')
        if sample <= 0:
            self.add_error('sample', 'Input error. Must be > 0')
        if gen_sample <= 0:
            self.add_error('gen_sample', 'Input error. Must be > 0')
        if u < 0 or u > 100:
            self.add_error('u', 'Input error. Must be from 0 to 100')


class NpsForm(forms.Form):
    crit1 = forms.FloatField(widget=(forms.NumberInput(attrs={'class': 'input_field', 'placeholder': 'Critics 0-6'})))
    neut1 = forms.FloatField(
        widget=(forms.NumberInput(attrs={'class': 'input_field', 'placeholder': 'Neutralists 7-8'})))
    prom1 = forms.FloatField(
        widget=(forms.NumberInput(attrs={'class': 'input_field', 'placeholder': 'Promoters 9-10'})))
    crit2 = forms.FloatField(widget=(forms.NumberInput(attrs={'class': 'input_field', 'placeholder': 'Critics 0-6'})))
    neut2 = forms.FloatField(
        widget=(forms.NumberInput(attrs={'class': 'input_field', 'placeholder': 'Neutralists 7-8'})))
    prom2 = forms.FloatField(
        widget=(forms.NumberInput(attrs={'class': 'input_field', 'placeholder': 'Promoters 9-10'})))

    def clean(self):
        cleaned_data = super().clean()

        var_list1 = [
            cleaned_data['crit1'],
            cleaned_data['neut1'],
            cleaned_data['prom1']
        ]

        var_list2 = [
            cleaned_data['crit2'],
            cleaned_data['neut2'],
            cleaned_data['prom2']
        ]

        if any(i < 0 for i in var_list1):
            self.add_error("crit1", "Input error. Some values < 0")

        if any(i < 0 for i in var_list2):
            self.add_error("crit2", "Input error. Some values < 0")