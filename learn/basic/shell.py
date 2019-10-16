from subprocess import *
# r = run(['df', '-h'])
c = call(['ls'])
result = getoutput(['ls'])

print(len(result))
