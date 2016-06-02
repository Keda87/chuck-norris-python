# chuck-norris-python
[![Build Status](https://travis-ci.org/Keda87/chuck-norris-python.svg?branch=master)](https://travis-ci.org/Keda87/chuck-norris-python)

Python wrapper for "The Internet Chuck Norris Database" http://www.icndb.com/api/

This python library has the same response with JSON API response but already parsed as python dictionary for easy usage.
Compatible with python 2 & 3.

#### Example usage:
```python
from chuck import ChuckNorris

cn = ChunkNorris()

# Get random jokes.
cn.random()

# Get multiple random jokes.
data = cn.random(total=5)
for i in data:
    print(i.id)
    print(i.joke)
    print(i.categories)

# Get random jokes with manipulate actor name (first name or last name).
data = cn.random(first_name='John')
data = cn.random(last_name='Doe')
data = cn.random(first_name='John', last_name='Doe')
print(data.id)
print(data.joke)
print(data.categories)

# Get random jokes filter by categories (must be an iterable).
data = cn.random(categories=['nerdy', 'geeks'])
print(data.id)
print(data.joke)
print(data.categories)

# Get random jokes filter exclude by categories (must be an iterable).
data = cn.random(exclude_categories=['nerdy'])
print(data.id)
print(data.joke)
print(data.categories)

# Get jokes by specific ID.
data = cn.get_jokes_by_id(15)
print(data.id)
print(data.joke)
print(data.categories)

# Get total jokes count.
data = cn.get_jokes_count()
print(data)  # int

# Get all jokes categories.
data = cn.get_jokes_categories()
for i in data:
    print i  # string

# Get entire jokes data.
cn.get_all_jokes()
for i in data:
    print(i.id)
    print(i.joke)
    print(i.categories)
```

