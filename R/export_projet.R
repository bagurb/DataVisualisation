# install.packages('shiny')
# install.packages("shinydashboard")
# install.packages("plotly")
# install.packages("ggplot2")
# install.packages("dplyr")
# install.packages("leaflet")
# install.packages("reticulate")

library(shiny)
library(shinydashboard)
library(tidyverse)
library(plotly)
library(ggplot2)
library(dplyr)
library(leaflet)
library(reticulate)


if(!(file.exists("new_data.csv"))){
  py_run_file("sort_script.py")
}

data_set <- read.csv("new_data.csv",sep=";",encoding="UTF-8")



runApp(getwd())
