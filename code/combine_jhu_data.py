## Read the CSSE Daily Data
## Dependencies: the JHU COVID-19 repo in the /data/ folder
## Products: daily.df dataframe of concatenated data

import pandas as pd
import os
import pickle

covid_daily_datadir = "../data/COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/"

def proc_file(cff):
    """
    Process the csv file at global covid_daily_datadir
    :param cff: filename
    :return: dataframe with date and key index
    """
    cdf = pd.read_csv(covid_daily_datadir + cff)
    cdf['Date'] = pd.Period(cff[:-4],'d')
    # cdf = cdf.set_index(['Date','Combined_Key'])
    return cdf

if __name__=="__main__":
    covid_files = os.listdir(covid_daily_datadir)
    covid_files = [cf for cf in covid_files if "csv" in cf]
    daily_df = pd.concat((proc_file(cff) for cff in covid_files))
    with open('../data/daily.df', 'wb') as daily_dat:
        pickle.dump(daily_df, daily_dat)
