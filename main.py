# Import engine and other stuff from init.py
from init import engine, notifications
from Assistant.functions import clean_exit, compare_time
from datetime import timedelta, datetime

# Do the main loop.
run = True

# note: this only works with the presumption that no one wants a notification at 00:00.
checked_time = datetime.now().replace(hour=0, minute=0)

while run == True:
    # Poll the clock to see if something is happening right now.
    now = datetime.now()

    # This might not be optimal (it has caused a segfault before)
    for time, text in notifications.iteritems():
        if compare_time(now, time) and not compare_time(now, checked_time):
            checked_time = datetime.now()
            engine.say(text)
            print text
            # Test, remove this.
            if text == 'exit':
                run = False

# TODO: Make a clean method for the program
clean_exit()