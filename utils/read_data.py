import pandas as pd

def read_data():
    weather_df = pd.read_csv('../data/wetter_Kiel_2015_2019.csv', sep=';', decimal=',', parse_dates=['Date'], dayfirst=True)

    # Weather Cloud Cover: https://en.wikipedia.org/wiki/Okta
    # Weather Code:  https://wetterkanal.kachelmannwetter.com/was-ist-der-ww-code-in-der-meteorologie/
    weather_df = weather_df.astype({'nnav': 'category', 'wwav': 'category'})
    # sort by date
    weather_df.sort_values(by=['Date'], inplace=True)
    
    
    sales_df = pd.read_csv('../data/hackathon_meteolytix_Artikelgruppen_Umsatz_verschiedeneStandorte.csv', parse_dates=['Datum'])
    sales_df = sales_df.rename(columns={'Datum': 'Date', 'Umsatz': 'Sales', 'Artikelgruppe': 'Product Group'})
    sales_df = sales_df.astype({'Filiale': 'category', 'Product Group': 'category'})
    # sort by date
    sales_df.sort_values(by=['Date'], inplace=True)
    
    
    product_group_df = pd.read_csv('../data/meteolytix_Artikelgruppen.csv', sep=';')
    # change to dictionary
    product_group_dict = product_group_df.set_index('Artikelgruppe').to_dict()['Name']
    
    return weather_df, sales_df, product_group_dict