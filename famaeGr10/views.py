from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import pandas as pd

contaminants = pd.read_csv('famaeGr10/data/contaminants2.csv', index_col=0)
zipcodes = pd.read_csv('famaeGr10/data/zip_codes2.csv')

df = contaminants.merge(zipcodes, left_on='locations_served', right_on='county')
df_simplified = df[['city', 'lat', 'long']]


def map(request):
  return render(request, 'map.html')

def byCity(request, id=None):
  print("id :", id)

  data_no_duplicate = df_simplified.drop_duplicates().reset_index()
  data_full = df.drop_duplicates().reset_index()

  if id == None:
    final_data = data_no_duplicate
  else:
    try:
      final_data = data_full[data_full['index'] == int(id)]
    except:
      return HttpResponse({"Error : Bad 'id' type (not int)"}, content_type = 'application/json')

  return HttpResponse(final_data.to_json(orient="records"), content_type = 'application/json')

def autocomplete(request, search=None):
  print("search :", search)

  custom_data = df_simplified.drop_duplicates().reset_index()

  final_data = custom_data[custom_data['city'].str.contains(search.upper())]

  return HttpResponse(final_data.to_json(orient="records"), content_type = 'application/json')