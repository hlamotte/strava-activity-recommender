# strava-activity-recommender

We are creatures of habit and tend to run the same routes. Getting inspiration for a new route can be challenging, it's hard to know what other options are out there that satisfy your preferences.

[Stava](https://www.strava.com/) is a social network for running, uploading telemetry from your runs, such as GPS and heart rate sensor measurements, as posts to share with your Strava friends. I frequently find myself getting inspiration from others on Strava for new running routes, leading me to wonder if it might be possible to create a recommender system for recommending new runs that suit my preferences.

Strava provides an [API](https://developers.strava.com) to gain access to all the "activities" uploaded by a user. This dataset of a user's historical activities could be used to get an impression of the kind of activities a user likes.

Now that we have a dataset for representing a user's preferences, we need a dataset containing a large number of possible options for activities. Strava has a repository of "segments", routes that the public have submitted, and often compete to get best times. These segments can be used as a library of possible routes.


## ToDo
- [ ] Individual user data
  - [x] Authenticating user
  - [x] Collecting user data
  - [ ] Visualizations on user data
- [x] Route data
  - [x] Authentication
  - [x] Exhaustive search of segments in grid
- [ ] Module docs
- [ ] GitHub Actions CI?
- [ ] Recommendation system models
  - [ ] Unsupervised approach
- [ ] Enriching data
  - [ ] [Google maps API](https://developers.google.com/maps/documentation/places/web-service/search)

## Starting virtual environment
```
source venv/bin/activate
```

## Strava Authentication
[Stravio](https://github.com/sladkovm/stravaio) is a great library for handling collecting the tokens and handling the responses.

## Strava data schema
- SummaryActivity
- DetailedActivity
  - Segment efforts
  - Best efforts

## Exhaustive search
The Strava API only returns 10 of segments within the rectangle defined by two lat/long coordinates. In order to collect all the segments within a rectangle, the API must be called on sub-rectangles of increasingly smaller sizes until all of the segments in an area have been collected. Halving the size of the domain along one axis and recursing until the API call returns less than 10 results should result in an exhaustive search.

# Build docs
```
$ sphinx-build -b html docs build
```


