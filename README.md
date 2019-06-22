# Capstone Project - The Battle of Neighborhoods

# Neighborhood crime-records based venue suggestion


## 1. Introduction -

In today's day and age, travelling to a new place is no longer as tedious a process as it was a few decades back. Unlike before, when one had to rely on locals to guide them to places like nearby restaurants that they could visit, one can just spend 5 minutes on the Internet and find a list of tens of restaurants in a given locality. There are various sites and resources, like TripAdvisor and even FourSquare API, that can provide such a suggestions list in just a few seconds.

However, one of the flaws or rather, shortcomings about this is that although these services provide the list of venues along with its precise locations and reviews, it overlooks one key factor everyone needs to keep in mind while in a new city- how safe the neighborhood they are visiting, is.

For instance, one can be visiting a neighborhood in an entirely new city for the first time, and so might need some help inorder to decide which restaurant to visit for a meal. A regular internet search might provide the person with an idea of which restaurants are the best suited for the person, but it wouldn't give one any idea about how safe the neighborhood that he/she might be visiting, is. Hence, criminals and thiefs could take advantage of the fact that he/she is new to the nighborhood, and so one could get robbed, muggled, or something even worse can happen.

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
  
        #these are the columns that we'll use to store data about the top venues
        venue_columns = ['id', 
                 'score', 
                 'category', 
                 'name', 
                 'address',
                 'postalcode',
                 'city',
                 'href', 
                 'latitude', 
                 'longitude']


    df_top_venues = pd.DataFrame(columns=venue_columns)



   
    for venuex in top_venues:
    
    # Extract the available attributes
    venue_name = venuex.find(target="_blank").get_text()
    venue_score = venuex.find(class_="venueScore positive").get_text()
    venue_cat = venuex.find(class_="categoryName").get_text()
    venue_href = venuex.find(class_="venueName").h2.a['href']
    venue_id = venue_href.split('/')[-1]
        
    # Contruct the FourSquare venue API URL
    url = 'https://api.foursquare.com/v2/venues/{}?client_id={}&client_secret={}&v={}'.format(venue_id,
                                                                                              client_id,
                                                                                              client_secret,
                                                                                              version)
    
    # Request the venue data
    result = requests.get(url).json()
        
    # Get the properly formatted address and the latitude and longitude
    try:
      venue_address = result['response']['venue']['location']['address']
      venue_postalcode = result['response']['venue']['location']['postalCode']
      venue_city = result['response']['venue']['location']['city']
      venue_latitude = result['response']['venue']['location']['lat']
      venue_longitude = result['response']['venue']['location']['lng']
    
    except:
      continue
      
      
    # Add the venue to the top venues dataframe
    df_top_venues = df_top_venues.append({'id': venue_id,
                                          'score': venue_score,
                                          'category': venue_cat,
                                          'name': venue_name,
                                          'address': venue_address,
                                          'postalcode': venue_postalcode,
                                          'city': venue_city,
                                          'href': venue_href,
                                          'latitude': venue_latitude,
                                          'longitude': venue_longitude},ignore_index=True)

'''


### Data scrapping from Foursquare for top restaurants around our top venues -

For getting the top restaurants around the top venues in NYC, the following bit of code was used. Data scrapping required me to inspect the site already mentioned before, to find the required address of various elements that together form a part of our dataset. 

'''

    # The column names for the restaurants dataframe
    restaurants_columns = ['id',
                       'score', 
                       'category', 
                       'categoryID', 
                       'name', 
                       'address',
                       'postalcode',
                       'city',
                       'latitude',
                       'longitude', 
                       'venue_name', 
                       'venue_latitude',
                       'venue_longitude']
    # Create the empty top venues dataframe
    df_restaurant = pd.DataFrame(columns=restaurants_columns)
    
    # Create a list of all the top venue latitude and longitude
    top_venue_lngs = df_top_venues['longitude'].values

    # Create a list of all the top venue names
    top_venue_names = df_top_venues['name'].values
  
    # Iterate over each of the top venues
    # The venue name, latitude and longitude are passed to the loop
    top_venue_lats = df_top_venues['latitude'].values
    
    for ven_name, ven_lat, ven_long in zip(top_venue_names, top_venue_lats, top_venue_lngs):
    
    # Configure additional Search parameters
    # This is the FourSquare Category Id for all food venues
    categoryId = '4d4b7105d754a06374d81259'
    radius = 500
    limit = 50
    
    # Contruct the FourSquare search API URL
    url = 'https://api.foursquare.com/v2/venues/search?client_id={}&client_secret={}&ll={},{}&v={}&categoryId={}&radius={}&limit={}'.format(
        cid,
        csecret,
        ven_lat,
        ven_long,
        '20180604',
        categoryId,
        radius,
        limit)
    
    # Make the search request
    results = requests.get(url).json()
    
    
    
    # Want a good selection of Restaurents
    # If less than 10 are returned ignore
    if len(results['response']['venues']) < 10:
        continue
        
    # Populate the new dataframe with the list of restaurants
    # Get the values for each Restaurant from the JSON
    for restaurant in results['response']['venues']:
      try:
        # Sometimes the Venue JSON is missing data. If so ignore and continue
        
        # Get location details
        rest_id = restaurant['id']
        rest_category = restaurant['categories'][0]['pluralName']
        rest_categoryID = restaurant['categories'][0]['id']
        rest_name = restaurant['name']
        rest_address = restaurant['location']['address']
        rest_postalcode = restaurant['location']['postalCode']
        rest_city = restaurant['location']['city']
        rest_latitude = restaurant['location']['lat']
        rest_longitude = restaurant['location']['lng']
        
        rest_url = 'https://api.foursquare.com/v2/venues/{}?client_id={}&client_secret={}&v={}'.format(
                rest_id, 
                cid,
                csecret,
                '20180604')
        resultf = requests.get(rest_url).json()
        rest_score = resultf['response']['venue']['rating']
        # Add the restaurant details to the datafram
        df_restaurant = df_restaurant.append({'id': rest_id,
                                           'score': rest_score,
                                            'category': rest_category,
                                            'categoryID': rest_categoryID,
                                            'postalcode': rest_postalcode,
                                            'name': rest_name,
                                            'address': rest_address,
                                            'city': rest_city,
                                            'latitude': rest_latitude,
                                            'longitude': rest_longitude,
                                            'venue_name': ven_name,
                                            'venue_latitude': ven_lat,
                                            'venue_longitude': ven_long}, ignore_index=True)
            
        # If there are any issue with a restaurant ignore and continue
      except:
            continue
'''

The above codes along with the dataframe it stored the data in, is available on my Github repository.


### Map 1 - Top venues along with the locations of the crimes of 2016-17

![Map 1](https://github.com/mayank-liv/Coursera_Capstone/blob/master/Capstone/Screenshot%20(57).png)

From this map, we can see the distribution of the top venues, as well as the location of the crimes of 2016-17. Clearly, the north of the city seems more unsafe, because of the larger number of crimes there. Also, since most of the top-venues are in South and Central New York, that is the location a user should prefer staying in and exploring.

### Map 2 - Heat Map of crimes of 2016-17 

![Map 2](https://github.com/mayank-liv/Coursera_Capstone/blob/master/Capstone/Screenshot%20(59).png)

Seeing this map, we can conclude that there are primarily 2 major hotspots for crimes in NYC, one in the souther fringes of the city, and one in the northern part. The northern part seems to be having a larger number of crimes. So, later on we will build on this and try to cluster these crime into 3 different clusters, based on their location.

### Map 3 - Recommended restaurants around Central Park, along with heat map of nearby crimes

![Map 3](https://github.com/mayank-liv/Coursera_Capstone/blob/master/Capstone/Screenshot%20(64).png)

We assume that seeing the earlier maps, the user chooses to visit a safe venue like Central Park, and later searches for the top restaurants around that venue. The map shows the top venue (Central Park) marked with a red star, along with a heat map based on the location of crimes that have occured here since 2006. Clearly, barely a few crimes have occured here, so its a very safe place to visit. Moreover, the location of crimes around Central Park seem to be focused around 3 hotspots, so those are the places a person needs to be most careful around. Also, the blue icons marked as thumbs show the top 10 restaurants, around Central Park. When we click on these icons, the restaurant's name, category as well as overall score pops up, which helps the user choose which restaurant he/she wants to visit. Since most of the top restaurants are towards the east of Central Park, that's where a user is recommended to go.


### Map 4 - Recommended restaurants around Hudson River Park, along with heat map of nearby crimes

![Map 4](https://github.com/mayank-liv/Coursera_Capstone/blob/master/Capstone/Screenshot%20(67).png)

Now, Hudson River Park is located at a relatively unsafe location, when compared to Central Park, which is why the heatmap is so dense. Since folium can print maps only when the numbers of makrers/ data points is less than 1000, we have shown only the crimes that have occured withing 460 metres of Hudson River Park. If the user wishes to visit this venue, he is recommended to be extra careful, and to spend as less time here as possible. We can also see the top restaurants around this venue, along with their category and ratings.

### Map 5 - Clustering of the crimes of 2016-17, on the basis of location

![Map 5](https://github.com/mayank-liv/Coursera_Capstone/blob/master/Capstone/Screenshot%20(74).png)

As we had seen in Map 2, the crimes of New York City in 2016-17 mostly occur around 2 hotspots. So, we used K-Means clustering to cluster the crimes into 3 separate clusters, based on their location. Clearly, the 2 clusters on the North seem very close together and have the greatest numbers of crimes and so are most dense, while the southern cluster is far of from them. There is clearly an area on the map devoid of crimes, which means that central NYC is the safest place to be.


### K-Means clustering - 

Clearly, the dataset we had procured had already classified the crimes into various categories, based on the type of offense, the type of crime, the location of it etc. Hence, there was a limited scope for us to further classify the data into newer categories. However, from Map 2, we saw that seemed to be 2 sepearate clusters of crimes in the year 2016-17. So that I wasn't being too rigid on our observations, I decided to apply K-means clustering with 3 different clusters, so that 3 clusters based on location could be formed. From Map 5, we can say that one of the clusters is in south NYC, one is in North-and-central NYC, and one cluster is in extreme north NYC, with very few crimes reported in NYC at all. Clearly, north NYC is highly unsafe, and isn't recommended to be visited for someone who doesn't know the place or the people well.

The code we use for the K-means clustering algorithm, is given below.

'''   

    # set number of clusters
    kclusters = 3

    # run k-means clustering
    kmeans = KMeans(n_clusters=kclusters, random_state=0).fit(dfaq)

    # check cluster labels generated for each row in the dataframe
    kmeans.labels_ 

    # add clustering labels
    df.insert(0, 'Cluster Labels', kmeans.labels_)
'''



## 4. Results - 

From the visualisation of data we have done before, we can come to the following conclusions.

* The safest location to stay in NYC, is Central NYC, in the region around Central Park.

* The safest months to visit NYC are November and December.

* The safest days of the week to come to NYC are Saturday, Sunday and Monday, based on the crime statistics since 2006.

* 00 hours. and the hour after it, is by far the unsafest time in NYC, so its recommended to stay indoors if one can. 

* The top 10 venues to visit in NYC, are : i) Central Park
                                          ii) Brooklyn Bridge Park
                                          iii) Minskoff Theatre
                                          iv) Long Meadow
                                          v) Hudson River Greenway Running Path
                                          vi) Gantry Plaza State Park
                                          vii) Brooklyn Heights Promenade
                                          viii) Bryant Park
                                          ix) Metropolitan Museum of Art
                                          x) Hudson River Park
 
 These recommendations are purely on the basis of current trends, and are subject to change with time. The other top venues can be seen in the notebook that I have uploaded.
 
 * The venues in central NYC, like Central Park, Bryant Park, Metropolitan Museum of Art etc are the safest to visit.
 
 * The top 3 crimes in NYC are : i) Possession of Marijuana
                                 ii) Assault
                                 iii) Theft of Services
Hence, a person who is new to the city is advised to be aware of these crimes.                                 
 
 * Crimes in NYC can basically be segregated into 3 clusters, based on location. Two clusters are very close by and have maximum number of crimes, in north NYC (with a few exceptions from central NYC too), while a relatively smaller number of crimes are spread over a cluster in southern NYC.
 
 * The top 10 recommended restaurants around the top venue a user wishes to explore, can be seen using the notebook. For now, in Map 3 and Map 4, I have shown a couple of such maps, which will help a user choose a safe restaurant to visit.




## 5. Discussion - 

The dataframe we have used here for the K-Means clustering of crimes, is the one containing crime records for 2016-17. Since this dataframe has just 26 records, I couldn't use any features other than the latitude and longitude coordinates, to train the K-means clustering model.

Ideally, I would've preferred using the dataframe having crime records of NYC since 2006, but unfortunately, Folium maps has a flaw wherein if we insert more than 1000 markers/data points in a map, the map doesn't get printed at all. And so even if we could train the model and classify the crimes into various clusters based on not only the latitude and longitude but also on the basis of the crime, the type of offence etc, we wouldn't be able to visualise it on the map as we have 4,798,339 data points in the dataset. Hence, we needed to settle with modelling using simple features (latitude and longitude) on the 2016-17 crime records dataset, so that the clustering could be done properly without too many anomalies.





## 6. Future Improvements on this -

I'll hope to find libraries other than folium that support the visualisation of datasets that are as large as the dataset of crimes since 2006, that we had used for a few of our visualisations. Moreover, just like in Google Maps once gets an estimate of the travel time between two points based on the history of the traffic trend on the route, I would like to integrate a more refined version of this above project on a similar platform to Google Maps, so that when one searches for places to visit in a city, he also gets to see the trends of the crimes around it, as well as the times that the place is safest to be visited.






