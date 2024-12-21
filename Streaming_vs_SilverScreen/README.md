# Predicting Film Success in a Rapidly Changing Industry

## Intro
The last few years have brought significant changes to just about every industry, but perhaps one of the most well-known and rapidly changing industries continues to be the film industry. With challenges presented by the COVID-19 pandemic severely impacting theater attendance, along with the rapid increase and availability of content on streaming services, the film industry looks much different today than it ever has in the past which has led to significant unpredictability in how well a film will perform. For this project, I plan to gather data on films released in the last 5-10 years amidst some of these huge changes (both within the industry and with people’s behaviors in consuming films) to see what factors could potentially predict a film’s success in this new landscape. 


## Data Sources and Relationships
The three data sources I chose are as follows: 
Flat File (.csv): https://www.kaggle.com/datasets/shivamb/netflix-shows 

The flat file data set contains a list of television shows and movies that are on the streaming service Netflix, including their original release dates and the date that they were added to streaming. Similar data sets also exist for Amazon Prime Video, Hulu, and Disney+ which I also plan to leverage in this project. 


API: https://developer.themoviedb.org/reference/intro/getting-started 

The movie database API contains tons of data on just about every movie, including the film’s title, synopsis, budget, genres, cast, crew, language, production company, popularity rank on The Movie Database, runtime, filming locations, and more.


Website: https://www.boxofficemojo.com/year/2021/?grossesOption=calendarGrosses 

Box Office Mojo contains box office performance data on films as well as information such as how many theaters films opened in and gross box office earnings both domestically and internationally. This site contains multiple tables that are broken out by year, so I will most likely be using multiple tables available on this site.
