from flask import Flask, render_template
import requests
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def get_codeforces_data():
    url = "https://codeforces.com/api/user.ratedList"
    response = requests.get(url)
    users = response.json()["result"]

    results = []
    for user in users:
        if "country" in user and user["country"] == "Bangladesh":
            try:
                results.append({
                    "id": user["handle"],
                    "name": f'{user.get("firstName", "")} {user.get("lastName", "")}'.strip(),
                    "rating": user["rating"],
                })
            except Exception as e:
                logger.error(f"Error processing user {user}: {e}")

    return results

@app.route("/")
def ranklist():
    codeforces_data = get_codeforces_data()
    codeforces_data.sort(key=lambda x: x["rating"], reverse=True)

    return render_template("ranklist.html", data=codeforces_data, enumerate=enumerate)

if __name__ == "__main__":
    app.run(debug=True)
