# You
# will
# be
# given
# some
# emails
# until
# you
# receive
# the
# command
# "End".Create
# the
# following
# custom
# exceptions
# to
# validate
# the
# emails:
# NameTooShortError -
# raise it
# when
# the
# name in the
# email is less
# than or equal
# to
# 4("peter"
# will
# be
# the
# name in the
# email
# "peter@gmail.com")
# MustContainAtSymbolError -
# raise it
# when
# there is no
# "@" in the
# email
# InvalidDomainError -
# raise it
# when
# the
# domain
# of
# the
# email is invalid(valid
# domains
# are:.com,.bg,.net,.org)
# When
# an
# error is encountered,
# raise it
# with an appropriate message:
#     NameTooShortError - "Name must be more than 4 characters"
# MustContainAtSymbolError - "Email must contain @"
# InvalidDomainError - "Domain must be one of the following: .com, .bg, .org, .net"
# Hint: use the following syntax to add message to the Exception: MyException("Exception Message") If the current email is valid, print "Email is valid" and read the next one.

# INPUT:
# abc@abv.bg

# OUTPUT:
# Traceback (most recent call last):
#   File ".\email_validator.py", line 20, in <module>
#     raise NameTooShort("Name must be more than 4 characters")
# __main__.NameTooShort: Name must be more than 4 characters

# INPUT:
# peter@gmail.com
# petergmail.com

# OUTPUT:
# Email is valid
# Traceback (most recent call last):
#   File ".\email_validator.py", line 18, in <module>
#     raise MustContainAtSymbolError("Email must contain @")
# __main__.MustContainAtSymbolError: Email must contain @

# INPUT:
# peter@gmail.hotmail

# OUTPUT:
# Traceback (most recent call last):
#   File ".\email_validator.py", line 22, in <module>
#     raise InvalidDomainError("Domain must be one of the folowing: .com, .bg, .org, .net")
# __main__.InvalidDomainError: Domain must be one of the folowing: .com, .bg, .org, .net

from errors import MustContainAtSymbolError, NameTooShortError, InvalidDomainError, InvalidDomainNameError

allowed_domains = {"com", "bg", "org", "net"}

while True:
    line = input()
    if line == "End":
        break
    email_parts = line.split("@")
    if len(email_parts) == 2:
        raise MustContainAtSymbolError("Email must contain @")
    name, domain = email_parts

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    post_domain_part = domain.split(".")[-1]
    if len(post_domain_part) < 2 or not all([len(x) > 1 for x in post_domain_part]):
        raise InvalidDomainNameError("Invalid domain name.")

    if not post_domain_part in allowed_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid.")
