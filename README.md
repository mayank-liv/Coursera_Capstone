# Capstone Project - The Battle of Neighborhoods

# Neighborhood crime-records based venue suggestion


## 1. Introduction -

In today's day and age, travelling to a new place is no longer as tedious a process as it was a few decades back. Unlike before, when one had to rely on locals to guide them to places like nearby restaurants that they could visit, one can just spend 5 minutes on the Internet and find a list of tens of restaurants in a given locality. There are various sites and resources, like TripAdvisor and even FourSquare API, that can provide such a suggestions list in just a few seconds.

However, one of the flaws or rather, shortcomings about this is that although these services provide the list of venues along with its precise locations and reviews, it overlooks one key factor everyone needs to keep in mind while in a new city- how safe the neighborhood they are visiting, is.

For istance, one can be visiting a neighborhood in an entirely new city for the first time, and so might need some help inorder to decide which restaurant to visit for a meal. A regular internet search might provide the person with an idea of which restaurants are the best suited for the person, but it wouldn't give one any idea about how safe the neighborhood that he/she might be visiting, is. Hence, criminals and thiefs could take advantage of the fact that he/she is new to the nighborhood, and so one could get robbed, muggled, or something even worse can happen.

Hence, in a way, the restaurant with the best ratings isn't necessarily the one that should be suggested to a person. Instead, one should also be given an idea about how safe the neighborhood around that restaurant is, at the time of the day one's planning to visit it. My project aims to address this problem and find a solution around it.

### Idea for the project - 

I believe that when a newcomer to a city searches for top venues in a certain neighborhood, the regular information of the venues he gets, should be supplemented with the criminal record of places around that neighborhood.

Hence, I aim to provide this additional information to the user, with my Capstone project.

My project will be based on the neighborhoods and venues of New York City, along with the crime record of it.

When a person searches for top venues at a particular neighborhood, Foursquare API is scrapped to provide us with the data about the top venues at that neighbrhood.

We manipulate this data, adding additional information and dropping unnecessary information, to provide us with a more desired list of top venues.

Now, the major part of my project comes into play. I use the data I have about the crime record at places in New York City, and provide the user with information about the history of the predominant crimes committed within a certain distance of the top venues.

Finally, we will provide this information in the format of a map too, inorder to give the user a better understanding of the data, as well as a sense of direction and a better perspective.

### Target User Base -

As I've explained in excruciating detail earlier, this project aims to help travellers to new cities, specially the ones that are most vulnerable to crimes. This list of people that are more vulnerable to such crimes include: 

* Solo travellers
* Small groups of elderly tourists
* Small groups of female tourists
* People who don't speak the local tongue
* Young travellers
* New residents of a city


## 2. Data Description -

For this project, we'll be using two major open datasets.

### New York City Crime Record for 2016-17 :

This dataset is available at the link: [New York City 2016-17 crime records](https://data.cityofnewyork.us/Public-Safety/NYC-crime/qb7u-rbmr) and includes all valid felony, misdemeanor, and violation crimes reported to the New York City Police Department (NYPD) for all complete quarters of 2017. This dataset is mostly used for visualisation with Folium Maps, as it has lesser number of data points.

The description of the columns of this dataset we'll primarily be using, is given in a table below. The other columns are not needed, so we clean the file and its data accordingly

|Field Name|Description|
|-----|-----|
|CMPLNT_NUM|Randomly generated persistent ID for each complaint |
|CMPLNT_FR_TM|Exact time of occurrence for the reported event|
|PD_DESC|Classification of crime into categories|
|Latitude|Latitude coordinate where crime occured|
|Longitude|Longitude coordinate where crime occured|

We further use various data cleaning techniques to split columns like CMPLNT_FR_TM into its components, like hours etc, to further help with our data modelling and visualisation.


### New York City Crime Historic Crime Record since 2006 - 

This dataset is available in the link: [New York Historic Crime Record Since 2006](https://data.cityofnewyork.us/Public-Safety/NYPD-Arrests-Data-Historic-/8h9b-rp9u/data) and contains a list of every arrest in NYC going back to 2006 through the end of the previous calendar year.

The description of the columns of this dataset we'll primarily be using, is given in a table below. The other columns are not needed, so we clean the file and its data accordingly

|Field Name|Description|
|-----|-----|
|ARREST_KEY|Randomly generated persistent ID for each arrest|
|ARREST_DATE|Exact date of arrest for the reported event|
|PD_DESC|Classification of crime into its category|
|OFNS_DESC|Classification of offense into its category|
|ARREST_BORO|Borough of arrest.|
|Latitude|Latitude coordinate where crime occured|
|Longitude|Longitude coordinate where crime occured|

We further use various data cleaning techniques to split columns like CMPLNT_FR_TM into its components, like Month, Day of week etc.to further help with our data modelling and visualisation.


For the rest of the data we will need, we use Foursquare API. The other datasets we extract using Foursquare are:

### Top 30 venues in New York City - 

We first use Foursquare API to explore New York City for its top 30 venues, which leads us to the following link: [Top 30 venues](https://foursquare.com/explore?mode=url&ne=40.822383%2C-73.841&q=Top%20Picks&sw=40.666056%2C-74.129047).

Next, we use BeautifulSoup to scrap off data from this link. The data we scrap is stored in the following columns, in a dataframe.

|Field Name|Description|
|-----|-----|
|id|The unique ID of the venue|
|score|The rating out of 10, assigned to the venue by users|
|category|Category of the venue (Park, restaurant etc)|
|name|Name of venue|
|address|Address of venue|
|postalcode|Postal Code of venue|
|city|City of venue|
|href|Code to further find info about venue on Foursquare|
|latitude|Latitude of venue's location|
|longitude|Longitude of venue's location|

### Top restaurants within a certain distance of these Top Venues - 

We further use Foursquare API and find out data about the top restaurants that are around our top venues in NYC, and then scrap it and store it in a dataframe using BeautifulSoup. The columns in the dataframe are:

|Field Name|Description|
|-----|-----|
|id|The unique ID of the restaurant|
|score|The rating out of 10, assigned to the restaurant by users|
|category|Category of restaurant|
|categoryID|Unique code identifying the category|
|postalcode|Postal Code of the restaurant|
|name|Name of restaurant|
|address|Address of restaurant|
|city|City of restaurant|
|latitude|Latitude of location of restaurant|
|longitude|Longitude of location of restaurant|
|venue_name|Name of venue restaurant is nearest to|
|venue_latitude|Latitude of location of venue closest to restaurant|
|venue_longitude|Longitude of location of venue closest to restaurant|




## 3. Exploratory Data Analysis and Visualisation-

### First, we take a look at what the top 10 crimes that people have been arrested for in NYC over the last 10 years, are -

![Top 10 crimes](https://github.com/mayank-liv/Coursera_Capstone/blob/master/Capstone/Screenshot%20(71).png)

This gives us the user an idea about what crimes to expect while at NYC, and to prepare for it accordingly.


### A look at which months are the safest to visit NYC in -

We group the crime data of NYC since 2006, according to the months the crime occured in, and then have a look at a bar-diagram to have a better understanding of the data.

![Month-wise comparison of crimes](https://github.com/mayank-liv/Coursera_Capstone/blob/master/Capstone/Fig1%20(1).png)

Clearly, we can see that months 11 and 12 (i.e. November and December respectively) are the ones with the lowest number of total crimes since 2006. Hence, we can conclude that that's the safest time of the month for a person to visit NYC. The low number of crimes might be because of the bitterly cold NYC winters, which make people prefer staying indoors. Still, based on this visualisation, we can recommend December as the safest month to visit NYC.


### A look at which days are the safest to visit NYC in - 

We group the crime data of NYC since 2006, according to the months the crime occured in, and then have a look at a bar-diagram to have a better understanding of the data.

![Day-wise comparison of crimes](https://github.com/mayank-liv/Coursera_Capstone/blob/master/Capstone/Fig2%20(1).png)

Clearly, we can see that days 1 and 7 (i.e. Monday and Sunday, respectively) have witnessed the least number of crimes since 2006. Hence, the user is recommended to visit NYC during these days. Days 3 and 4 (i.e Wednesday and Thursday respectively) witness the most number of crimes, probably because these are peak weekdays. 


### A look at which hours are the safest to go out in NYC, in -

For this, we group the crime data of NYC in 2016-17, as the hour parameter is not present in the crime dataset of NYC since 2006. Since we are plotting the number of crimes for just 1 year, the number of crimes that are shown is drastically low.

![Hour-wise comparison of crimes](https://github.com/mayank-liv/Coursera_Capstone/blob/master/Capstone/Fig3.png)

We can see peak-criminal activity at 0 hours, after which the numbers of crimes drastically falls down. Hence its highly recommended for a person to stay indoor and cautious at this time. The early morning hours seem to be the safest, so if someone wants to explore the neighbourhood, that would be the time to do it. 

### A look at the month-wise comparison of the top 3 crimes - 

![Month-wise top 3 crimes](https://github.com/mayank-liv/Coursera_Capstone/blob/master/Capstone/Fig4%20(1).png)

From this visualisation, we can clearly see a gradual dip in the number of crimes from month 10 (October) for around 3 months, so that marks the beginning of the safest months.

### A look at the day-wise comparison of the top 3 crimes -

![Day-wise top 3 crimes](https://github.com/mayank-liv/Coursera_Capstone/blob/master/Capstone/Fig5.png)

From this visualisation, we can clearly see the dip in the number of crimes towards day 5 (Friday) that last till day 1 (Monday). Hence, this is the best time of the week to visit NYC.



### Data Scrapping from Foursquare for top 30 Venues-

For getting the top 30 venues in NYC, the following bit of code was used. Data scrapping required me to inspect the site already mentioned before, to find the required address of various elements that together form a part of our dataset.


'''

top=requests.get("https://foursquare.com/explore?mode=url&ne=40.822383%2C-73.841&q=Top%20Picks&sw=40.666056%2C-74.129047")

soup = BeautifulSoup(top.content, 'html.parser')

top_venues = soup.find_all('div', class_='venueDetails')

'''


version='20180604'

