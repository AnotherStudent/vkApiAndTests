# vkApiAndTests

```
$ python main.py
[{'response': [{'city': {'id': 2, 'title': 'Санкт-Петербург'},
                'first_name': 'Павел',
                'id': 1,
                'last_name': 'Дуров',
                'nickname': '',
                'sex': 2,
                'site': 'http://t.me/durov'}]},
 {'response': [{'first_name': 'Александра',
                'hidden': 1,
                'id': 2,
                'last_name': 'Владимирова',
                'nickname': '',
                'sex': 1,
                'site': ''}]},
 {'response': [{'deactivated': 'deleted',
                'first_name': 'DELETED',
                'id': 3,
                'last_name': '',
                'sex': 0}]}]
```

```
$ python -m pytest tests.py -v
====================== test session starts ======================
platform darwin -- Python 3.6.1, pytest-3.0.7, py-1.4.33, pluggy-0.4.0 --
cachedir: .cache
rootdir: inifile:
plugins: hypothesis-3.37.0
collected 2 items 

tests.py::test_durov_id PASSED
tests.py::test_bad_address PASSED

=================== 2 passed in 0.16 seconds ====================
```
