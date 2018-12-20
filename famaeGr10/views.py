from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from functools import lru_cache

import pandas as pd


def map(request):
  return render(request, 'map.html')


def sources(request):
  dataset = get_dataset()
  dots = dataset[['id', 'city', 'lat', 'long']].drop_duplicates(['lat', 'long']).reset_index()

  return HttpResponse(dots.to_json(orient="records"), content_type="application/json")


def search(request, search=None):
  dataset = get_dataset(drop_duplicates=True)

  # Get rows where the city or supplier name starts by search
  cityNameStartsWith = dataset['city'].str.startswith(search.upper())
  supplierNameStartsWith = dataset['supplier_name'].str.startswith(search.upper())

  # Get results
  results = dataset[cityNameStartsWith | supplierNameStartsWith]
  results = results[['id', 'city', 'supplier_name', 'lat', 'long']].drop_duplicates().reset_index()

  return HttpResponse(results.head(10).to_json(orient="records"), content_type='application/json')

def source(request, id):
  dataset = get_dataset()

  rows = dataset[dataset['id'] == int(id)]

  results = rows.groupby(['id', 'city', 'supplier_name', 'lat', 'long'], as_index=False)
  results = results.apply(lambda x: x[['contaminant', 'average_result', 'max_result', 'health_limit', 'health_limit_exceeded', 'legal_limit', 'legal_limit_exceeded']].to_dict('r'))
  results = results.reset_index().rename(columns={0: 'contaminants'}).to_json(orient='records')

  return HttpResponse(results, content_type='application/json')


def get_dataset(drop_duplicates=False):
  # Read contaminants and zip codes CSV files
  contaminants = pd.read_csv('famaeGr10/data/contaminants2.csv', index_col=0)
  zipcodes = pd.read_csv('famaeGr10/data/zip_codes2.csv', index_col=0)

  # Join both files
  return contaminants.merge(zipcodes, left_on='locations_served', right_on='county')