# CoffeePlease
CoffeePlease is a small Pyhton app developed to demonstrate the capability of collecting and acting on data using tkinter and smptlib in Python

SMTP CONFIG:

in order to get this to work you will need to configure the server.login and server.sendmail on line 81 and 82

The configuration is as follows:

[line 81]: <youremail@gmail.com> - as the smtp server is running gmail you will need to use a gmail for this to work, enter your gmail account here.
[line 81]: <YourAppKeyOrEmailPassword> - using gmail we can generate app keys, in order for this to work you will need to generate one from your gmail account settings
[line 82]: <yourEmail@gmail.com> - this defines the sender email that the the recipient will see. put your sending email here
[line 82]: <recipientEmail@domain.com> - put the recipients email here, this is the person receiving the request by email
[line 82]: "your ask nicely has been placed"... - this is the message that the recipient will receive, its set to include the output of the radio buttons as a variable.
