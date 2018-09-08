# advo-signin
Advo assembly sign-in using unique ids retrieved from stdin (from a rfid reader). Code for a raspberry pi daemon.

In order to reuse this code, you need to create two files:

 - password file: defaults to "pwd.txt", but filename can be changed in line 11 of signin.py.
 first line is email address, second line is password. Since emails are sent using Google's smtp servers, a google email address is assumed. Make sure you have "Allow Less Secure Apps: ON" in your google account settings, or google will not allow the login.
 
 - names file: running the daemon will fail unless a names file is specified as the first (and only) command line argument.
  each name gets it's own line.
  
  
  # to run:
 - Run signin.py, passing in your names text file as an argument. 

 - Scan each rfid chip, in the order that you put the names in the file. Ensure that the scan id is in stdin for the program to read. The program will start regular operation automatically once all chips are scanned.

 - When an rfid chip that is initialized at setup is scanned to stdin, the bot will send an email to advocate_email (line 10) at 3:00pm local time with a list of everyone who checked in that day. Note that if someone checks in on a non-assembly day, an email will be sent to the advocate on that day. This was designed to ensure the advocate does not need to pre-program the assembly dates, but can't be spammed with emails if someone decides to maliciously spam the scan on an off day. Besides, the advocate will see who did that, or this could be prevented altogether by simply only giving access to the rfid reader on assembly days.
