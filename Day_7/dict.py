thisdict = {
    1: 'orange',
    'Two': 'cherry'
}
for name in thisdict.values():
    print(f'values:{name}')

# key value :
for key, val in thisdict.items():
    print(f'key{key}, Values:{val}')

print(thisdict.get(3, 'Invalid option'))
