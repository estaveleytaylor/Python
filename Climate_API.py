import pandas as pd
import requests
import json
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import ast
import xlrd
from scipy.stats import sem
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
from statsmodels.tsa.stattools import adfuller

file_name = '/Users/bootcamp/Documents/Countries_And_Codes.xlsx'
Countries_And_Codes = pd.read_excel(io=file_name)

# code = None

def get_location_code(country_input):
    # global country_input
    # global code
    code = ''
    # country_input = input('Enter a Country ')
    for i in range(len(Countries_And_Codes)):
        if str(country_input) == (Countries_And_Codes['Location'][i]):
            code = (Countries_And_Codes['Code'][i])
            # print('Weather Station code = ' + code)
            # plot()
    print(code)
    return code
    # if code is None:
    #     print('Invalid Country Name!')
    #     set_location_code(country_input)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def data_request(code):
    global average_of_monthly_averages
    data = []
    month = []
    average_of_monthly_averages = []
    r = requests.get('http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1980/1999/' + code)
    a = ast.literal_eval(r.content.decode())
    print(a)
    s1 = json.dumps(a) #string
    d2 = json.loads(s1) #list

    for year in d2:
        monthly_temps_for_years = (year['monthVals'])
        data.append(monthly_temps_for_years)

    for j in range(12):
        for i in range(len(data)):
            temps = (data[i][j])
            month.append(temps)

    composite_list = [month[x:x + 15] for x in range(0, len(month) + 1, 15)]

    for i in range(len(composite_list) - 1):
        average_of_monthly_averages.append(np.mean(composite_list[i]))

    hottest_month_index = average_of_monthly_averages.index(max(average_of_monthly_averages))
    hottest_month_temperature = np.max(average_of_monthly_averages)
    hottest_month = months[hottest_month_index]
    # print('The hottest month in: ' + country_input + ' is ' + hottest_month + ' where the average temperature is: ' + str(round(hottest_month_temperature, 1)) + '°C' + '!')

    global errors
    errors = []

    for i in range(len(composite_list)-1):
        errors.append(sem(composite_list[i]))

    result_dict = {}
    result_dict['Monthly Temperature'] = average_of_monthly_averages
    return result_dict

def data_request_rain(code):
    global average_of_monthly_averages_rain
    data_rain = []
    month_rain = []
    average_of_monthly_averages_rain = []
    r_rain = requests.get('http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/pr/1980/1999/' + code)
    a_rain= ast.literal_eval(r_rain.content.decode())
    s1_rain = json.dumps(a_rain)
    d2_rain = json.loads(s1_rain)

    for year in d2_rain:
        monthly_rain_for_years = (year['monthVals'])
        data_rain.append(monthly_rain_for_years)

    for j in range (12):
        for i in range(len(data_rain)):
            rainfall = (data_rain[i][j])
            month_rain.append(rainfall)

    composite_list_rain = [month_rain[x:x + 15] for x in range(0, len(month_rain)+1, 15)]

    for i in range(len(composite_list_rain)-1):
        average_of_monthly_averages_rain.append(np.mean(composite_list_rain[i]))

    dryest_month_index = average_of_monthly_averages_rain.index(min(average_of_monthly_averages_rain))
    dryest_month_rainfall = np.min(average_of_monthly_averages_rain)
    dryest_month = months[dryest_month_index]
    print('The dryest month in: ' + country_input + ' is ' + dryest_month + ' where the average rainfall is: ' + str(round(dryest_month_rainfall, 1)) + 'mm' + '!')

    global errors_rain
    errors_rain = []

    for i in range(len(composite_list_rain)-1):
        errors_rain.append(sem(composite_list_rain[i]))

    result_dict = {}
    result_dict['Monthly Precipitation'] = average_of_monthly_averages
    return result_dict
