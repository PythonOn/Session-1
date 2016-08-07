#Execute this through command prompt/ terminal using this command: python 24HourClock.py or python3 24HourClock.py


#Python's input function always returns a string data which is assigned to variables currentTime and delayTime here.
currentTime = input("What's the current time (24 Hours clock) ? ")
delayTime = input("Alarm must ring after how many hours ? ")

#But to perform calculations we HAVE to convert string data into integer

#And that is done by writing
# (int)(String_name)
# Suppose a = "4"
# Then if we write print(a+2) expecting it to print 6, but instead it prints 42. That's because It converts 2 to a string and then concatenates it to "4" which is a string.
# Try to google these fancy words like concatenation and ofcourse we're always there for you.

#So what we do is to convert a from string to an int
#that's done by a = (int)(a)
# Now a = 4, quotes removed and string converted to int

#So that's why here we have written (int)(currentTime) and int(delayTime)
waitTime = (int(currentTime) + (int(delayTime) % 24))%24
print("Alarm time will be", waitTime, "hours.")
