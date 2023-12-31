
from flask import Flask, request
import redis

app = Flask(__name__)
version = "1.7.1"

r = redis.Redis(host="cache-server", port=6379)

@app.route("/getregion", methods = ["GET"])
def getregion():
    value ='<h1>Not found</h1>'
    country = request.args.get("country")
    try:
        city = r.get (country)
        value = '''<h1> {} is in {} </h1> <p><a href= "http://63.32.118.206">home</a>'''.format(city.upper(), country.upper())
    except:
        pass
    return  value

@app.route("/version")
def getversion():
    return version

@app.route("/saveregion", methods = ["GET"])
def saveregion():
    value = "<h1> Failed to save</h1>"

    country = request.args.get("country")
    city = request.args.get("city")
 
    try:
        r.set(country,city)
        value = '''<h1> {} is in {} saved successfully </h1><p><a href= "http://63.32.118.206">home</a>'''.format(city.upper(), country.upper())
    except:
        pass
    return  value

# @app.route("/getregion")
# def lookup():
#     value = "N/A"
#     country = request.args.get("country")
#     try:
#         city = r.get(country)
#         if city:
#             value = city.decode("utf-8")
#     except Exception as e:
#         print(f"Error: {e}")
#     return value

# @app.route("/version")
# def getversion():
#     return version

# @app.route("/saveregion/<country>/<city>")
# def savedata(country, city):
#     value = "pass"
#     try:
#         r.set(country, city)
#     except Exception as e:
#         value = "fail"
#         print(f"Error: {e}")
#     return value

# if __name__ == "__main__":
#     app.run(debug=True)

