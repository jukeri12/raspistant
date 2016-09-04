from datetime import timedelta, datetime

def dict_gen(string):
    # Split a formatted string and generate a dictionary out of it.
    if not string:
        print "No string supplied"
        return None

    # Attempt to generate a dict from the string.
    items = string.split('\n')
    dict = {}
    for item in items:
        # This only generates a 1-dimensional dictionary, so it stays relatively simple. It has a hack for line-endings though
        new_item = item.split(':')
        dict[new_item[0]] = new_item[1].replace('\r', '').replace(' ', '')
    return dict

def compare_time(time1, time2):
    # Compare minute and hour values of two datetime objects.

    if time1.minute == time2.minute and time1.hour == time2.hour:
        return True
    else:
        return False

def generate_notifications(dict):
    # Generate notifications from a dictionary.
    parsed = {}
    for time, text in dict.iteritems():
        parsed[datetime.strptime(time, '%H.%M')] = str(text)
    return parsed

def check_pyttsx_settings(dict):
    # Check that the pyttsx settings are okay.
    valid = True

    # Certain few parameters must exist.
    if not 'voice' in dict:
        valid = False

    # TODO: Check that values are within intended ranges.
    # for key, value in dict.iteritems...

    return valid

def clean_exit():
    # Clean memory and exit the program
    print 'safe exit'
    exit()