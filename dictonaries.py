ex_dict = {'alok' : [14, 'okey'],
           'tithi' : [11, 'good'],
           "juthi" : [9, 'good'],
           "laddu" : [1.5, 'cute']}

print(ex_dict)
print(ex_dict['alok'])
ex_dict['angshu'] = [2.5, 'cute']
ex_dict['tithi'][0] = [11.6]
print(ex_dict)

ex_dict['oioi'] = [0.00000000000000001, 'meh']
print(ex_dict)

del ex_dict['oioi']
print("After delete", ex_dict)
