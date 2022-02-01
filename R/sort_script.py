
import pandas as pd
import csv

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
                print(returned_data[var["Pays"]])
        else:
                returned_data[var["Pays"]] = dict([(var['Mois'],[var['Valeur'],var['Masse'],str(var["coordonnees_pays"]).split(",")[0],str(var["coordonnees_pays"]).split(",")[1]])])
                print(returned_data[var["Pays"]])

    new_data_set = pd.DataFrame(columns=["Pays","Mois","Valeurs","Masse","Longitude","Latitude"])
    for country in returned_data.keys():
        for mounth in returned_data[country].keys():
            new_data_set = new_data_set.append({"Pays":country,"Mois":mounth,"Valeurs":returned_data[country][mounth][0],
            "Masse":returned_data[country][mounth][1],"Longitude":returned_data[country][mounth][3],"Latitude":returned_data[country][mounth][2]},ignore_index=True)
            new_data_set = new_data_set.sort_values(by=["Pays","Mois"])
            new_data_set = new_data_set.dropna()
    return  new_data_set

csv_file = 'data.csv'
data_set = pd.read_csv(csv_file,delimiter=";")
index_2019 = data_set[data_set['Année'] == '2019'].index
data_set.drop(index_2019,inplace=True)
data_set = data_set.dropna()
new_data_set = create_new_set()
new_data_set.to_csv("new_data.csv",sep=";")
