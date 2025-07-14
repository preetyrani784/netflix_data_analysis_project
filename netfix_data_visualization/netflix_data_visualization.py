import pandas as pd
import matplotlib.pyplot as plt


#load the data
df = pd.read_csv('C:/Users/preet/OneDrive/Desktop/coding/python nptel/HandlingMissingData/Sorting&Aggregation.py/Numpy/indian_employee_dataset/netflix.csv')

#clean the data
df = df.dropna(subset=['type', 'release_year', 'rating', 'country', 'duration', 'listed_in'])

type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color=['skyblue', 'orange'])
plt.title("Number of Movies Vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig('C:/Users/preet/OneDrive/Desktop/coding/movies_vs_Tvshows.png', dpi=300)
# plt.show()

rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Percentage of Content Ratings")
plt.tight_layout()
plt.savefig('C:/Users/preet/OneDrive/Desktop/coding/content_rating.png', dpi=300)
# plt.show()

movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace('min', '').astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'], bins=30, color='purple', edgecolor='black')
plt.title("Distribution of Movie Duration")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig('C:/Users/preet/OneDrive/Desktop/coding/movie_duration_histogram.png', dpi=300)
# plt.show()

release_count = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_count.index, release_count.values, color='red')
plt.title("Release Year VS Number of Show")
plt.xlabel('Release Year')
plt.ylabel('Number of Show')
plt.tight_layout()
plt.savefig('C:/Users/preet/OneDrive/Desktop/coding/release_year_Scatter.png', dpi=300)
# plt.show()

country_count = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index, country_count.values, color='teal')
plt.title("Top 10 Countries by Number of Show")
plt.xlabel("Number of shows")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig('C:/Users/preet/OneDrive/Desktop/coding/Top10_countries.png', dpi=300)
# plt.show()

content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)

fig, ax = plt.subplots(1,2, figsize=(12,5))

# first subplot: movies
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
ax[0].set_title("Movies Released Per Year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of Movies")

# second subplot: TV shows
ax[0].plot(content_by_year.index, content_by_year['TV Show'], color='orange')
ax[0].set_title("TV Released Per Year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of TV Shows")

fig.suptitle("Comparison of Movies & TV Shows released over years")
plt.tight_layout()
plt.savefig('C:/Users/preet/OneDrive/Desktop/coding/Movies_TV_shows_comparison.png', dpi=300)
plt.show()
