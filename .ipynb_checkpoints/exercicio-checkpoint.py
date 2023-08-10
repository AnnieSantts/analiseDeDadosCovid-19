import numpy as np
import pandas as pd


# Carregar os dados dos arquivos CSV
vaccinations_data = pd.read_csv("COVID_VACCINATIONS.csv")
deaths_data = pd.read_csv("COVID_DEATHS.csv")


# Filtrar os dados para as colunas relevantes
vaccinations_filtered = vaccinations_data[["iso_code", "location", "total_vaccinations"]]
deaths_filtered = deaths_data[["iso_code", "location", "total_deaths", "population"]]

# Combinar os dados de vacinação e mortes com base no ISO code
combined_data = pd.merge(vaccinations_filtered, deaths_filtered, on=["iso_code", "location"])

# Calcular a proporção de mortes por COVID-19 em relação à população
combined_data["death_rate"] = (combined_data["total_deaths"] / combined_data["population"]) * 100

# Ordenar os dados pelo tamanho da população em ordem decrescente
combined_data_sorted = combined_data.sort_values(by="population", ascending=False)

# Selecionar os 10 países com maior população
top_10_countries = combined_data_sorted.head(10)

# Exibir os resultados
print(top_10_countries[["location", "population", "total_deaths", "death_rate"]])
