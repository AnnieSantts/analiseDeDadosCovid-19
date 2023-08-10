#Os 10 paises com maior população tiveram maiores números, em proporção, de mortes por Covid-19?

import numpy as np
import pandas as pd

vaccinations_data = pd.read_csv("COVID_VACCINATIONS.csv")
deaths_data = pd.read_csv("COVID_DEATHS.csv")



vaccinations_filtered = vaccinations_data[["iso_code", "location", "total_vaccinations"]]
deaths_filtered = deaths_data[["iso_code", "location", "total_deaths", "population"]]


combined_data = pd.merge(vaccinations_filtered, deaths_filtered, on=["iso_code", "location"])


combined_data["death_rate"] = (combined_data["total_deaths"] / combined_data["population"]) * 100


combined_data_sorted = combined_data.sort_values(by="population", ascending=False)


top_10_countries = combined_data_sorted.head(10)

print(top_10_countries[["location", "population", "total_deaths", "death_rate"]])
