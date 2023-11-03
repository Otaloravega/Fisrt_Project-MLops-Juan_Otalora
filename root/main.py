
import pandas as pd
from fastapi import FastAPI

app = FastAPI()


#Loanding flat files to be used by the functions
Genre_MaxPlayTime = pd.read_csv("datos/_1_Genre_MaxPlayTime.csv")
User_MaxPlayTime = pd.read_csv("datos/_2_User_MaxPlayTime.csv")
recommended_year_games = pd.read_csv("datos/_3_recommended_year_games.csv")
not_recommended_games_year = pd.read_csv("datos/_4_not_recommended_games_year.csv")
sentiment_analisis = pd.read_csv('datos/_5_sentiment_analysis_df.csv')
database_recomendations = pd.read_csv('datos/_6_database_recomendations.csv')


@app.get('/TimeGenrePlay/{genre}')
def TimeGenrePlay(genre: str):
    '''Return the the release year with more played hours for the entered genre'''
    # Get the corresponding year based on the gender
    year = Genre_MaxPlayTime.loc[Genre_MaxPlayTime['genres'].str.lower() == genre.lower(), 'release_year'].values
    if len(year) == 0:
        return {f'Videogame release year for the genre {genre}': 'no encontrado'}
    else:
        return {f'Videogame release year for the genre {genre}': str(year[0])}

@app.get('/UserbyGenre/{genre}')
def UserbyGenre(genre: str):
    '''Return the user who accumulates the most hours played for the given genre and a list of the accumulation of hours played per year.'''
    # Get the corresponding user based on the gender
    user = User_MaxPlayTime.loc[User_MaxPlayTime['genres'].str.lower() == genre.lower(), 'user_id'].values
    if len(user) == 0:
        return {f'User with more hours played for Gen  {genre}': 'no encontrado'}
    else:
        return {f'User with more hours played for Gen  {genre}': str(user[0])}

@app.get('/RecommendUsers/{year}')
def RecommendUsers( year : int ): 
    '''Returns the top 3 recommended games by users for the given year (reviews.recommend = True and positive/neutral reviews).'''
    #Filtering by year
    filtered_df = recommended_year_games[recommended_year_games['posted_year'] == year]
    #Sorting by  'times_recommended' in a descending order
    sorted_df = filtered_df.sort_values(by='times_recommended', ascending=False)
    #Selecting the 3 first records
    top_3_games = sorted_df.head(3)    
    lista_de_diccionarios = top_3_games[['title']].to_dict(orient='records')
    return lista_de_diccionarios

@app.get('/NotRecommendUsers/{year}')
def NotRecommendUsers( year : int ): 
    '''Returns the top 3 recommended games by users for the given year (reviews.recommend = True and positive/neutral reviews).'''
    #Filtering by year
    filtered_df = not_recommended_games_year[not_recommended_games_year['posted_year'] == year]
    #Sorting by  'times_recommended' in a descending order
    sorted_df = filtered_df.sort_values(by='times_not_recommended', ascending=False)
    #Selecting the 3 first records
    top_3_games = sorted_df.head(3)    
    lista_de_diccionarios = top_3_games[['title']].to_dict(orient='records')
    if len(lista_de_diccionarios) == 0:
        return []
    else:
        return lista_de_diccionarios
    
@app.get('/analysis_of_sentiment/{year}')
def analysis_of_sentiment(year: int):
    '''Enter year to consult, to return the Number of reviews categorized by sentiment'''
    Cantidad = sentiment_analisis[sentiment_analisis['year']==year]['sentiment'].to_list()[0]
    return Cantidad

@app.get('/recomendation_of_user/{id}')
def recomendation_of_user(id: str):
    '''Enter user ID to return recommended games'''
    Recomendations = database_recomendations[database_recomendations['user_id']==id]['recomendations'].to_list()[0]
    return Recomendations