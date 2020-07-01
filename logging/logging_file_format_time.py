import logging


# Displaying the date/time in messages
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')


'''
The default format for date/time display (shown above) is like ISO8601 or RFC 3339. 
If you need more control over the formatting of the date/time, provide a datefmt argument to basicConfig, 
as in this example:
'''
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')