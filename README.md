# this is a motherheckin READ ME
## the age old question finally answered - hot dogs or legs?

## these are our References, and theres some photos photos from google missing:
Understanding ML for images:
- https://gist.github.com/fchollet/0830affa1f7f19fd47b06d4cf89ed44d
- https://towardsdatascience.com/embedding-machine-learning-models-to-web-apps-part-1-6ab7b55ee428
- https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html 

Images: https://github.com/daj/legs-or-hotdogs-images 

# RUNNING THE APP 
## pip install -r requirements.txt
## python server.py

## Check your KERAS BACKEND
if Theano -> leave it be
if Tensorflow -> Follow The well crafted guide "To change Keras Backend" below

## To change Keras Backend
go to your room directiory: /Users/yourname/.keras/
find the keras.json file
edit the backend to say theano

# Endpoint SZN yo
## get '/'
renders the home page 

## get '/fight'
shuffles the photos in the battle against the ML classifier
renders the page to click start

## get '/test'
throws on over to page where you upload an image and have it be classified

## post '/leaderboard'
body contains name and time of your score if you got 8/8 classifications right
you pop yourself on the Leadboard via the Leaderboard class with this request
restarts everytime the server restarts

## post '/fightPlay '
Triggers the start of the game and loads the next image from the previously shuffled array
as you click a "hotdogs" or "legs" button, and updates your score if chosen correctly

## post '/testUpload'
triggering this uploads the photo you have selected on your computer and runs the 
classification algorithm on it and displays the results

# some architecture jazzzZZz
## ML Jawn - Sara
data - holds the test and train photos for the model (pulled from a github repository)
     - testing data also holds the sample images given for the test
model.py and hd_or_legs.h5 are the model -- run model.py to compile and save the model
     - the model is saved to the file hd_or_legs.h5 and loaded for predictions
modelUtils is list of functions used by the rest of the app to call on the model to predict for certain situations
     - the predict function utilizes the loaded model to predict upon the tensorized images (which is done by load_image)

## Web Slingin - Ezaan
server - hold main app and routes for Flask app, and main web interactions
static - holds the static photos for the fight and uploaded photos
templates - html files for each pages

yeezy szn approachin 
yeehaw
got the horses in the BACK

# zoo wee mama
