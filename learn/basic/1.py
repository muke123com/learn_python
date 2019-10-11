import re

m = re.match('foo', '1foo')
s = re.search('foo', '1foo')

if m is not None:
    print(m.group())
    print('***************')
    print(s.group())