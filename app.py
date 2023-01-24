from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
#es = Elasticsearch(http://localhost:9200)
es = Elasticsearch(["http://localhost:9200"])

# health check endpoint
@app.route("/health")
def health_check():
    return "OK"

# endpoint for inserting or updating the city and its population
@app.route("/city", methods=["POST"])
def add_or_update_city():
    data = request.get_json()
    city = data.get("city")
    country = data.get("country")
    population = data.get("population")

    # check if city already exists in Elasticsearch
    res = es.search(index="my_index", body={"query": {"match": {"city": city}}})
    if res["hits"]["total"]["value"] > 0:
        # update population if city already exists
        es.update(index="cities", id=res["hits"]["hits"][0]["_id"], body={"doc": {"population": population}})
        return jsonify({"message": "City population updated successfully"})
    else:
        # insert new city and population
        es.index(index="my_index", body={"city": city, "country": country, "population": population})
        return jsonify({"message": "City added successfully"})

# endpoint for retrieving the population of city
@app.route("/city/<string:city>", methods=["GET"])
def get_city_population(city):
    res = es.search(index="my_index", body={"query": {"match": {"city": city}}})
    if res["hits"]["total"]["value"] > 0:
        return jsonify({"city": city, "population": res["hits"]["hits"][0]["_source"]["population"]})
    else:
        return jsonify({"message": "City not found"})

# HTML code that displays all the info in a webpage
@app.route("/cities")
def display_cities():
    res = es.search(index="my_index", body={"query": {"match_all": {}}})
    cities = res["hits"]["hits"]
    html = "<html><head><title>Cities and their Population</title></head><body>"
    html += "<table><tr><th>City</th><th>Country</th><th>Population</th></tr>"
    for city in cities:
        html += "<tr><td>" + city["_source"]["city"] + "</td>"
        html += "<td>" + city["_source"]["country"] + "</td>"
        html += "<td>" + str(city["_source"]["population"]) + "</td></tr>"
    html += "</table></body></html>"
    return html

if __name__ == "__main__":
    app.run(debug=True)
