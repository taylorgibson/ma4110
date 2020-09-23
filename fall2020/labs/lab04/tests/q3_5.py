test = {   'name': 'q3_5',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> # Make sure to remove the '(No previous year)' CEOs;\n>>> '(No previous year)' not in with_previous_compensation.column('% Change')\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> import math;\n'
                                               '>>> # You have the column, but some of your values may be incorrect;\n'
                                               ">>> t = with_previous_compensation.sort('2014 Total Pay ($)', descending = True);\n"
                                               ">>> value = t.column('2014 Total Pay ($)').item(0);\n"
                                               '>>> math.isclose(value, 67700000.0, rel_tol = 0.01)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # You have the column, but your number of rows is not correct;\n>>> with_previous_compensation.num_rows == 81\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
