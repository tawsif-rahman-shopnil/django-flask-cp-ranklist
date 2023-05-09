from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def ranklist():
    url_codeforces = "https://codeforces.com/api/user.ratedList"
    codeforces_response = requests.get(url_codeforces)
    codeforces_json = codeforces_response.json()
    codeforces_data = codeforces_json["result"]

    # Filter for Bangladeshi users and users from BAIUST
    filtered_data = [
        user for user in codeforces_data
        if user.get("organization") ==  "BAIUST"
    ]

    return render_template("ranklist.html", data=filtered_data)

if __name__ == '__main__':
    app.run(debug=True)
