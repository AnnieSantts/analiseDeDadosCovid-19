#Países com maior índice de rigidez nas restrições tem uma taxa de mortalidade menor?

import numpy as np
import pandas as pd


vaccinations_data = pd.read_csv("COVID_VACCINATIONS.csv")
deaths_data = pd.read_csv("COVID_DEATHS.csv")


stringency_data = vaccinations_data[["iso_code", "location", "stringency_index"]]
mortality_data = deaths_data[["iso_code", "location", "total_deaths", "population"]]

combined_data = pd.merge(stringency_data, mortality_data, on=["iso_code", "location"])


combined_data["death_rate"] = (combined_data["total_deaths"] / combined_data["population"]) * 100

# Calcular a correlação entre índice de rigidez e taxa de mortalidade
correlation = combined_data["stringency_index"].corr(combined_data["death_rate"])


print(f"Correlação entre índice de rigidez e taxa de mortalidade: {correlation}")
