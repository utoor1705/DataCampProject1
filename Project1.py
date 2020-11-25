############ Data Camp Project - Super Bowl



# Import packages
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Load the CSV data into DataFrames
super_bowls= pd.read_csv('super_bowls.csv')
tv= pd.read_csv('tv.csv')
halftime_musicians= pd.read_csv('halftime_musicians.csv')


# For Reference
(super_bowls.head())
(tv.head())
(halftime_musicians.head())


tv.info()

halftime_musicians.info()



#Highest and lowest combined scores
(super_bowls[super_bowls['combined_pts'] > 70])
(super_bowls[super_bowls['combined_pts'] < 25])



# Histogram of point differences
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel("Number of Super Bowls")
plt.show()

# Closest game(s) and biggest blowouts
(super_bowls[super_bowls["difference_pts"] == 1])
(super_bowls[super_bowls["difference_pts"] >= 35])



# Join game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')



# Scatter plot with a linear regression model fit
sns.regplot(x = games_tv.difference_pts, y= games_tv.share_household, data=games_tv)


# Create a figure with 3x1 subplot and activate the top subplot
plt.subplot(3, 1, 1)
plt.plot(tv.super_bowl, tv.avg_us_viewers, color='#648FFF')
plt.title('Average Number of US Viewers')

# Activate the middle subplot
plt.subplot(3, 1, 2)
plt.plot(tv.super_bowl, tv.rating_household, color = "#DC267F")
plt.title('Household Rating')

# Activate the bottom subplot
plt.subplot(3, 1, 3)
plt.plot(tv.super_bowl, tv.ad_cost, color = "#FFB000")
plt.title('Ad Cost')
plt.xlabel('SUPER BOWL')

# Improve the spacing between subplots
plt.tight_layout()








# Halftime musicians for Super Bowls up to and including Super Bowl XXVII


(halftime_musicians[halftime_musicians.super_bowl <= 27])


# ## 8. Who has the most halftime show appearances?

halftime_appearances = halftime_musicians.groupby('musician').count()
halftime_appearances[halftime_appearances.super_bowl > 1]



# Filter out most marching bands
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

# Plot a histogram of number of songs per performance
most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins = most_songs)
plt.xlabel("Number of Songs Per Halftime Show Performance")
plt.ylabel('Number of Musicians')
plt.show()

# Sort the non-band musicians by number of songs per appearance...
no_bands = no_bands.sort_values('num_songs', ascending=False)
(no_bands.head(15))



# 2018-2019 conference champions
patriots = 'New England Patriots'
rams = 'Los Angeles Rams'

# Who will win Super Bowl LIII?
super_bowl_LIII_winner = ...
print('The winner of Super Bowl LIII will be the', super_bowl_LIII_winner)

