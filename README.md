# RiceDataBase
Django backend database for riceDB.

# JSON API
* GET /query/?q=[search term] - returns a JSON containing a list of rices which have some form of match with the search term
* POST /upload/ - Accepts a JSON in the format {"upstream":[link to github URL]} and verifies it before adding it to the RiceDB rice index.
