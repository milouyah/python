import configparser

config = configparser.ConfigParser()


print(config.sections())
config.read('example.ini')
print(config.sections())

# Test sections
print('bitbucket.org' in config) # true
print('bytebong.com' in config) # false

# Test values
print(config['bitbucket.org']['User']) # hg
print(config['DEFAULT']['Compression']) # 'yes'

topsecret = config['topsecret.server.com']
print(topsecret['ForwardX11']) # 'no'
print(topsecret['Port']) # '50022'

# Print keys in section
for key in config['bitbucket.org']:  
    print(key)

print(config['bitbucket.org']['ForwardX11']) # 'yes'

'''
Supported types
'''
print(' - Supported types - ')
print( int(topsecret['Port'])) # 50022
print( float(topsecret['CompressionLevel'])) # 9.0

print( topsecret.getboolean('ForwardX11')) # False
print( config['bitbucket.org'].getboolean('ForwardX11')) # True
print( config.getboolean('bitbucket.org', 'Compression')) # True

'''
Fallback Values
'''
print(' - Fallback Values - ')
print(topsecret.get('Port')) # '50022'
print(topsecret.get('CompressionLevel')) # '9'
print(topsecret.get('Cipher')) 
print(topsecret.get('Cipher', '3des-cbc')) # '3des-cbc'

print(topsecret.get('CompressionLevel', '3')) # '9'