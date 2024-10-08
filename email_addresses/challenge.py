"""
The Challenge

Did you know that there are many ways to write someone’s Gmail email address?
We can take someone’s Gmail address and add a plus (+) symbol and a string
before the @ symbol, and they’ll get any email we send to that new address.
That is, as far as Gmail addresses are concerned, all characters from a +
symbol to just before the @ symbol are ignored.

For example:
I tell people that my Gmail address is daniel.zingaro@gmail.com, but that’s
only one way to write it.
If you send email to daniel.zingaro+book@gmail.com or
daniel.zingaro+hi.there@gmail.com, I’ll get it. (Choose your favorite. Say hi!)
Dots before the @ symbol are also ignored in Gmail addresses.
For example:
If you send email to
danielzingaro@gmail.com (no dot at all),
daniel..zingaro@gmail.com (two dots in a row),
da.nielz.in.gar.o..@gmail.com (chaotic dots),
daniel.zin.garo+blah@gmail.com, and so on, I’ll get it.
Last thing: uppercase and lowercase differences throughout the address are
ignored. I hope you’re not firing a flurry at me by this point, but I’d get
anything you send to
Daniel.Zingaro@gmail.com,
DAnIELZIngARO+Flurry@gmAIL.COM, and so on.

In this problem, we’re provided with email addresses, and we’re asked to
determine the number of them that are unique.
The rules for email addresses in this problem are the same as those discussed
for Gmail: characters from a + symbol to just before the @ symbol are ignored,
dots before the @ symbol are ignored, and case throughout the entire address is
ignored.

Input
- List of strings each one representing an email address.

Output
- An integer representing the number of not repeating email addresses.
"""


def count_unique_emails(emails):
    unique_emails = set()
    for email in emails:
        unique_emails.add(clean_email(email))
    return len(unique_emails)


def clean_email(email):
    email = email.lower()
    local_part, domain = email.split("@")
    if local_part.find("+") != -1:
        local_part = local_part[: local_part.find("+")]
    local_part = local_part.replace(".", "")
    return local_part + "@" + domain
