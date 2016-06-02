"""
Python wrapper for `The Internet Chuck Norris Database` API at
http://www.icndb.com/api/.
This wrapper has the same response with the API json response but returns
python dictionary for easy usage.

:author:     --  Adiyat Mubarak <adiyatmubarak@gmail.com>
:link:       --  http://adiyatmubarak.web.id/
:license:    --  MIT License - http://www.opensource.org/licenses/mit-license.php
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
