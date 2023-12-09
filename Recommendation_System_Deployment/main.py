import streamlit as st
import pickle
import pandas as pd

# importing the preprocessed dataset
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# converting it in dataframe
movies = pd.DataFrame(movies_dict)
# importing the similiarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

# recommend method will return Top 5 recommended movies
def recommend(movie):
    # find the index of the movie entered by user
    movie_index = movies[movies['title']==movie].index[0]
    # finding the similarity vector of that movie
    distances = similarity[movie_index]
    # enumerate assign index with similarity value and return tuple
    movies_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        # adding title of top 5 movies
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# creating Web page

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'How would you like to be contacted ?',
    movies['title'].values)

if st.button('recommend'):
    recommendations = recommend(selected_movie_name)
    # This will return the top five recommended movies
    for i in recommendations:
        st.write(i)