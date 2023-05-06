class NameTooShortError(Exception):
    """Name must be more than 4 characters"""


class MustContainAtSymbolError(Exception):
    """Email must contain @"""


class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""


email = input("Enter an email that is going to be validated: ")

first_check = email.split("@")[0]
if len(first_check) < 5:
    raise NameTooShortError("Name must be more than 4 characters")

if "@" not in email:
    raise MustContainAtSymbolError("Email must contain @")

second_check = email.split(".")[-1]
if second_check != "com" and second_check != "bg" and second_check != "net" and second_check != "org":
    raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

print(f'Email is valid')
