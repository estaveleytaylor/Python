from flask import Flask
import Climate_API as cli


app = Flask(__name__)

@app.route("/monthlytemperature/<variable>/")
def temp(variable):
    result_dict = {}
    result_dict['Monthly Temperature'] = cli.data_request()
    return result_dict

@app.route("/monthlyprecipitation/<variable>/")
def precip(variable):
    result_dict1 = {}
    result_dict1['Monthly Precipitation'] = cli.data_request()
    return result_dict1

if __name__ == "__main__":
    app.run()