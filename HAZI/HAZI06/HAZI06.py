import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from GYAK.GYAK06.classifier import DecisionTreeClassifier


data = pd.read_csv('C:/bevadat/BEVADAT2022232/HAZI/HAZI06/NJ.csv')

X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values.reshape(-1,1)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=.2, random_state=41)

classifier = DecisionTreeClassifier(100, 10)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)
print(accuracy_score(Y_test, Y_pred))

'''
A tanítást a min_samples_split és a max_depth paramétereknek 3-at adtam értékül,
majd a max_depth-et növeltem egyesével, amíg a 8-as értékre KeyError-t nem kaptam.
A max_depth növelésével az accuracy is nőtt.
Ezután a min_samples_split értékét növeltem először 10-re, és javulást tapasztalam.
Majd a min_samples_split értékének a növelésével folytattam, minnél nagyobb értéket
adtam át, annál jobb lett az accuracy is (mondhatni exponenciálisan kellettt növelnem
a paraméter értékét annak érdekében, hogy javulást tapasztaljak).
A 80% eléréséhez a max_depth paramétert is növelnem kellett.
Azt vettem észre, hogy minél nagyobb paraméterekkel futtattam le a tanulást, annnál
több időt vett igénybe a kiértékelés.

1. fitelés:
    paraméterek: 
        - min_samples_split=3
        - max_depth=3
    elért accuracy: 0.7839166666666667

2. fitelés:
    paraméterek:
        - min_samples_split=3
        - max_depth=4
    elért accuracy: 0.7849166666666667

3. fitelés:
    paraméterek:
        - min_samples_split=3
        - max_depth=7
    elért accuracy: 0.7934166666666667

4. fitelés:
    paraméterek:
        - min_samples_split=3
        - max_depth=8
    elért accuracy: KeyError

5. fitelés:
    paraméterek:
        - min_samples_split=10
        - max_depth=7
    elért accuracy: 0.7935

6. fitelés:
    paraméterek:
        - min_samples_split=11
        - max_depth=7
    elért accuracy: 0.7935

7. fitelés:
    paraméterek:
        - min_samples_split=20
        - max_depth=7
    elért accuracy: 0.7936666666666666

8. fitelés:
    paraméterek:
        - min_samples_split=50
        - max_depth=7
    elért accuracy: 0.7935833333333333

9. fitelés:
    paraméterek:
        - min_samples_split=100
        - max_depth=7
    elért accuracy: 0.7940833333333334

10. fitelés:
    paraméterek:
        - min_samples_split=100
        - max_depth=10
    elért accuracy: 0.80225
'''