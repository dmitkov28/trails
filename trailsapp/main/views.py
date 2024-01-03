import folium
from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def my_first_view(request: HttpRequest):
    m = folium.Map(location=(42.6654086, 23.2597745), zoom_start=20, tiles="cartodb positron")
    folium.Marker(
        location=[42.6654086, 23.2597745],
        tooltip="Zenobia Baby",
        popup="Zenobia Baby",
        icon=folium.Icon(icon="heart"),
    ).add_to(m)

    context = {
        "map": m._repr_html_()
    }
    return render(request=request, template_name='index.html', context=context)
