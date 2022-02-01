import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import csv
import numpy as np

#Initialisation du DashBoard
app = dash.Dash(__name__)

#Dictionnaire de traduction des mois numériques en lettres. Ceci permet un affichage plus esthétique des sliders.
mounth_trad = {
"1":"Janvier",
"2":"Février",
"3":"Mars",
"4":"Avril",
"5":"Mai",
"6":"Juin",
"7":"Juillet",
"8":"Août",
"9":"Septembre",
"10":"Octobre",
"11":"Novembre",
"12":"Décembre"
}

###                    ###
# Traitement des données #
###                    ###
def create_new_set():
    """
    Fonction de traitement du data_set, élimination des données inexploitables, sommes des transactions par pays par mois.

    Return une pandas.Dataframe.
    """
    returned_data = {}
    for index,var in data_set.iterrows():
        if (var["Pays"] in returned_data.keys()):
            if (var["Mois"] in returned_data[var["Pays"]].keys()):
                returned_data[var["Pays"]][var["Mois"]][0] += var["Valeur"]
                returned_data[var["Pays"]][var["Mois"]][1] += var["Masse"]
            else:
                returned_data[var["Pays"]].update({var["Mois"] : [var["Valeur"],var["Masse"],str(var["coordonnees_pays"]).split(",")[0],str(var["coordonnees_pays"]).split(",")[1]]})
        else:
                returned_data[var["Pays"]] = dict([(var['Mois'],[var['Valeur'],var['Masse'],str(var["coordonnees_pays"]).split(",")[0],str(var["coordonnees_pays"]).split(",")[1]])])

    new_data_set = pd.DataFrame(columns=["Pays","Mois","Valeurs","Masse","Longitude","Latitude"])
    for country in returned_data.keys():
        for mounth in returned_data[country].keys():
            new_data_set = new_data_set.append({"Pays":country,"Mois":mounth,"Valeurs":returned_data[country][mounth][0],
            "Masse":returned_data[country][mounth][1],"Longitude":returned_data[country][mounth][3],"Latitude":returned_data[country][mounth][2]},ignore_index=True)
            new_data_set = new_data_set.sort_values(by=["Pays","Mois"])
            new_data_set = new_data_set.dropna()
    return  new_data_set

# La boucle suivante permet d'éviter les processus de traitement de donnée si celle-ci a déjà été traité en vérifiant si le ficher new_data.csv existe.
try:
    csv_file = 'new_data.csv'
    new_data_set = pd.read_csv(csv_file,delimiter=";",index_col=0)
except FileNotFoundError:
    csv_file = 'data.csv'
    data_set = pd.read_csv(csv_file,delimiter=";")
    index_2019 = data_set[data_set['Année'] == '2019'].index
    data_set.drop(index_2019,inplace=True)
    data_set = data_set.dropna()
    new_data_set = create_new_set()
    new_data_set.to_csv("new_data.csv",sep=";")


###                    ###
# Création du DashBoard  #
###                    ###

#Dictionnaire de couleur pour faciliter la mise en page.
colors = {'background' : '#292929',
'text':'#7FDBFF'
}

#Création de la page globale du DashBoard qui va contenir tous les autres éléments.
app.layout = html.Div(style={'backgroundColor':colors['background']},children=[

#Première division correspondant à la première ligne du DashBoard contenant:
# - le titre
# - le dropdown du graphique en barre
# - le graphique en barre
# - le slider
# Les éléments sont placés dans des sous divisions html afin de faciliter la mise en page.
    html.Div([
    html.H1(
        children='Export mondial Français : 2018.',
        style={'textAlign' : 'center','color':colors['text']}
        ),

          
    html.Div(style={'color':colors['text'],'backgroundColor':colors['background'],"width":"30%"},children=[
        html.P(children="Valeur/Masse",className='value_text_left'),
        dcc.Dropdown(
            id = "drop_1",
            options=[{"value":"Valeurs", "label":"Valeurs"},{"value":"Masse","label":"Masse"}],
            optionHeight = 25,
            value = "Valeurs",
            className='select_box'
        ),
    ]),
    dcc.Graph(
        id='values-graph',
        figure={}
    ),
    html.Div(style={"width":"50%",'margin':'auto'},children=[
    dcc.Slider(
        id = 'mounth-slider_1',
        min=new_data_set['Mois'].min(),
        max=new_data_set['Mois'].max(),
        value=new_data_set['Mois'].min(),
        marks={str(mois): {'label': mounth_trad[str(mois)],'style' : {'color':colors["text"]}} for mois in new_data_set['Mois'].unique()},
        step=None
            )
        ]),
    ]),

#Deuxième division correspondant à la deuxième ligne du DashBoard contenant:
# - les 2 dropdowns de l'histogramme
# - le dropdown de la carte
# - l'histogramme
# - la carte
# - le slider de la l'histogramme
# - le slider de la carte
# Les éléments sont placés dans des sous divisions html afin de faciliter la mise en page.
    html.Div(className='row',children=[
        html.Div(style={'color':colors['text'],'backgroundColor':colors['background'],"width":"15%",'display': 'inline-block'},children=[
        html.P(children="Valeur/Masse",className='value_text_left'),
            dcc.Dropdown(
                id = "drop_2",
                options=[{"value":"Valeurs", "label":"Valeurs"},{"value":"Masse","label":"Masse"}],
                optionHeight = 25,
                value = "Valeurs",
                className='select_box'
            ),
        ]),
        html.Div(style={'color':colors['text'],'backgroundColor':colors['background'],'display': 'inline-block'},children=[
        html.P(children="Echelle",className='value_text_left'),
            dcc.Dropdown(
                id = "drop_range",
                options=[{"value":15000000000, "label":"15B"},{"value":10000000000,"label":"10B"},{"value":5000000000, "label":"5B"},{"value":1000000000,"label":"1B"}
                ,{"value":500000000, "label":"500M"},{"value":250000000,"label":"250M"},{"value":125000000, "label":"125M"},{"value":100000000,"label":"100M"}
                ,{"value":50000000, "label":"50M"},{"value":10000000,"label":"10M"}],
                optionHeight = 25,
                value = 15000000000,
                className='select_box_mid'
            ),
        ]),
        html.Div(style={'color':colors['text'],'backgroundColor':colors['background'],"width":"30%",'display': 'inline-block'},children=[
        html.P(children="Valeur/Masse",className='value_text_right'),
            dcc.Dropdown(
                id = "drop_3",
                options=[{"value":"Valeurs", "label":"Valeurs"},{"value":"Masse","label":"Masse"}],
                optionHeight = 25,
                value = "Valeurs",
                className='select_box_right'
            ),
        ]),
        dcc.Graph(
            id="histo-graph",
            figure={},
            style={
                    "width": "50%",
                    'display': 'inline-block'}
        ),
        dcc.Graph(
            id='map-graph',
            figure={},
            style={
                    "width" : "50%",
                    'display': 'inline-block'}
        ),
        html.Div(style={"width":"50%",'display': 'inline-block'},children=[
            dcc.Slider(
        id = 'mounth-slider_2',
        min=new_data_set['Mois'].min(),
        max=new_data_set['Mois'].max(),
        value=new_data_set['Mois'].min(),
        marks={str(mois): {'label': mounth_trad[str(mois)],'style' : {'color':colors["text"]}} for mois in new_data_set['Mois'].unique()},
        step=None)]
                ),
        html.Div(style={"width":"50%",'display': 'inline-block'},children=[
            dcc.Slider(
        id = 'mounth-slider_3',
        min=new_data_set['Mois'].min(),
        max=new_data_set['Mois'].max(),
        value=new_data_set['Mois'].min(),
        marks={str(mois): {'label': mounth_trad[str(mois)],'style' : {'color':colors["text"]}} for mois in new_data_set['Mois'].unique()},
        step=None)]
                )
    ]),
#Dernière division correspondant à la troisième ligne du DashBoard contenant:
# - l'interval résponsable de l'animation du graphique
# - le graphique de point
# - le bouton Play/Stop
# - le slider du graphique de point
# Les éléments sont placés dans des sous divisions html afin de faciliter la mise en page.
    html.Div([
        dcc.Interval(id="animate",disabled=True,interval=1000,n_intervals=0),
        dcc.Graph(
            id="scatter-graph",
            figure={}
        ),
        html.Button('Play/Stop',id='play_button',n_clicks=0,className = "button"),

        html.Div(style={"width":"50%",'margin':'auto','display': 'inline-block'},children=[
            dcc.Slider(
        id = 'mounth-slider_4',
        min=new_data_set['Mois'].min(),
        max=new_data_set['Mois'].max(),
        value=new_data_set['Mois'].min(),
        marks={str(mois): {'label': mounth_trad[str(mois)],'style' : {'color':colors["text"]}} for mois in new_data_set['Mois'].unique()},
        step=None)]
                )
    ])
#Afin d'ajouter du contenu au DashBoard, il suffit de recréer une division HTML en dessous et l'agrémenter de graphiques et autres Input.
#Si vous ajoutez des graphiques dynamiques n'oubliez pas de configurer les "callback" et fonctions associées.
])

###                                   ###
# Callback, Graphiques et interactivité #
###                                   ###


#Callback du dropdown et slider pour le graphique en barre.
@app.callback(
    Output('values-graph','figure'),
    Input('mounth-slider_1','value'),
    Input('drop_1','value')
)

def update_bar_graph(selected_mounth,selected_value):
    """
    Calcul nécéssaire à la création et à l'update du graphique en barre.

    Keyword arguments:
    selected_mounth -- le mois séléctionné à l'aide du slider.
    selected_value -- la valeur séléctionné à l'aide du dropdown.
    """
    mounth_data = new_data_set[new_data_set["Mois"] == selected_mounth]
    if(selected_value == "Valeurs"):
        label = "valeur(€)"
    else:
        label = "masse(Kg)"
    fig = px.bar(mounth_data, x = "Pays",y=selected_value,title="Graphique en barre des exports Français en " + label +" pour chaque pays par mois.")
    fig.update_layout(plot_bgcolor = colors["background"],paper_bgcolor = colors["background"],font_color = colors['text'],margin={"r":0,"t":25,"l":0,"b":25},transition_duration = 500)
    return fig

#Callback des dropdown et du slider pour l'histogramme'.
@app.callback(
    Output('histo-graph','figure'),
    Input('mounth-slider_2','value'),
    Input('drop_2','value'),
    Input('drop_range','value')
)

def update_histo_graph(selected_mounth,selected_value,selected_range):
    """
    Calcul nécéssaire à la création et à l'update de l'histogramme.

    Keyword arguments:
    selected_mounth -- le mois séléctionné à l'aide du slider.
    selected_value -- la valeur séléctionné à l'aide du dropdown.
    selected_range -- la valeur d'échelle séléctionné à l'aide du deuxième dropdown.
    """
    mounth_data = new_data_set[new_data_set["Mois"] == selected_mounth]
    if(selected_value == "Valeurs"):
        label = "valeur(€)"
    else:
        label = "masse(Kg)"
    histogram = px.histogram(mounth_data[mounth_data[selected_value]<selected_range],x=selected_value,title="Nombre de pays par tranche de " + label + " des exports par mois.")
    histogram.update_layout(plot_bgcolor = colors["background"],paper_bgcolor = colors["background"],font_color = colors['text'],margin={"r":25,"t":50,"l":0,"b":25},transition_duration = 500)
    return histogram

#Callback du dropdown et du slider pour la carte'.
@app.callback(
    Output('map-graph','figure'),
    Input('mounth-slider_3','value'),
    Input('drop_3','value')
)

def update_map_graph(selected_mounth,selected_value):
    """
    Calcul nécéssaire à la création et à l'update de la carte.

    Keyword arguments:
    selected_mounth -- le mois séléctionné à l'aide du slider.
    selected_value -- la valeur séléctionné à l'aide du dropdown.
    """
    mounth_data = new_data_set[new_data_set["Mois"] == selected_mounth]
    if(selected_value == "Valeurs"):
        label = "valeur(€)"
    else:
        label = "masse(Kg)"
    map = px.scatter_geo(mounth_data,lon = "Longitude",
    lat = "Latitude",
    locationmode="ISO-3",
    hover_name="Pays",
    size = selected_value,
    color = selected_value, color_continuous_scale = "deep",
    title = "Carte des exports mondiaux Français en " + label + " par mois.")
    map.update_layout(plot_bgcolor = colors["background"],paper_bgcolor = colors["background"],font_color = colors['text'],margin={"r":25,"t":50,"l":0,"b":25},transition_duration = 500)
    return map

#Callback du slider pour le graphique de point'.
@app.callback(
    Output('scatter-graph','figure'),
    Input('mounth-slider_4','value'),
)

def update_scatter_graph(selected_mounth):
    """
    Calcul nécéssaire à la création et à l'update du graphique de point.

    Keyword arguments:
    selected_mounth -- le mois séléctionné à l'aide du slider.
    """
    mounth_data = new_data_set[new_data_set["Mois"] == selected_mounth]
    scatter_fig = px.scatter(mounth_data,x = "Valeurs", y = "Masse",hover_name='Pays',title="Graphique de la valeur(€) en fonction de la masse(Kg) pour chaque pays par mois.",size="Valeurs",color = "Valeurs", color_continuous_scale = "deep")
    scatter_fig.update_layout(plot_bgcolor = colors["background"],paper_bgcolor = colors["background"],font_color = colors['text'],margin={"r":25,"t":50,"l":0,"b":25},transition_duration = 500,yaxis_range=[0,8000000000],xaxis_range=[0,15000000000])
    return scatter_fig

#Callback du bouton pour mettre en On/Off l'intervals'.
@app.callback(
    Output('animate','disabled'),
    Input('play_button','n_clicks'),
    State('animate','disabled')
)

def toggle(n,playing):
    """
    Interaction On/Off du bouton sur l'intervals.

    Keyword arguments:
    n -- l'event du click relatif au bouton'.
    playing -- boolean permettant la mise en marche où non de l'intervalls.
    """
    if n:
        return not playing
    return playing

#Callback de l'intervals sur slider du graphique en point'.
@app.callback(
    Output('mounth-slider_4','value'),
    Input('animate','n_intervals')
)

def animate(n_intervals):
    """
    Animation du slider controlé par un intervals de 1sec.

    Keyword arguments:
    n_intervals -- Paramètres de l'intervals augmentant à chaque tick pour faire varier le slider.
    """
    if n_intervals is None:
        return 0
    else:
        return (n_intervals+1)%new_data_set['Mois'].max()

#Main démarage du serveur DashBoard.
if __name__ == '__main__':
    app.run_server(debug=True)