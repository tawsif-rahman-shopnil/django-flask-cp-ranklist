from flask import Flask, render_template, jsonify
import requests
import json

app = Flask(__name__)

def color_class(judge, rating):
    if judge == 'cf':
        if not rating or rating < 1200: return 'cf-newbie'
        elif rating < 1400: return 'cf-pupil'
        elif rating < 1600: return 'cf-specialist'
        elif rating < 1900: return 'cf-expert'
        elif rating < 2100: return 'cf-candidate-master'
        elif rating < 2300: return 'cf-master'
        elif rating < 2400: return 'cf-international-master'
        elif rating < 2600: return 'cf-grandmaster'
        elif rating < 3000: return 'cf-internation-grandmaster'
        else: return 'cf-legendary-grandmaster'
    elif judge == 'cc':
        if not rating or rating < 1400: return 'cc-1star'
        elif rating < 1600: return 'cc-2star'
        elif rating < 1800: return 'cc-3star'
        elif rating < 2000: return 'cc-4star'
        elif rating < 2200: return 'cc-5star'
        elif rating < 2500: return 'cc-6star'
        else: return 'cc-7star'

@app.route('/')
def ranklist():
    url = "YOUR_URL"  # Replace with your URL
    response = requests.get(url)
    data = response.json()

    for user in data:
        user['color_class'] = color_class(user.get('judge'), user.get('rating'))

    data = sorted(data, key=lambda x: x.get('lup', 0), reverse=True)

    return render_template("ranklist.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
