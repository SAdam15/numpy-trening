import pandas as pd

# Wczytaj plik CSV - podaj właściwą ścieżkę do swojego pliku
df = pd.read_csv(r'C:\kodilla\albumy.csv')

# Zamień nagłówki na polskie odpowiedniki
df.columns = ['Tytuł', 'Artysta', 'Rok', 'Max Poz']

# Ilu unikalnych artystów?
unikalni_artysci = df['Artysta'].nunique()
print(f"Liczba unikalnych artystów: {unikalni_artysci}")

# Najczęściej pojawiające się zespoły/artysci
czestosc_artystow = df['Artysta'].value_counts()
print("Najczęściej pojawiający się artyści/zespoły:")
print(czestosc_artystow)

# Usuń kolumnę 'Max Poz'
df = df.drop(columns=['Max Poz'])

# Zmień nagłówki: pierwsza litera wielka, reszta mała
df.columns = [col.capitalize() for col in df.columns]

# Rok z największą liczbą wydanych albumów
rok_max_albumow = df['Rok'].value_counts().idxmax()
print(f"Rok z największą liczbą wydanych albumów: {rok_max_albumow}")

# Liczba albumów wydanych między 1960 a 1990 włącznie
liczba_albumow_1960_1990 = df[(df['Rok'] >= 1960) & (df['Rok'] <= 1990)].shape[0]
print(f"Liczba albumów wydanych między 1960 a 1990 włącznie: {liczba_albumow_1960_1990}")

# Rok wydania najmłodszego albumu
rok_najmlodszy = df['Rok'].max()
print(f"Rok wydania najmłodszego albumu: {rok_najmlodszy}")

# Najwcześniej wydane albumy każdego artysty
najwczesniejsze_albumy = df.loc[df.groupby('Artysta')['Rok'].idxmin()]

# Zapisz do pliku CSV
najwczesniejsze_albumy.to_csv(r'C:\kodilla\najwczesniejsze_albumy.csv', index=False)

print("Lista najwcześniejszych albumów każdego artysty zapisana do 'najwczesniejsze_albumy.csv'")