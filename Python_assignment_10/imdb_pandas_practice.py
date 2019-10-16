'''
Pandas Homework with IMDb data
'''

import pandas as pd
import matplotlib.pyplot as plt

'''
BASIC LEVEL
'''

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
movies = pd.read_csv('imdb_1000.csv')

#Q1: print the number of rows and columns
print(movies.shape)

#Q2: check the data type of each column
movies.dtypes

#Q3: calculate the average movie duration
movies.duration.mean()

#Q4: sort the DataFrame by duration to find the shortest and longest movies and print shortest and longest movie records
print(movies.sort('duration').head(1))
print(movies.sort('duration').tail(1))

#Q5: create a histogram of duration, choosing an "appropriate" number of bins
movies.duration.plot(kind='hist', bins=20)
plt.show()

#Q6: use a box plot to display that same data
movies.duration.plot(kind='box')
plt.show()

'''
INTERMEDIATE LEVEL
'''

#Q7: count how many movies have each of the content ratings and print them
movies.content_rating.value_counts()

#Q8: use a visualization to display that same data, including a title and x and y labels
movies.content_rating.value_counts().plot(kind='bar', title='Top 1000 Movies by Content Rating')
plt.xlabel('Content Rating')
plt.ylabel('Number of Movies')
plt.show()

#Q9 convert/replace the following content ratings NOT RATED, APPROVED, PASSED, GP to "UNRATED"
movies.content_rating.replace(['NOT RATED', 'APPROVED', 'PASSED', 'GP'], 'UNRATED', inplace=True)

#Q10 convert the following content ratings X, TV-MA to "NC-17"
movies.content_rating.replace(['X', 'TV-MA'], 'NC-17', inplace=True)

#Q11: Repeat Q7 and print the count with new rating names

#Q12 count the number of missing values in each column
movies.isnull().sum()

#Q13: if there are missing values: examine them, then fill them in with "UNDER REVIEW" values
movies[movies.content_rating.isnull()]
movies.content_rating.fillna('UNDER REVIEW', inplace=True)

#Q14: calculate the average (mean) star rating for movies 2 hours or longer,

#Q15: compare that with the average star rating for movies shorter than 2 hours
movies[movies.duration >= 120].star_rating.mean()
movies[movies.duration < 120].star_rating.mean()

#Q16: use a visualization to detect whether there is a relationship between duration and star rating
movies.plot(kind='scatter', x='duration', y='star_rating', alpha=0.2)
plt.show()
#Q17: calculate the average duration for each genre (Hint: use groupby)
movies.groupby('genre').duration.mean()

'''
ADVANCED LEVEL
'''

#Q18: determine the top rated movie (by star rating) for each genre
movies.sort('star_rating', ascending=False).groupby('genre').title.first()
movies.groupby('genre').title.first()   # equivalent, since DataFrame is already sorted by star rating


'''
BONUS
'''

# Figure out something "interesting" using the actors data!
