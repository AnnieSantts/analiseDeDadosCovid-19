#Qual é a proporção de pessoas vacinadas que foram hospitalizadas devido à COVID-19 em comparação com pessoas não vacinadas?

import numpy as np
import pandas as pd

vaccinations_data = pd.read_csv("COVID_VACCINATIONS.csv")
deaths_data = pd.read_csv("COVID_DEATHS.csv")

# Filtrar os dados relevantes para cada análise
vaccinated_data = vaccinations_data[["iso_code", "location", "people_vaccinated", "people_fully_vaccinated"]]
hospitalization_data = deaths_data[["iso_code", "location", "hosp_patients", "hosp_patients_per_million"]]


combined_data = pd.merge(vaccinated_data, hospitalization_data, on=["iso_code", "location"])


combined_data["hospitalization_rate"] = (combined_data["hosp_patients"] / combined_data["people_vaccinated"]) * 100


combined_data["unvaccinated_hospitalization_rate"] = (combined_data["hosp_patients"] / (combined_data["hosp_patients_per_million"] * 1000000)) * 100


print(combined_data[["location", "hospitalization_rate", "unvaccinated_hospitalization_rate"]])
