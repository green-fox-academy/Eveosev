import re
#Reserved admin
string0 = 'admin'
string1 = 'Admin'
reversed0 = string0[::-1]
reversed1 = string1[::-1]
p = re.compile('[' + reversed0 + ']')
result1 = p.match(string1[::-1])
print(result1)

#Numbers below 100
string2 = ['0', '9', '55', '100', '101', '-4']
regex = '^[0-9]|(^[1-9][0-9]{1})|100'
p = re.compile(regex)
for i in string2:
    if p.search(i) != None:
        print(i)

#Hungarian mobile numbers
mobile_nums = ['+36 20 473 2746',
               '+36 30 217 4912',
               '00 36 70 381 1288',
               '00 36 31 471 2818',
               '+36 20 3173 4717',
               '+36 102 237 1121',
               '+49 20 483 1273',
               '36 70 381 2183'
               ]

regex1 = r'(\+36)?(00 36)?\s\d{2}\s\d{3}\s\d{4}'
p_phonecheck = re.compile(regex1)
for i in mobile_nums:
    if p_phonecheck.match(i) != None:
        print(i)



#GFA email address
email_book = ['john@greenfoxacademy.com',
              'jane.doe@greenfoxacademy.com',
              'jane@greenfox.academy',
              'john@wick.com',
              'jane@citromail.com',
              'janegreenfoxacademy.com']

regex_email = r'\S+(?=\@greenfox)'
p_emailcheck = re.compile(regex_email)
capturegroup = []

for  i in email_book:
    r_emailcheck = p_emailcheck.search(i)
    if r_emailcheck != None:
        capturegroup.append(r_emailcheck.group())
        print(f"{i}, the capture group is {r_emailcheck.group()}")
        

#Mobile number
        """
          Here phone number from UK will be matched
          00 44 / +44
        """
mobile_nums_44 = ['+44 20 473 2746',
               '+44 30 217 4912',
               '00 44 70 381 1288',
               '00 44 31 471 2818',
               '+44 20 3173 4717',
               '+44 102 237 1121',
               '+49 20 483 1273',
               '44 70 381 2183'
               ]
def mobilecheck(areacode, mobilelist):
    regex_mobile1 = r'[(\+)(00)]\s?44\s\d{2}\s\d{3}\s\d{4}'
    p_mobilecheck = re.compile(regex_mobile1)
    print(f"Mobile numbers from area {areacode} are:")
    for i in mobilelist:
        if p_mobilecheck.search(i) != None:
            print(i)
mobilecheck(44, mobile_nums_44)

#Image sourse
image_source = ['<img src="dog.png">',
                '<img alt="Cat picture" src="./images/cat-01.png">',
                '<script src="jquery.js"></script>']

def image_source_capture(imagelist):
    regex_image = r'(?<=src=\")\S+\w'
    p_image_source = re.compile(regex_image)
    for i in imagelist:
        m = p_image_source.search(i)
        if m != None:
            if m.group()[-3:] == 'png':
              print(m.group(0))

image_source_capture(image_source)














