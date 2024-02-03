import folium
from django.http import HttpRequest
from django.shortcuts import render
from folium.plugins.fullscreen import Fullscreen
from folium.plugins.locate_control import LocateControl
from trailsapp.main.utils.js_button import JsButton


def home_view(request: HttpRequest):
    m = folium.Map(
        location=(42.6654086, 23.2597745), zoom_start=10, tiles="OpenStreetMap"
    )

    LocateControl(auto_start=True, keepCurrentZoomLevel=True).add_to(m)

    Fullscreen(
        position="topright",
        title="Expand me",
        title_cancel="Exit me",
        force_separate_button=True,
    ).add_to(m)

    folium.Marker(
        location=[42.6654086, 23.2597745],
        tooltip="Zenobia Baby",
        popup="Zenobia Baby",
        icon=folium.Icon(icon="heart"),
    ).add_to(m)

    # Add custom JS Button to Map
    JsButton(
        title='<span>Click</span>',
        function="""
    function(btn, map) {
       alert('It works!');
    }
    """,
    ).add_to(m)

    # folium.Marker(
    #     location=[42.656817785193056, 23.34933134976066],
    #     tooltip="Дани локация",
    #     popup="Тука живее Данката",
    #     icon=folium.Icon(icon="leaf", color="red", icon_color="white", prefix="fa"),
    # ).add_to(m)

    folium.Marker(
        location=[42.65463735755751, 23.370681409879392],
        tooltip="KFC",
        popup="MMMMMMMMMMMMMMMMMMMMMMMM KFC",
        icon=folium.Icon(
            icon="drumstick-bite", color="red", icon_color="white", prefix="fa"
        ),
    ).add_to(m)

    context = {"map": m._repr_html_()}

    return render(request=request, template_name="index.html", context=context)
