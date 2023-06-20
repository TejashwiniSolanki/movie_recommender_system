import streamlit as st
import pickle
import pandas as pd
import requests


# def fetch_poster(movie_id):
#     movie_path = 'https://api.themoviedb.org/3/movie/{}?api_key=a6df0b03161c642e7c45c409c67654f8'.format(movie_id)
#     response = requests.get(movie_path)
#     data = response.json()
#     st.text(movie_path)
#     st.text(data)
#     return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']


def recommend_movie(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_name = []
    # recommended_movie_poster = []

    for i in movies_list[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movie_name.append(movies.iloc[i[0]].title)
        # recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movie_name


all_movies = pickle.load(open('movies_dump.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies = pd.DataFrame(all_movies)

st.title(' Lets Recommend Movies')


selected_movie = st.selectbox('What movie you wanna watch today?', movies['title'].values)

if st.button('Recommend'):
    our_recommendations = recommend_movie(selected_movie)
    for i in our_recommendations:
        st.write(i)

    # names, posters = recommend_movie(selected_movie)
    # col1, col2, col3, col4, col5 = st.columns(5)
    # with col1:
    #     st.text(names[0])
    #     st.image(posters[0])
    # with col2:
    #     st.text(names[1])
    #     st.image(posters[1])
    # with col3:
    #     st.text(names[2])
    #     st.image(posters[2])
    # with col4:
    #     st.text(names[3])
    #     st.image(posters[3])
    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])
