from django.shortcuts import render
from .forms import ZCriteriaForm, SampleForm, NpsForm
from math import sqrt


def calc_error(form):
    values = {
        '80%': '1.2815515655',
        '90%': '1.6448536270',
        '95%': '1.9599639845',
        '99%': '2.5758293035',
    }

    z = form.cleaned_data['prob']
    zp = float(values[z])

    u = form.cleaned_data['u']
    sam = form.cleaned_data['sample']
    gen = form.cleaned_data['gen_sample']

    answer = zp * sqrt((u ** 2 / sam) * (1 - sam / gen))

    return round(answer, 2)


def sample(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            context = {
                'title': 'sample-c',
                'answer': calc_error(form),
                'form': form,
            }
            return render(request, 'calculators/sample.html', context)
    else:
        form = SampleForm()

    context = {
        'title': 'sample',
        'form': form,
    }

    return render(request, 'calculators/sample.html', context)


def z_calc(form):
    values = {
        '80%': '1.2815515655',
        '90%': '1.6448536270',
        '95%': '1.9599639845',
        '99%': '2.5758293035',
    }

    perc_1 = form.cleaned_data['perc_1'] / 100
    perc_2 = form.cleaned_data['perc_2'] / 100
    sample_1 = form.cleaned_data['sample_1']
    sample_2 = form.cleaned_data['sample_2']

    first = ((perc_1) * (1 - perc_1)) / sample_1
    second = ((perc_2) * (1 - perc_2)) / sample_2

    z = abs(perc_1 - perc_2) / (sqrt(first + second))

    answer = {}

    for k, v in values.items():
        if z > float(v):
            answer[k] = 'Sig. diff'
        else:
            answer[k] = 'No sig. diff'

    return answer


def z_criteria(request):
    if request.method == 'POST':
        form = ZCriteriaForm(request.POST)
        if form.is_valid():
            context = {
                'title': 'z_criteria',
                'answer': z_calc(form),
                'form': form,
            }
            return render(request, 'calculators/z_criteria.html', context)
    else:
        form = ZCriteriaForm()

    context = {
        'title': 'z_criteria',
        'form': form,
    }

    return render(request, 'calculators/z_criteria.html', context)


def nps_calc(form):
    values = {
        '80%': '1.2815515655',
        '90%': '1.6448536270',
        '95%': '1.9599639845',
        '99%': '2.5758293035',
    }

    crit1 = form.cleaned_data['crit1']
    neut1 = form.cleaned_data['neut1']
    prom1 = form.cleaned_data['prom1']
    crit2 = form.cleaned_data['crit2']
    neut2 = form.cleaned_data['neut2']
    prom2 = form.cleaned_data['prom2']

    base1 = crit1 + neut1 + prom1
    nps1 = round(100 * ((prom1 / base1) - (crit1 / base1)), 2)

    base2 = crit2 + neut2 + prom2
    nps2 = round(100 * ((prom2 / base2) - (crit2 / base2)), 2)

    average1 = ((1 * prom1) + (-1 * crit1)) / base1
    average2 = ((1 * prom2) + (-1 * crit2)) / base2

    p1 = (1 - average1) ** 2
    n1 = (0 - average1) ** 2
    k1 = (-1 - average1) ** 2

    p2 = (1 - average2) ** 2
    n2 = (0 - average2) ** 2
    k2 = (-1 - average2) ** 2

    s1 = (((p1 * prom1) + (n1 * neut1) + (k1 * crit1)) / (base1 - 1)) ** 0.5
    s2 = (((p2 * prom2) + (n2 * neut2) + (k2 * crit2)) / (base2 - 1)) ** 0.5

    se1 = s1 / (base1 ** 0.5)
    se2 = s2 / (base2 ** 0.5)

    z = abs((average1 - average2) / sqrt((se1 ** 2) + (se2 ** 2)))

    answer = {'npsmeans': {'nps1': f'NPS1 -> {nps1}', 'nps2': f'NPS2 -> {nps2}'},
              'sig': {},
              }

    for k, v in values.items():
        if z > float(v):
            answer['sig'][k] = 'Sig. diff'
        else:
            answer['sig'][k] = 'No sig. diff'

    return answer


def nps(request):
    if request.method == 'POST':
        form = NpsForm(request.POST)
        if form.is_valid():
            calculate = nps_calc(form)
            context = {
                'title': 'nps',
                'answer': calculate['sig'],
                'nps1': calculate['npsmeans']['nps1'],
                'nps2': calculate['npsmeans']['nps2'],
                'form': form,
            }
            return render(request, 'calculators/nps.html', context)
    else:
        form = NpsForm()

    context = {
        'title': 'nps',
        'form': form,
    }
    return render(request, 'calculators/nps.html', context)
