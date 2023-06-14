from django.db.models import Count
from django.db.models.functions import Trunc
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Covidians
from .forms import CovidiansForm
import plotly.graph_objects as go


def covid_app(request):
    #test = "To jest cos we views"

    #return HttpResponse("<h1>1st test</h1>")
    #return render(request, "covidians.html", {'text': test})# trzeci jest obiekt ktorego parametrem text jest test
    #dajemy to o co spytalismy w funkcji
    #return render(request, "covidians.html", {'text':["USER1","USER2"]})
    queryset = Covidians.objects.values('user_created_at').annotate(count=Count('id')).order_by('user_created_at')
    print('queryset', queryset)
    return render(request, "covidians.html", {'covidians': queryset})

def new_user(request):
    form = CovidiansForm(request.POST or None, request.FILES or None) #na stronei mogą byc 2 opcje wczytujemy stronę
    # i ona jest pusta bo nie ma post request i wyswietlamy zwyklą stronę,2 opcja request files or none strona pobiera zawartosc formularza
    # i wyswielta jako post. Jeśli jest POST to go akceptujemy lub ignorujemy i Files pliki musza byc przesylane osobno
    if form.is_valid():
        form.save()


    return render(request, 'new_user.html', {'form': form}) #request to co przekazalismy a new-user to nowa tempaltka to template, a przekazujemy form. Pierwsze wyswietlenie form pusty drugi submit zadziała i sie wypelni

def edit_user(request, id):     #funckja do edytowania userow
    covidian = get_object_or_404(Covidians, pk=id) #jaki obiekt ma byc podany i po czym szukamy czyli po id i to nasze pk jak brak obiektu to 404
    form = CovidiansForm(request.POST or None, request.FILES or None, instance=covidian)  # na stronei mogą byc 2 opcje wczytujemy stronę
    # i ona jest pusta bo nie ma post request i wyswietlamy zwyklą stronę,2 opcja request files or none strona pobiera zawartosc formularza
    # i wyswielta jako post. Jeśli jest POST to go akceptujemy lub ignorujemy i Files pliki musza byc przesylane osobno
    #do form wrzucamy instacnję covidianform bedzie wypełnion ydanymi z covidian Możemy użyć tego samego emplate do edycji co dla nowego uzytkownika

    if form.is_valid():
        form.save()
        return redirect(covid_app)  #jak form zostanie zapisany i mamy POST to rpzechodzimy do covid_app w przeciwnym wypadku
    # return renderponizej


    return render(request, 'new_user.html', {'form': form}) #request to co przekazalismy a new-user tonowa tempaltka to template, a przekazujemy form. Pierwsze wyswietlenie form pusty drugi submit zadziała i sie wypelni


def delete_user(request, id):     #funckja do edytowania userow
    covidian = get_object_or_404(Covidians, pk=id) #ja obiekt isntieje to przypisuje go do zmiennej a jak brak obiektu to 404

    if request.method == "POST": #czy to co wysłałem z template jest post jak nie to wyswietlam stronę normalną jak jest POST to delete metoda jest post jak w template html jest post
        covidian.delete()
        return redirect(covid_app) #jak skasuje to przejdz dow szstkich userow

    return render(request, 'confirm.html', {'covidian': covidian}) #request to co przekazalismy a new-user tonowa tempaltka to template, a przekazujemy



def dashboard(request):
    #for elements in covid_app.queryset:
    #    print(elements)

    # points = Point.objects.all()
    print('xyz')
    queryset = Covidians.objects.values('user_created_at').annotate(count=Count('id')).order_by('user_created_at')
    x_date = [point['user_created_at'] for point in queryset]
    y_date = [point['count'] for point in queryset]
    fig = go.Figure(data=go.Scatter(x=x_date, y=y_date))
    fig.update_layout(
        xaxis=dict(
            tickmode='auto',
            nticks=len(x_date)
        ),
        yaxis=dict(
            tickmode='linear',
            dtick=1
        )
    )

    plot_div = fig.to_html(full_html=False)

    context = {
        'name': "The Covid users counter graphics",
        'plot_div': plot_div
    }
    #
    return render(request, 'dashboard.html', context=context)



"""

    #objects_per_date = Covidians.objects.annotate(created_date=Trunc('user_created_at', 'date')).values('created_date').annotate(count=Count('id'))
    #print(objects_per_date)
    #points = Point.objects.all()
    #x_date = [1, 2, 3, 4, 5, 6]
    #y_date = [1, 4, 9, 16, 25, 36]


    #points = Point.objects.all()
    #x_date = [point.x for point in points]
    #y_date = [point.y for point in points]

    #fig = go.Figure(data=go.Scatter(x=x_date, y=y_date))

    #plot_div = fig.to_html(full_html=False)

    context = {
        'name': "The Covid users counter graphics",
        'plot_div': plot_div
    }
    return render(request, 'dashboard.html', context=context)
"""
