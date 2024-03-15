import random

def predict_weather():
    sunshine = random.choice(['True', 'False'])

    if sunshine == 'True':
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()
