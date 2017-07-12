from clarifai.rest import ClarifaiApp
app=ClarifaiApp(api_key='a1b3910e08a4437b9fe85c5dbe967205')
mode1=app.models.get('food-items-v1.0')
response= mode1.predict_by_url('http://financialadvicenow.co.uk/wp-content/uploads/2015/12/The-dramatic-rise-of-the-robo-adviser.jpg')
print response