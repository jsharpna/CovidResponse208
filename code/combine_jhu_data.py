import pandas as pd
import os

covid_daily_datadir = "../data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/"

covid_files = os.listdir(covid_datadir)
covid_files = [cf for cf in covid_files if ""]

pd.read_csv()