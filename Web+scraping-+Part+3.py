
# coding: utf-8

# # Toronto neighbourhoods and boroughs web scraping

# ## 1. First part of the assignment - 

# First, I have to import the libraries needed

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np


# Now, I get the contents of the Wikipedia page using the BeautifulSoup package

# In[2]:


site = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text
soup = BeautifulSoup(site, 'lxml')

#print(soup.prettify())

table= soup.find('table', class_='wikitable sortable')

rows_table = table.find_all('tr')

#print(rows_table)

list = []

for tr in rows_table:
    td=tr.find_all('td')
    row_txt= [pr.text for pr in td]
    list.append(row_txt)
    
#print (list)


# My next step is to take only the rows that have an assigned Borough

# In[3]:


df = pd.DataFrame(list, columns=['PostalCode', 'Borough', 'Neighborhood'])[1:]

df = df[df['Borough'] != 'Not assigned']

df.head()


# Now, I need to make sure that more than one neighbourhood having the same 'PostalCode' is grouped together

# In[4]:


same_pcode = df["PostalCode"].duplicated(keep= False)

df1 = df[-same_pcode]

print(df1.head())

df2 = df[same_pcode]

print(df2.head())


# Due to some issues with the duplicated function on python, it didn't work in one go. Hence I needed to keep repeating it multiple times before it worked like it was supposed to. Instead of using loop, I hard coded this part.

# In[5]:


bool1= df2.duplicated('PostalCode', keep='last')
df3= df2[bool1]
df4 = df2[-bool1]
bool2 = df3.duplicated('PostalCode', keep='last')
df5 = df3[bool2]
df6 = df3[-bool2]
#print(df4)
#print(df5)
bool3 = df5.duplicated('PostalCode', keep='last')
df7= df5[bool3]
df8 = df5[-bool3]
bool4= df7.duplicated('PostalCode', keep='last')
df9 = df7[bool4]
df10 = df7[-bool4]
bool5= df9.duplicated('PostalCode', keep='last')
df11 = df9[bool5]
df12 = df9[-bool5]
bool6= df11.duplicated('PostalCode', keep='last')
df13 = df11[bool6]
df14 = df11[-bool6]
bool7= df13.duplicated('PostalCode', keep='last')
df15 = df13[bool7]
df16 = df13[-bool7]
bool8= df15.duplicated('PostalCode', keep='last')
df17 = df15[bool8]
df18 = df15[-bool8]
final1 = pd.merge(df18, df16, on= ['PostalCode', 'Borough'],how='outer')
final2 = pd.merge(final1, df16, on= ['PostalCode', 'Borough'],how='outer')
final3 = pd.merge(final2, df14, on= ['PostalCode', 'Borough'],how='outer')
final4=  pd.merge(final3, df12, on= ['PostalCode', 'Borough'],how='outer')
final5=  pd.merge(final4, df10, on= ['PostalCode', 'Borough'],how='outer')
final6=  pd.merge(final5, df8, on= ['PostalCode', 'Borough'],how='outer')
final7=  pd.merge(final6, df6, on= ['PostalCode', 'Borough'],how='outer')
final8=  pd.merge(final7, df4, on= ['PostalCode', 'Borough'],how='outer')
final9=  pd.merge(final8, df1, on= ['PostalCode', 'Borough'],how='outer')
final9 = final9.replace(np.nan, '', regex=True)
columnNumbers = [x for x in range(final9.shape[1])]  

columnNumbers.remove(4) #removing column integer index 0
final9 = final9.iloc[:, columnNumbers]

final9



# Now, we need to combine all the different neigbourhood columns into a single one

# In[6]:


final9.columns =['PostalCode', 'Borough', 'Neighborhood_a', 'Neighborhood_b',
       'Neighborhood_c', 'Neighborhood_d', 'Neighborhood_e', 'Neighborhood_f',
       'Neighborhood_g', 'Neighborhood_h', 'Neighborhood_i']

final9['combined']=final9['Neighborhood_i']+','+final9['Neighborhood_h']+','+final9['Neighborhood_g']+','+final9['Neighborhood_f']+','+final9['Neighborhood_e']+','+final9['Neighborhood_d']+','+final9['Neighborhood_c']+','+final9['Neighborhood_b']+','+final9['Neighborhood_a']

final9= final9.loc[:,['PostalCode', 'Borough', 'combined']]
final9.columns=['PostalCode', 'Borough', 'Neighborhood']
final9.head()


# Now, we need to clean the data in the Neighborhood column so that the \n is removed

# In[7]:


def clean_df(x):
    x=x.replace("\n","").replace(",,,,","").replace(",,,","").replace(",,","")
    return x
final9['Neighborhood']= final9['Neighborhood'].apply(clean_df)
final9.head()


# I have cleaned the table contents and now I just need to print the table and its shape

# In[8]:


final9


# In[9]:


final9.shape


# This part of the assignment is now complete

# ## 2. Second part of the assignment - 

# In[10]:


Lat_file= pd.read_csv("Geospatial_Coordinates.csv")
Lat_file.columns=['PostalCode', 'Latitude', 'Longitude']

final10= pd.merge(final9, Lat_file, on=['PostalCode'])

final10.head()


# In[11]:


final10


# The Second Part of the assignment is now complete

# ## 3. Third part of the assingment - 

# In[12]:


get_ipython().system('conda install -c conda-forge folium=0.5.0 --yes ')
import folium


# In[18]:


CLIENT_ID = 'J1WNF1XMAB3QQNZ1KRZGNQCDWG5TOIIHJ2OUZNB3LKUDAPOC'

CLIENT_SECRET = 'CAST03F1YFNTHG1OCZEFERNMDPLR2EB0DWD1FBL3F1UHSD2D'

VERSION = VERSION = '20180605'

LIMIT = 100

RADIUS = 500


# First, we change our dataframe to include only the boroughs that include the word 'Toronto' in them 

# In[17]:


boolean = [ True if "Toronto" in dummy else False for dummy in final10['Borough']]

final11 = final10[boolean]

final11.head()


# We make a function to get the closest venues to our boroughs

# In[20]:


def nearby_places(names, latitudes, longitudes, radius=500):
    
    venues_list=[]
    for name, lat, lng in zip(names, latitudes, longitudes):
                  
        url ='https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
            CLIENT_ID, 
            CLIENT_SECRET, 
            VERSION, 
            lat, 
            lng, 
            50, 
            100)
            
        results = requests.get(url).json()["response"]['groups'][0]['items']
        
        venues_list.append([(
            name, 
            lat, 
            lng, 
            v['venue']['name'], 
            v['venue']['location']['lat'], 
            v['venue']['location']['lng'],  
            v['venue']['categories'][0]['name']) for v in results])

    nearby_venues = pd.DataFrame([item for venue_list in venues_list for item in venue_list])
    nearby_venues.columns = ['Neighborhood', 
                  'Neighborhoods centre Latitude', 
                  'Neighborhoods centre Longitude', 
                  'Venue', 
                  'Venue Latitude', 
                  'Venue Longitude', 
                  'Venue Category']
    
    return(nearby_venues)

Toronto_info = nearby_places(names=final11['Neighborhood'],
                                   latitudes=final11['Latitude'],
                                   longitudes=final11['Longitude']
                                  )

Toronto_info.head()


# Now, we check how many unique venues are there
# 

# In[21]:


print("Number of unique venues are :" + str(len(Toronto_info['Venue Category'].unique())))


# We convert categorical data into numbers, using pd.getdummies

# In[29]:


Toronto_x = pd.get_dummies(Toronto_info[['Venue Category']], prefix="", prefix_sep="")

Toronto_x['Neighborhood'] = Toronto_info['Neighborhood'] 


Toronto_x.head()


# In[30]:



Toronto_grouped = Toronto_x.groupby('Neighborhood').mean().reset_index()
Toronto_grouped.shape


# We try and print the most common venues around our neughbourhoods

# In[39]:


def return_most_common_venues(row, num_top_venues):
    row_categories = row.iloc[1:]
    row_categories_sorted = row_categories.sort_values(ascending=False)
    
    return row_categories_sorted.index.values[0:num_top_venues]


# In[40]:


num_top_venues = 8

indicators = ['st', 'nd', 'rd']

columns = ['Neighborhood']
for ind in np.arange(num_top_venues):
    try:
        columns.append('{}{} Most Common Venue'.format(ind+1, indicators[ind]))
    except:
        columns.append('{}th Most Common Venue'.format(ind+1))

neighborhoods_venues_sorted = pd.DataFrame(columns=columns)
neighborhoods_venues_sorted['Neighborhood'] = Toronto_grouped['Neighborhood']

for ind in np.arange(Toronto_grouped.shape[0]):
    neighborhoods_venues_sorted.iloc[ind, 1:] = return_most_common_venues(Toronto_grouped.iloc[ind, :], num_top_venues)

neighborhoods_venues_sorted


# Now I perform K-Means clustering on the above data

# In[43]:


from sklearn.cluster import KMeans

kclusters = 5

Toronto_grouped_clustering = Toronto_grouped.drop('Neighborhood', 1)

kmeans = KMeans(n_clusters=kclusters, random_state=0).fit(Toronto_grouped_clustering)


kmeans.labels_[0:10]
Toronto_grouped= pd.merge(final11,Toronto_grouped, on='Neighborhood', how='right')


# In[44]:


Toronto_merged = Toronto_grouped
Toronto_merged['Cluster Labels'] = kmeans.labels_

Toronto_merged = Toronto_merged.join(neighborhoods_venues_sorted.set_index('Neighborhood'), on='Neighborhood', how='left')
Toronto_merged.head() 


# Now, we just print a map

# In[45]:


import matplotlib.cm as cm
import matplotlib.colors as colors


# In[46]:


map_clusters = folium.Map(location=[43.6532, -79.3832], zoom_start=11)


x = np.arange(kclusters)
ys = [i+x+(i*x)**2 for i in range(kclusters)]
colors_array = cm.rainbow(np.linspace(0, 1, len(ys)))
rainbow = [colors.rgb2hex(i) for i in colors_array]


markers_colors = []
for lat, lon, poi, cluster in zip(Toronto_merged['Latitude'], Toronto_merged['Longitude'], Toronto_merged['Neighborhood'], Toronto_merged['Cluster Labels']):
    label = folium.Popup(str(poi) + ' Cluster ' + str(cluster), parse_html=True)
    folium.CircleMarker(
        [lat, lon],
        radius=10,
        popup=label,
        color=rainbow[cluster-1],
        fill=True,
        fill_color=rainbow[cluster-1],
        fill_opacity=0.7).add_to(map_clusters)
       
map_clusters

