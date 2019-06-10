#1. Introduction - 



In today's day and age, travelling to a new place is no longer as tedious a process as it was a few decades back. Unlike before,  when one had to rely on locals to guide them to places like nearby restaurants that they could visit, one can just spend 5 minutes on the Internet and find a list of tens of restaurants in a given locality. There are various sites and resources, like TripAdvisor and even FourSquare API, that can provide such a suggestions list in just a few seconds.

However, one of the flaws or rather, shortcomings about this is that although these services provide the list of venues along with its precise locations and reviews, it overlooks one key factor everyone needs to keep in mind while in a new city- how safe the neighborhood they are visiting, is. 

For istance, one can be visiting a neighborhood in an entirely new city for the first time, and so might need some help inorder to decide which restaurant to visit for a meal. A regular internet search might provide the person with an idea of which restaurants are the best suited for the person, but it wouldn't give one any idea about how safe the neighborhood that he/she might be visiting, is. Hence, criminals and thiefs could take advantage of the fact that he/she is new to the nighborhood, and so one could get robbed, muggled, or something even worse can happen.

Hence, in a way, the restaurant with the best ratings isn't necessarily the one that should be suggested to a person. Instead, one should also be given an idea about how safe the neighborhood around that restaurant is, at the time of the day one's planning to visit it. My project aims to address this problem and find a solution around it.


## Idea for the project - 

I believe that when a newcomer to a city searches for top venues in a certain neighborhood, the regular information of the venues he gets, should be supplemented with the criminal record of places around that neighborhood.

Hence, I aim to provide this additional information to the user, with my Capstone project.

My project will be based on the nighborhoods and venues of New York City, along with the crime record of it. 

When a person searches for top venues at a particular neighborhood, Foursquare API is scrapped to provide us with the data about the top venues at that neighbrhood.

We manipulate this data, adding additional information and dropping unnecessary information, to provide us with a more desired list of top venues.

Now, the major part of my project comes into play. I use the data I have about the crime record at places in New York City, and provide the user with information about the history of the predominant crimes committed within a certain distance of the top venues.

Finally, we will provide this information in the format of a map too, inorder to give the user a better understanding of the data, as well as a sense of direction and a better perspective.

## Target User Base - 

As I've explained in excruciating detail earlier, this project aims to help travellers to new cities, specially the ones that are most vulnerable to crimes. This list of people that are more vulnerable to such crimes include:



*   Solo travellers
*  Small groups of elderly tourists
*  Small groups of female tourists
*   People who don't speak the local tongue
*  Young travellers
*  New residents of a city


---







# 2. Data Description - 

For this project, we will primarily need 2 major datasets - 



*  Dataset about neighbrhoods in New York City and their top venues
*  Dataset about the crime records in various locations in New York City

First, we use the link [New York City Neighborhoods Data](https://geo.nyu.edu/catalog/nyu_2451_34572 ) to get data about all the nieghborhoods in New York and their boroughs, in the form of a json file. The link is about the dataset of NYC neighborhoods of the year 2014, so there might be negligibly small inaccuracies in some data. Also, the data we get won't be too clean or organised, and won't really make sense to a layman, as you can see in the picture shown below.



<img src="http://drive.google.com/uc?export=view&id=
1PA1b7efkgFdQtgyF23Z8pjJikkkXnb9D">

Now, although the data seems chaotic, we extract only the features we want, namely : 

*   Borough - the broroughs mentioned in the New York City dataset
* Neighborhood - the various neighborhoods in the aforesaid boroughs
*   Latitude - the latitude coordinates of the neighborhood
* Longitude - the longitude coordinates of the neighborhood


This data is extracted and converted into a panda dataframe, so that it will be easier for us to manipulate this dataframe later on. 

Later, we use Foursquare API to extract the top venues in the nighborhood the user wants to search for venues in. The query looks similar to the one mentioned below - 

<img src="http://drive.google.com/uc?export=view&id=
1ZITOgWMzC8Bq3odJ7gDUpX5ACzENLmIG">

It gives us another chaotic form of data -

<img src="http://drive.google.com/uc?export=view&id=
1-4hIk1gPa6HtB4DuyobBUDtmjSDeU7yh
">

However, we scrap the data and finally extract the dataframe consisting of just 4 columns - 



*   name - the name of the venue
*   category - the kind of place it is (restaurant, museum etc)
* latitude - the latitude coordinates of the venue
* longitude - the longitude coordinates of the venue


Finally, I need to mention about the other major dataset which we shall be using. The dataset about the crimes can be accessed in the website [New York City Crime Data](https://data.cityofnewyork.us/Public-Safety/NYC-crime/qb7u-rbmr) Here, a list of all the crimes occuring in New York City in the year 2016, in various neighborhoods, is recorded and stored in immense detail. The dataset has the following data, who's description is shown in the table too. 

<img src="http://drive.google.com/uc?export=view&id=
1TQVj2JcWwvOiIeKucNM0d7gzj0BdyvQh">
<img src="http://drive.google.com/uc?export=view&id=
1vNfCgwwBcVd3a7EPGkqLAB5xmLLopX2G">
<img src="http://drive.google.com/uc?export=view&id=
1etMsaFt40MrRw_HwH4JBu_JVCeyM5hEB">

We will only use the features that are necessary, as you will see in the implementation of the project.
