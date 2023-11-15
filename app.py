from flask import Flask, render_template
from datetime import datetime, timedelta
import requests

app = Flask(__name__)

# Replace 'your_api_key' and 'your_api_secret' with your actual Codeforces API key and secret
CODEFORCES_API_KEY = '8d2638e3c29c506b17a1b7cc45f9e70619d10d3e'
CODEFORCES_API_SECRET = 'e9e07d34373f8781a7bf28f6a08a9302170c7e1e'

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
    url = "https://codeforces.com/api/user.ratedList"
    
    # Add the API key and secret to the request headers
    headers = {'key': CODEFORCES_API_KEY, 'secret': CODEFORCES_API_SECRET}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return f"Error fetching data from Codeforces API. Status code: {response.status_code}"

    try:
        data = response.json()
    except ValueError:
        return "Error parsing JSON data from Codeforces API."

    if data['status'] != "OK":
        return f"Codeforces API error: {data['comment']}"

    users = data['result']

    # Filter users from BAIUST
    baiust_users = [user for user in users if user.get('organization') == 'BAIUST']

    # Get the timestamp for 3 months ago
    three_months_ago = (datetime.now() - timedelta(days=90)).timestamp()

    for user in baiust_users:
        # Check if the user was active in the last 3 months
        if user.get('lastOnlineTimeSeconds', 0) < three_months_ago:
            user['rating'] = 0

        user['color_class'] = color_class('cf', user.get('rating'))

    baiust_users = sorted(baiust_users, key=lambda x: (x.get('rating', -1), x.get('handle')), reverse=True)

    return render_template("ranklist.html", data=baiust_users)

if __name__ == '__main__':
    app.run(debug=True)
