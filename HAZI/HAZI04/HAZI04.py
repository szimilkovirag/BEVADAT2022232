import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
'''
FONTOS: Az első feladatáltal visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''
'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''
def csv_to_df(test_data_file_name) -> pd.core.frame.DataFrame:
    data = pd.read_csv(test_data_file_name)
    return pd.DataFrame(data)

csv_to_df('C:/bevadat/BEVADAT2022232/HAZI/HAZI04/StudentsPerformance.csv')
'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''
def capitalize_columns(df_data) -> pd.core.frame.DataFrame:
    df = df_data.copy()

    return df.rename(columns=lambda x: x.upper() if 'e' not in x.lower() else x)
'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''
def math_passed_count(df_data) -> int:
    df = df_data.copy()
    count = np.sum(df['math score'] >= 50)
    return count
'''
Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''
def did_pre_course(df_data) -> pd.core.frame.DataFrame:
    df = df_data.copy()
    df_did_pre_course = df[df['test preparation course'] == 'completed']
    return df_did_pre_course
'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''
def average_scores(df_data) -> pd.core.frame.DataFrame:
    df = df_data.copy()
    df_average_scores = df.groupby('parental level of education')['math score', 'reading score', 'writing score'].mean()
    return df_average_scores
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''
def add_age(df_data) -> pd.core.frame.DataFrame:
    df = df_data.copy()
    np.random.seed(42)
    df['age'] = np.random.randint(18, 67, df.shape[0])
    return df
'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''
def female_top_score(df_data) -> tuple:
    df = df_data.copy()
    females = df[df['gender'] == 'female']
    sorted = females.sort_values(by=['math score', 'reading score', 'writing score'], ascending=False)
    top_score = sorted[['math score', 'reading score', 'writing score']].iloc[0].tolist()
    return (top_score[0], top_score[1], top_score[2])
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''
def add_grade(df_data) -> pd.core.frame.DataFrame:
    df = df_data.copy()
    df['grade'] = ((df['math score']+df['reading score']+df['writing score'])/300*100)

    for i in range(len(df)):
        if df['grade'][i] >= 0 and df['grade'][i] < 60:
            df['grade'][i] = 'F'
        elif df['grade'][i] >= 60 and df['grade'][i] < 70:
            df['grade'][i] = 'D'
        elif df['grade'][i] >= 70 and df['grade'][i] < 80:
            df['grade'][i] = 'C'
        elif df['grade'][i] >= 80 and df['grade'][i] < 90:
            df['grade'][i] = 'B'
        elif df['grade'][i] >= 90 and df['grade'][i] < 100:
            df['grade'][i] = 'A'

    return df
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''
def math_bar_plot(df_data) -> plt.figure:
    df = df_data.copy()
    df_average_scores = df.groupby('gender')['math score'].mean()

    fig, ax = plt.subplots()

    ax.bar(['female', 'male'], df_average_scores)
    ax.set_xlabel('Gender')
    ax.set_ylabel('Math Score')
    ax.set_title('Average Math Score by Gender')

    return fig
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''
def writing_hist(df_data) -> plt.figure:
    result_df = df_data.copy()
    
    fig, ax = plt.subplots()
    ax.hist(result_df['writing score'])
    ax.set_title('Distribution of Writing Scores')
    ax.set_xlabel('Writing Score')
    ax.set_ylabel('Number of Students')

    return fig
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''
def ethnicity_pie_chart(df_data) -> plt.figure:
    new_df = df_data.copy()
    fig, ax = plt.subplots()

    grouped = new_df.groupby('race/ethnicity')['gender'].count()

    ax.pie(grouped, labels=['group A', 'group B', 'group C', 'group D', 'group E'], autopct='%1.1f%%')
    ax.set_title('Proportion of Students by Race/Ethnicity')

    return fig