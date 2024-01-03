import folium
from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def my_first_view(request: HttpRequest):
    m = folium.Map(
                location=(42.6654086, 23.2597745),
                # zoom_start=20,
                tiles="OpenStreetMap"
                   )
    folium.Marker(
        location=[42.6654086, 23.2597745],
        tooltip="Zenobia Baby",
        popup="Zenobia Baby",
        icon=folium.Icon(icon="heart"),
    ).add_to(m)
    folium.Marker(
        location=[42.6531609, 23.365499],
        tooltip="KFC",
        popup="MMMMMMMMMMMMMMMMMMMMMMMM KFC",
        icon=folium.Icon(icon="drumstick-bite", color="red", icon_color="white", prefix="fa", angle=45),

    ).add_to(m)

    context = {
        "map": m._repr_html_()
    }
    return render(request=request, template_name='index.html', context=context)
