test = {   'name': 'q3_5',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(change_in_death_rates, Table)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> change_in_death_rates.num_rows\n88', 'hidden': False, 'locked': False},
                                   {'code': ">>> all(elem in change_in_death_rates.column('Year') for elem in make_array(1971, 1973))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
