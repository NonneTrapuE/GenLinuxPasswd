# GenLinuxPasswd
Generate a linux password hash 

This small python script generate a password hash for Linux user without pam security policies.
It simple : launch script, tape your dreaming password and press enter.

to launch script:
```$> python -Wignore GenLinuxPasswd.py```

You can use result for inject password in /etc/shadow or with useradd/usermod command.

ex :

```
$> useradd nonnetrapue --password $(python -Wignore GenLinuxPasswd.py)
tape your password here
$> su nonnetrapue
Password:
```




référence: (https://www.cyberciti.biz/faq/understanding-etcshadow-file/)
