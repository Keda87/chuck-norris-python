"""
The MIT License (MIT)
Copyright (c) 2016 adiyatmubarak

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER DEALINGS IN THE SOFTWARE.
"""
import requests


class NorrisException(Exception):
    pass


class ChuckNorris(object):

    def __init__(self):
        self.base_url = 'http://api.icndb.com/jokes/'

    def random(self, total=None, first_name=None, last_name=None,
               categories=None, exclude_categories=None):
        params = {}
        url = self.base_url + 'random/'

        if total is not None:
            url += '%d/' % total

        if first_name is not None:
            params.update({'firstName': first_name})

        if last_name is not None:
            params.update({'lastName': last_name})

        if categories is not None:
            if hasattr(categories, '__iter__'):
                params.update({'limitTo': categories})
            else:
                raise NorrisException('Categories must be an iterable.')

        if exclude_categories is not None:
            if hasattr(exclude_categories, '__iter__'):
                params.update({'exclude': exclude_categories})
            else:
                raise NorrisException('Exclude categories must be an iterable.')

        try:
            response = requests.get(url, params=params)
            return response.json()
        except ValueError:
            return None

    def get_jokes_by_id(self, joke_id):
        url = self.base_url + '%d/' % joke_id
        response = requests.get(url)
        return response.json()

    def get_jokes_count(self):
        url = self.base_url + 'count/'
        response = requests.get(url)
        return response.json()

    def get_jokes_categories(self):
        url = self.base_url.replace('jokes/', 'categories')
        response = requests.get(url)
        return response.json()

    def get_all_jokes(self):
        response = requests.get(self.base_url)
        return response.json()
