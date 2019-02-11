print 'Welcome to Delta Airlines.'
print 'Please enter your first name.'
name = raw_input()
print 'Now please enter your last name' , name+'.'
last = raw_input()
print 'Please enter your luggage weight', name , last+'. (pounds)'
pounds = int (raw_input()) 
if pounds > 50:
    print 'Your luggage exceeds our 50lb weight limit. You will receive an additional $25 fee.'
print 'Thank you for your business', name,last+', have a nice flight.'

