# **Neighborhood crime-records based venue suggestion**

# 1. Introduction - 


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

First, we use the link [New York City Neighborhoods Data](https://geo.nyu.edu/catalog/nyu_2451_34572 ) to get data about all the nieghborhoods in New York and their boroughs, in the form of a json file. The link is about the dataset of NYC neighborhoods of the year 2014, so there might be negligibly small inaccuracies in some data. Also, the data we get won't be too clean or organised, and won't really make sense to a layman, so we will need to clean it. 

We extract only the features we want, namely : 

*   Borough - the broroughs mentioned in the New York City dataset
* Neighborhood - the various neighborhoods in the aforesaid boroughs
*   Latitude - the latitude coordinates of the neighborhood
* Longitude - the longitude coordinates of the neighborhood


This data is extracted and converted into a panda dataframe, so that it will be easier for us to manipulate this dataframe later on. 

Later, we use Foursquare API to extract the top venues in the nighborhood the user wants to search for venues in. 

It gives us another chaotic form of data. However, we scrap the data and finally extract the dataframe consisting of just 4 columns - 

*   name - the name of the venue
*   category - the kind of place it is (restaurant, museum etc)
* latitude - the latitude coordinates of the venue
* longitude - the longitude coordinates of the venue


Finally, I need to mention about the other major dataset which we shall be using. The dataset about the crimes can be accessed in the website [New York City Crime Data](https://data.cityofnewyork.us/Public-Safety/NYC-crime/qb7u-rbmr) Here, a list of all the crimes occuring in New York City in the year 2016, in various neighborhoods, is recorded and stored in immense detail. The dataset has the following data, who's description is shown in the table too. 

| Field name | Description |
|--|--|
| CMPLNT_NUM |Randomly generated persistent ID for each complaint  |
| CMPLNT_FR_DT | Exact date of occurrence for the reported event (or starting date of occurrence, if CMPLNT_TO_DT exists) |
|CMPLNT_FR_TM|Exact time of occurrence for the reported event (or starting time of occurrence, if CMPLNT_TO_TM exists)|
| CMPLNT_TO_DT | Ending date of occurrence for the reported event, if exact time of occurrence is unknown |
|  CMPLNT_TO_TM| Ending time of occurrence for the reported event, if exact time of occurrence is unknown |
|  RPT_DT|Date event was reported to police|
|   KY_CD | Three digit offense classification code |
|  OFNS_DESC|  Description of offense corresponding with key code|
|PD_CD|Three digit internal classification code (more granular than Key Code)|
| PD_DESC |  Description of internal classification corresponding with PD code (more granular than Offense Description)|
|  CRM_ATPT_CPTD_CD| Indicator of whether crime was successfully completed or attempted, but failed or was interrupted prematurely |
|LAW_CAT_CD|Level of offense: felony, misdemeanor, violation|
|  JURIS_DESC|  Jurisdiction responsible for incident. Either internal, like Police, Transit, and Housing; or external, like Correction, Port Authority, etc.|
|BORO_NM| The name of the borough in which the incident occurred |
|ADDR_PCT_CD|The precinct in which the incident occurred|
| LOC_OF_OCCUR_DESC | Specific location of occurrence in or around the premises; inside, opposite of, front of, rear of |
|PREM_TYP_DESC| Specific description of premises; grocery store, residence, street, etc. |
|PARKS_NM|Name of NYC park, playground or greenspace of occurrence, if applicable (state parks are not included)|
| HADEVELOPT | Name of NYCHA housing development of occurrence, if applicable |
|X_COORD_CD|X-coordinate for New York State Plane Coordinate System, Long Island Zone, NAD 83, units feet (FIPS 3104)  |
|Y_COORD_CD|Y-coordinate for New York State Plane Coordinate System, Long Island Zone, NAD 83, units feet (FIPS 3104)|
|Latitude  | Latitude coordinate for Global Coordinate System, WGS 1984, decimal degrees (EPSG 4326) |
|Longitude| Longitude coordinate for Global Coordinate System, WGS 1984, decimal degrees (EPSG 4326) |









We will only use the features that are necessary, as you will see in the implementation of the project.





<!--stackedit_data:
eyJoaXN0b3J5IjpbOTUyMjU0NzU3LDc3NTE1Njk5NSw3NzUxNT
Y5OTVdfQ==
-->