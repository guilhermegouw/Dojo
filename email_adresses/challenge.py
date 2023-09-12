"""
The Challenge

Did you know that there are many ways to write someone's Gmail email address?
- We can take someone's Gmail address and add a plus (+) symbol and a string 
before the @ symbol, and they'll get any email we send to that new address. 
That is, as far as Gmail addresses are concerned, all characters from a + 
symbol to just before the @ symbol are ignored. 
For example: 
I tell people that my Gmail address is daniel.zingaro@gmail.com, but that's 
only one way to write it. If you send email to daniel.zingaro+book@gmail.com
or
daniel.zingaro+hi.there@gmail.com,

(daniel.zingaro@gmail.com, 
daniel.zingaro+book@gmail.com, 
daniel.zingaro+hi.there@gmail.com)
All The Same!

- Dots before the @ symbol are also ignored in Gmail addresses. 
For example, if you send email to
danielzingaro@gmail.com
(no dot at all),
daniel..zingaro@gmail.com
(two dots in a row), 
da.nielz.in.gar.o..@gmail.com
(chaotic dots),
daniel.zin.garo+blah@gmail.com, 
and so on, I'll get it.

(
   danielzingaro@gmail.com,
   daniel..zingaro@gmail.com,
   da.nielz.in.gar.o..@gmail.com,
   daniel.zin.garo+blah@gmail.com
)
All The Same!

- Last thing: uppercase and lowercase diﬀerences throughout the address are 
ignored. I hope you're not ﬁring a ﬂurry at me by this point, but I'd get 
anything you send to Daniel.Zingaro@gmail.com, DAnIELZIngARO+Flurry@gmAIL.COM, 
and so on.
(
    Daniel.Zingaro@gmail.com, 
    DAnIELZIngARO+Flurry@gmAIL.COM
)
All The Same!

In this problem, we're provided with email addresses, and we're asked to 
determine the number of them that are unique. 
The rules for email addresses in this problem are the same as those discussed 
for Gmail: 
    - characters from a + symbol to just before the @ symbol are ignored
    - dots before the @ symbol are ignored 
    - case throughout the entire address is ignored.

Input

The input consists of 10 test cases. 
Each test case contains the following lines:
- A line containing integer n, the number of email addresses. 
n is between 1 and 100,000.
- n lines, each of which gives an email address. 
Each email address consists of at least one character before the @ symbol, 
followed by the @ symbol itself, followed by at least one character after 
the @ symbol. 
Characters before the @ symbol consist of letters, numbers, dots, and pluses. 
Characters after the @ symbol consist of letters, numbers, and dots.

Output

For each test case, output the number of unique email addresses.
The time limit for solving the test cases is 30 seconds.
"""

def how_many_unique_emails(num, *emails):
    valid_emails = []
    for email in emails:
        email.lower()
        domain = email[email.index('@'):]
        username = email[:email.index('@')]
        if '+' in username:
            plus = username.index('+')
            username = username[:plus]
        if '.' in username:
            username = username.replace('.', '')
        email = username + domain            
        valid_emails.append(email)
    return len(set(valid_emails))


if __name__=="__main__":
    how_many_unique_emails(2, 'daniel.zingaro@gmail.com', 'daniel.zingaro+doesnotcount@gmail.com')
