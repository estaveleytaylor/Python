from flask import Flask
import Climate_API as cli


app = Flask(__name__)


@app.route("/monthlytemperature/<variable>")
def temp(variable):
    print('we got here')
    country_code = cli.get_location_code(variable)
    result_dict = {}
    result_dict['Monthly Temperature'] = cli.data_request(country_code)
    return result_dict


@app.route("/monthlyprecipitation/<variable>")
def precip(variable):
    result_dict1 = {}
    result_dict1['Monthly Precipitation'] = cli.data_request_rain(cli.get_location_code(variable))
    return result_dict1

if __name__ == "__main__":
    app.run()