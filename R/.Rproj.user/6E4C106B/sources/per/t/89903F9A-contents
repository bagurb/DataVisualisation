#
# This is the server logic of a Shiny web application. You can run the
# application by clicking 'Run App' above.
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
# Define server logics
shinyServer(function(input,output){
    
    
    #Interactive Graphs
    #Graphique pour le menu Valeurs.
    
    #Logique du graphique en barre.
    output$bargraphvaleurs <- renderPlotly({
        bargraphvaleurs <- plot_ly(
            mounth_set <- filter(data_set, Mois == input$Mois_bar_valeurs),
            x = mounth_set$Pays,
            y = mounth_set$Valeurs,
            type = "bar")
        bargraphvaleurs <- bargraphvaleurs %>% layout(
                                        xaxis = list(title="Pays"),
                                        yaxis = list(title="Valeurs(€)"))
        bargraphvaleurs
    })
    
    #Logique du graphique de l'histogramme
    output$histographvaleurs <- renderPlotly({
        histographvaleurs <- plot_ly(mounth_set <- filter(data_set, Mois==input$Mois_histo_valeurs&Valeurs<=as.numeric(input$Scale_histo_valeurs)),
                              x = mounth_set$Valeurs,
                              type = "histogram"
        )
        histographvaleurs <- histographvaleurs %>% layout(
                                            xaxis = list(title="Valeurs(€)"),
                                            yaxis = list(title="Nombre de Pays"))
        histographvaleurs
    })
    
    #Logique de la carte
    output$map_geo_valeurs <- renderLeaflet({
        mounth_set <- filter(data_set, Mois == input$Mois_map_valeurs)
        color_pal <- colorQuantile("Reds",mounth_set$Values,n=9)
        map_geo_valeurs <- leaflet() %>%
            addTiles() %>% 
            setView(0, 0, zoom = 1) %>%
            addCircleMarkers(lng=mounth_set$Longitude,lat=mounth_set$Latitude,popup = as.character(mounth_set$Valeurs), label= mounth_set$Pays,
                             color=color_pal(mounth_set$Valeurs),fillOpacity=0.5,radius = sqrt(as.numeric(mounth_set$Valeurs))/5000)%>%
            addLegend(pal = color_pal, values=(as.numeric(mounth_set$Masse)),position = "bottomright")
        map_geo_valeurs
    })
    
    #Logique du pie chart.
    output$piegraphvaleurs <- renderPlotly({
        piegraphvaleurs <- plot_ly(mounth_set <- filter(data_set, Mois==input$Mois_pie_valeurs&Valeurs>=500000000),
                            labels = mounth_set$Pays,values = mounth_set$Valeurs,type="pie"
                            )
        piegraphvaleurs
    })

    
    #Logique du graphique de point.
    output$scattergraphvaleurs <- renderPlotly({
        mounth_set <- filter(data_set, Mois == input$Mois_scatter_valeurs)
        scattergraphvaleurs <- plot_ly(
                           x=mounth_set$Valeurs,y=mounth_set$Masse,text=mounth_set$Pays, size=mounth_set$Valeurs,color=mounth_set$Valeurs,type="scatter",mode="markers")
        scattergraphvaleurs <- scattergraphvaleurs %>% layout(
            xaxis = list(title="Valeurs(€)"),
            yaxis = list(title="Masses(Kg)"))
        scattergraphvaleurs
    })
    
    #Graphique pour le menu masse.
    
    #Logique du graphique en barre.
    output$bargraphmasses <- renderPlotly({
        bargraphmasses <- plot_ly(
            mounth_set <- filter(data_set, Mois == input$Mois_bar_masses),
            x = mounth_set$Pays,
            y = mounth_set$Masse,
            type = "bar")
        bargraphmasses <- bargraphmasses %>% layout(
            xaxis = list(title="Pays"),
            yaxis = list(title="Masses(Kg)"))
        bargraphmasses
    })

    #Logique du graphique de l'histogramme
    output$histographmasses <- renderPlotly({
        histographmasses <- plot_ly(mounth_set <- filter(data_set, Mois==input$Mois_histo_masses&Masse<=as.numeric(input$Scale_histo_masses)),
                              x = mounth_set$Masse,
                              type = "histogram"
        )
        histographmasses <- histographmasses %>% layout(
            xaxis = list(title="Masses(Kg)"),
            yaxis = list(title="Nombre de Pays"))
        histographmasses
    })

    #Logique de la carte
    output$map_geo_masses <- renderLeaflet({
        mounth_set <- filter(data_set, Mois == input$Mois_map_masses)
        color_pal <- colorQuantile("Reds",mounth_set$Values,n=9)
        map_geo_masses <- leaflet() %>%
            addTiles() %>%
            setView(0, 0, zoom = 1) %>%
            addCircleMarkers(lng=mounth_set$Longitude,lat=mounth_set$Latitude,popup = as.character(mounth_set$Masse), label= mounth_set$Pays,
                             color=color_pal(mounth_set$Masse),fillOpacity=0.5,radius = sqrt(as.numeric(mounth_set$Masse))/5000) %>%
            addLegend(pal = color_pal, values=(as.numeric(mounth_set$Masse)),position = "bottomright")
        map_geo_masses
    })

    #Logique du pie chart.
    output$piegraphmasses <- renderPlotly({
        piegraphmasses <- plot_ly(mounth_set <- filter(data_set, Mois==input$Mois_pie_masses&Masse>=500000000),
                            labels = mounth_set$Pays,values = mounth_set$Masse,type="pie"
        )
        piegraphmasses
    })
    
    #Logique du graphique de point.
    output$scattergraphmasses <- renderPlotly({
        mounth_set <- filter(data_set, Mois == input$Mois_scatter_masses)
        scattergraphmasses <- plot_ly(
            x=mounth_set$Valeurs,y=mounth_set$Masse,text=mounth_set$Pays, size=mounth_set$Valeurs,color=mounth_set$Valeurs,type="scatter",mode="markers")
        scattergraphmasses <- scattergraphmasses %>% layout(
            xaxis = list(title="Valeurs(€)"),
            yaxis = list(title="Masses(Kg)"))
        scattergraphmasses
    })
})
