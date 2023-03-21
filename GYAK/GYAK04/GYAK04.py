import pandas as pd
import matplotlib.pyplot as plt
'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''
'''
Készíts egy függvényt ami a bemeneti dictionary-ből egy DataFrame-et ad vissza.

Egy példa a bemenetre: test_dict
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: dict_to_dataframe
'''
stats = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

def dict_to_dataframe(test_dict) -> pd.core.frame.DataFrame:
    test_df = pd.DataFrame(test_dict)
    return test_df
'''
Készíts egy függvényt ami a bemeneti DataFrame-ből vissza adja csak azt az oszlopot amelynek a neve a bemeneti string-el megegyező.

Egy példa a bemenetre: test_df, 'area'
Egy példa a kimenetre: test_df
return type: pandas.core.series.Series
függvény neve: get_column
'''
def get_column(test_df, column_name) -> pd.core.series.Series:
    new_df = test_df.copy()
    return new_df.loc[:,column_name]
'''
Készíts egy függvényt ami a bemeneti DataFrame-ből vissza adja a két legnagyobb területű országhoz tartozó sorokat.

Egy példa a bemenetre: test_df
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: get_top_two
'''
def get_top_two(test_df) -> pd.core.frame.DataFrame:
    new_df = test_df.copy()
    df = new_df.sort_values(by=['area'], ascending=False)
    return df.iloc[:2]
'''
Készíts egy függvényt ami a bemeneti DataFrame-ből kiszámolja az országok népsűrűségét és eltárolja az eredményt egy új oszlopba ('density').
(density = population / area)

Egy példa a bemenetre: test_df
Egy példa a kimenetre: test_df
return type: pandas.core.frame.DataFrame
függvény neve: population_density
'''
def population_density(test_df) -> pd.core.frame.DataFrame:
    new_df = test_df.copy()
    new_df['density'] = new_df['population'] / new_df['area']
    return new_df
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlopdiagramot (bar plot),
ami vizualizálja az országok népességét.

Az oszlopdiagram címe legyen: 'Population of Countries'
Az x tengely címe legyen: 'Country'
Az y tengely címe legyen: 'Population (millions)'

Egy példa a bemenetre: test_df
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: plot_population
'''
def plot_population(test_df) -> plt.figure:
    x = test_df['country']
    y = test_df['population']

    fig = plt.figure()
    plt.bar(x, y)
    plt.xlabel('Country')
    plt.ylabel('Population (millions)')
    plt.title('Population of Countries')
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja az országok területét. Minden körcikknek legyen egy címe, ami az ország neve.

Az kördiagram címe legyen: 'Area of Countries'

Egy példa a bemenetre: test_df
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: plot_area
'''
def plot_area(test_df) -> plt.figure:
    x = test_df['area'].to_numpy()
    labels = test_df['country'].tolist()

    fig, ax = plt.subplots()
    ax.pie(x=x, labels=labels)
    ax.set_title('Area of Countries')