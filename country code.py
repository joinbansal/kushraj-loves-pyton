country_code = {'India' : '0091',
                'Austrailia' :'0025',
                'Nepal' : '00977'}

print("Country code for india-")
print(country_code.get('india', 'Not Found'))

print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))