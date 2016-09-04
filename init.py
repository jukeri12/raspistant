'''

I N I T . P Y

Initialize pyttsx and all relevant data for Raspistant to work.

'''
import pyttsx
import os, time
from Assistant.functions import dict_gen, check_pyttsx_settings, generate_notifications
engine = pyttsx.init()

# Set timezone
os.environ['TZ'] = 'Europe/Helsinki'

# Read a text file to set settings for the pyttsx module
t2s_file = open('pyttsx-settings.ini', 'r')
t2s_settings = dict_gen(t2s_file.read())
time.tzset()

# Quit the program if the settings were not valid!
if not check_pyttsx_settings(t2s_settings):
    print "Text-to-speech settings were invalid! Program aborting."
    # TODO: Proper closing of opened files, etc.
    exit()

# This way the settings stay pretty flexible and dynamic. Static file would avoid confusion though
for setting, value in t2s_settings.iteritems():
    engine.setProperty(setting, int(value))

# Generate our notifications for the day from a text file
notifications_file = open('notifications.ini', 'r')
notifications = dict_gen(notifications_file.read())
notifications = generate_notifications(notifications)

# Remove all unnecessary stuff from memory
t2s_file.close()
notifications_file.close()