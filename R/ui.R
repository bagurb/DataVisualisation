#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(shinydashboard)
library(tidyverse)
library(plotly)
library(ggplot2)
library(dplyr)
library(leaflet)

# Define UI for application

    # Sidebar et définition des items qu'elle contient sur le dashboard.
    sidebar <- dashboardSidebar(
        sidebarMenu(
        menuItem(" Valeurs monétaires (€)", tabName = "valeursId", icon=icon("euro-sign")),
        menuItem(" Volumes (Kg)", tabName = "masseId", icon=icon("weight-hanging"))
        )
    )
    
    # Corps du dashboard pour chaque items de la sidebar. Permettant le changement de page suivant l'item séléctionné.
    body <- dashboardBody(
        tabItems(
        #TabItem présentant les graphiques pour les valeurs monétaires.
        tabItem(tabName = "valeursId",
            #Affichage du graphique en barre.
            box(
                title = "Graphique en barre des exports Français en valeurs(€) pour chaque pays par mois.",
                status= "info",
                solidHeader = TRUE,
                width = 500,
                plotlyOutput("bargraphvaleurs"),
                #Slider du choix du mois pour le graphique en barre, input utilisée dans server.R.
                sliderInput("Mois_bar_valeurs","Choisissez un Mois:",min= min(data_set$Mois),max=max(data_set$Mois),value= min(data_set$Mois),step=1)
            ),
            #Affichage de l'histogramme.
            box(
                title = "Nombre de pays par tranche de valeurs(€) des exports par mois.",
                status= "info",
                solidHeader = TRUE,
                width = 6,
                height = 700,
                
                #Dropdown de l'échelle de l'histogramme, input utilisée dans server.R.
                selectInput("Scale_histo_valeurs","Choisissez une échelle:",choices = c("15000000000","10000000000","5000000000","1000000000",
                                                                                "500000000","250000000","125000000","100000000","50000000","10000000")),
                plotlyOutput("histographvaleurs"),
                #Slider du choix du mois pour l'histogramme, input utilisée dans server.R.
                sliderInput("Mois_histo_valeurs","Choisissez un Mois:",min= min(data_set$Mois),max=max(data_set$Mois),value= min(data_set$Mois),step=1)
            ),
            #Affichage de la carte.
            box(
                title = "Carte des exports en valeurs(€) par Mois.",
                status= "info",
                solidHeader = TRUE,
                width = 6,
                height = 700,
                leafletOutput("map_geo_valeurs"),
                #Slider du choix du mois pour la carte, input utilisée dans server.R.
                sliderInput("Mois_map_valeurs","Choisissez un Mois:",min= min(data_set$Mois),max=max(data_set$Mois),value= min(data_set$Mois),step=1)
            ),
            #Affichage du pie chart.
            box(
                title = "Graphique des principaux pays importateurs de produits Français en valeurs(€) par mois.",
                status= "info",
                solidHeader = TRUE,
                width = 6,
                
                plotlyOutput("piegraphvaleurs"),
                #Slider du choix du mois pour le pie chart. input utilisée dans server.R.
                sliderInput("Mois_pie_valeurs","Choisissez un Mois:",min= min(data_set$Mois),max=max(data_set$Mois),value= min(data_set$Mois),step=1)
            ),
            #Affichage du graphique de point.
            box(
                title = "Graphique de la valeurs(€) par rapport aux volumes(Kg) des exports par pays par mois.",
                status= "info",
                solidHeader = TRUE,
                width = 6,
                plotlyOutput("scattergraphvaleurs"),
                #Slider du choix du mois pour le graphique de point. input utilisée dans server.R.
                sliderInput("Mois_scatter_valeurs","Choisissez un Mois:",min= min(data_set$Mois),max=max(data_set$Mois),value= min(data_set$Mois),step=1)
            )  
        )
        ,
        #TabItem présentant les graphiques pour les volumes.
        tabItem(tabName = "masseId",
                #Affichage du graphique en barre.
                box(
                    title = "Graphique en barre des exports Français en volumes(Kg) pour chaque pays par mois.",
                    status= "info",
                    solidHeader = TRUE,
                    width = 500,
                    plotlyOutput("bargraphmasses"),
                    #Slider du choix du mois pour le graphique en barre, input utilisée dans server.R.
                    sliderInput("Mois_bar_masses","Choisissez un Mois:",min= min(data_set$Mois),max=max(data_set$Mois),value= min(data_set$Mois),step=1)
                ),
                #Affichage de l'histogramme.
                box(
                    title = "Nombre de pays par tranche de volumes(Kg) des exports par mois.",
                    status= "info",
                    solidHeader = TRUE,
                    width = 6,
                    height = 700,
                    #Dropdown de l'échelle de l'histogramme, input utilisée dans server.R.
                    selectInput("Scale_histo_masses","Choisissez une échelle:",choices = c("15000000000","10000000000","5000000000","1000000000",
                                                                                    "500000000","250000000","125000000","100000000","50000000","10000000")),
                    plotlyOutput("histographmasses"),
                    #Slider du choix du mois pour l'histogramme, input utilisée dans server.R.
                    sliderInput("Mois_histo_masses","Choisissez un Mois:",min= min(data_set$Mois),max=max(data_set$Mois),value= min(data_set$Mois),step=1)
                ),
                #Affichage de la carte.
                box(
                    title = "Carte des exports en volumes(Kg) par Mois.",
                    status= "info",
                    solidHeader = TRUE,
                    width = 6,
                    height = 700,
                    leafletOutput("map_geo_masses"),
                    #Slider du choix du mois pour la carte, input utilisée dans server.R.
                    sliderInput("Mois_map_masses","Choisissez un Mois:",min= min(data_set$Mois),max=max(data_set$Mois),value= min(data_set$Mois),step=1)
                ),
                #Affichage du pie chart.
                box(
                    title = "Graphique des principaux pays importateurs de produits Français en volumes(Kg) par mois.",
                    status= "info",
                    solidHeader = TRUE,
                    width = 6,

                    plotlyOutput("piegraphmasses"),
                    #Slider du choix du mois pour le pie chart. input utilisée dans server.R.
                    sliderInput("Mois_pie_masses","Choisissez un Mois:",min= min(data_set$Mois),max=max(data_set$Mois),value= min(data_set$Mois),step=1)
                ),
                #Affichage du graphique de point.
                box(
                    title = "Graphique de la valeurs(€) par rapport aux volumes(Kg) des exports par pays par mois.",
                    status= "info",
                    solidHeader = TRUE,
                    width = 6,
                    plotlyOutput("scattergraphmasses"),
                    #Slider du choix du mois pour le graphique de point. input utilisée dans server.R.
                    sliderInput("Mois_scatter_masses","Choisissez un Mois:",min= min(data_set$Mois),max=max(data_set$Mois),value= min(data_set$Mois),step=1)
                )

            )
        
        
        )
    )
    shinyUI(dashboardPage(
        #Header de la page Dashboard contenant le titre.
        dashboardHeader(
            title = "Exports Mondiaux Français: 2018",
            titleWidth = 500
        ),
        sidebar,
        body
        ))
