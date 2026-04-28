import pandas as pd

  Alunos = ("Carlos", "Daniela", "Igor", "Gabriel", "Fernanda"),
    Matemática = (5.1, 8.6, 5.6, 8.0, 10.0,)
    Português =(9.1, 6.9, 7.8, 5.8, 6.0,)
    História = (7.3, 9.8, 8.8, 8.5, 7.0,)
    Geografia =( 6.6, 8.6, 5.5, 8.6, 8.2,)
    Ciências = (6.5, 7.0, 6.8, 9.2, 7.5)


df = pd.read_csv('prova01.csv')
df
df.head(Alunos, Matemática, Português, História, Geografia, Ciências)
df.columns(6)
df.shape (4)