import pandas as pd

movie_info = pd.read_csv("./tmdb_5000_movies.csv")

print(movie_info.head(3))
print(movie_info.shape)
print(movie_info.loc[0])

columns = ["title", "spoken_languages"]
m_list = movie_info[columns]
print(m_list.loc[0:100])
print(pd.isnull(movie_info['title']))


