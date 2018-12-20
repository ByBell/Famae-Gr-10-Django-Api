from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from functools import lru_cache

import pandas as pd

s = pd.read_csv('famaeGr10/data/sources.csv', index_col=0)


def map(request):
  return render(request, 'map.html')


def sources(request):
  dataset = s
  dots = dataset[['id', 'city', 'lat', 'long']].drop_duplicates(['lat', 'long']).dropna().reset_index()

  return HttpResponse(dots.to_json(orient="records"), content_type="application/json")


def search(request, search=None):
  dataset = s

  # Get rows where the city or supplier name starts by search
  cityNameStartsWith = dataset['city'].str.startswith(search.upper())
  supplierNameStartsWith = dataset['supplier_name'].str.startswith(search.upper())

  # Get results
  results = dataset[cityNameStartsWith | supplierNameStartsWith]
  results = results[['id', 'city', 'supplier_name', 'lat', 'long']].drop_duplicates().reset_index()

  return HttpResponse(results.head(10).to_json(orient="records"), content_type='application/json')

def source(request, id):
  dataset = s

  rows = dataset[dataset['id'] == int(id)]

  results = rows.groupby(['id', 'city', 'supplier_name', 'lat', 'long'], as_index=False)
  results = results.apply(lambda x: x[['contaminant', 'average_result', 'max_result', 'health_limit', 'health_limit_exceeded', 'legal_limit', 'legal_limit_exceeded']].to_dict('r'))
  results = results.reset_index().rename(columns={0: 'contaminants'}).to_json(orient='records')

  return HttpResponse(results, content_type='application/json')