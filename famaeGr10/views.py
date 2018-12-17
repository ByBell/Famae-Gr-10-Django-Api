from django.http import HttpResponse, JsonResponse
import pandas as pd

contaminants = pd.read_csv('famaeGr10/data/contaminants2.csv', index_col=0)
zipcodes = pd.read_csv('famaeGr10/data/zip_codes2.csv')

data = contaminants.merge(zipcodes, left_on='locations_served', right_on='county')
data = data[['city', 'lat', 'long']]



def essai(request, zipcode):

    data2 = data.drop_duplicates().reset_index()
    del data2['index']

    json = data2.to_json(orient='records')[1:-1].replace('},{', '} {')
    dummyDict = {'data': json}

    return JsonResponse(dummyDict)