"""
Python wrapper for `The Internet Chuck Norris Database` API at http://www.icndb.com/api/.

:author:     --  Adiyat Mubarak <adiyatmubarak@gmail.com>
:link:       --  http://adiyatmubarak.web.id/
:license:    --  MIT License - http://www.opensource.org/licenses/mit-license.php
"""
import requests


class NorrisException(Exception):
    pass


class Norris(object):

    def __init__(self):
        self.id = None
        self.joke = None
        self.categories = None

    def __repr__(self):
        return '<{cls}: {joke}>'.format(
            cls=self.__class__.__name__,
            joke=self.joke
        )


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
            data = response.json()
            data = data['value']
            if isinstance(data, list):
                results = []
                for i in data:
                    norris = Norris()
                    norris.id = i['id']
                    norris.joke = i['joke']
                    norris.categories = i['categories']
                    results.append(norris)
                return results

            norris = Norris()
            norris.id = data['id']
            norris.joke = data['joke']
            norris.categories = data['categories']
            return norris
        except ValueError:
            return Norris()

    def get_jokes_by_id(self, joke_id):
        if isinstance(joke_id, str):
            raise NorrisException('ID is not a number.')
        url = self.base_url + '%d/' % joke_id
        try:
            response = requests.get(url)
            data = response.json()
            data = data['value']
            norris = Norris()
            norris.id = data['id']
            norris.joke = data['joke']
            norris.categories = data['categories']
            return norris
        except ValueError:
            return Norris()

    def get_jokes_count(self):
        url = self.base_url + 'count/'
        response = requests.get(url)
        return response.json()['value']

    def get_jokes_categories(self):
        url = self.base_url.replace('jokes/', 'categories')
        response = requests.get(url)
        return response.json()['value']

    def get_all_jokes(self):
        response = requests.get(self.base_url)
        data = response.json()
        data = data['value']
        results = []
        for i in data:
            norris = Norris()
            norris.id = i['id']
            norris.joke = i['joke']
            norris.categories = i['categories']
            results.append(norris)
        return results
