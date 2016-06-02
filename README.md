# chuck-norris-python
[![Build Status](https://travis-ci.org/Keda87/chuck-norris-python.svg?branch=master)](https://travis-ci.org/Keda87/chuck-norris-python)

Python wrapper for "The Internet Chuck Norris Database" http://www.icndb.com/api/

This python library has the same response with JSON API response but already parsed as python dictionary for easy usage.

#### Example usage:
```python
from chuck import ChuckNorris

cn = ChunkNorris()
# Get random jokes.
cn.random()

# Get multiple random jokes.
cn.random(total=5)

# Get random jokes with manipulate actor name (first name or last name).
cn.random(first_name='John')
cn.random(last_name='Doe')
cn.random(first_name='John', last_name='Doe')

# Get random jokes filter by categories (must be an iterable).
cn.random(categories=['nerdy', 'geeks'])

# Get random jokes filter exclude by categories (must be an iterable).
cn.random(exclude_categories=['nerdy'])

# Get jokes by specific ID.
cn.get_jokes_by_id(15)

# Get total jokes count.
cn.get_jokes_count()

# Get all jokes categories.
cn.get_jokes_categories()

# Get entire jokes data.
cn.get_all_jokes()
```

