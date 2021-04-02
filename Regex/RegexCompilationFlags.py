import re
# pat = re.compile(r'^([a-zA-Z0-9_\'-]+)@([0-9a-z\.-]+)\.([a-z\.]{2,6})$')
pattern = re.compile(r"""
^([a-zA-Z0-9_\'-]+) #first part of email
@                   #single @ sign
([0-9a-z\.-]+)      #email provider
\.                  #single period
([a-z\.]{2,6})$     #com, org, net, etc.
""",re.VERBOSE | re.IGNORECASE)

match = pattern.search("dannythompson@Yahoo.com")
print(match.group())
print(match.groups())   