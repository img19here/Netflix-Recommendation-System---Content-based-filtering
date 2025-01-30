import pandas as pd
import pickle
import streamlit as st


movies = pickle.load(open('movie_dict.pkl' , mode = 'rb'))
df = pd.DataFrame(movies)
#print(movies)
print()
similarity = pickle.load(open('similarity.pkl' , mode = 'rb'))
#print(similarity)

# Recommendation
def movie_pred(movie):

    recommended_movies = []
    movie_index = df[df['title'] == movie ].index[0]
    distance = similarity[movie_index]
    movie_lst = sorted( list(enumerate(distance)) , reverse = True, key = lambda x : x[1])[1:6]
    l = []
    for i in movie_lst:
        # print(i[0])
        recommended_movies.append((df.iloc[i[0]].title))
    return recommended_movies

# Streamlit web-app

import streamlit as st
left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image("https://static.vecteezy.com/system/resources/previews/017/396/814/original/netflix-mobile-application-logo-free-png.png" , width=180)

movie = st.selectbox(label='Choose your movie: ' ,options=list(df['title'].values) )
btn = st.button(label='Recommend')

if btn:
    movie_lst = movie_pred(movie)
    for i in movie_lst:
        st.write(i)
