def validMonth(month):
    months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
    month_abbvs = dict((m[:3].lower(),m) for m in months)
    if month:
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)

def validDay(day):
    if int(day) in range(1, 32):
        return int(day)
    else:
        return None

def validYear(year):
    if year and year.isdigit():
        year = int(year)
        if year in range(1900, 2021):
            return year

given_string = "I think %s is a perfectly normal thing to do in public."
def sub1(s):
    return given_string%s #the "%s" after "given_string" is a variable and any data
                        #entered will go to replace the %s inside the string.i.e.
                        #means %variable
gT = "I think %s and %s are perfectly normal things to do in public."
def sub2(s1, s2):
    return gT%(s1, s2)

given_string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
def sub_m(name, nickname):
    return given_string2 % {"name":name , "nickname":nickname}


def escape_html(s):
    for (i, o) in (("&", "&amp;"), (">", "&gt;"), ("<", "&lt;"), ('"', "&quot;")):
        s = s.replace(i, o)
    return s
                       
'''
def escapeHtml(s):
    if s == ">":
        return "&gt;"
    elif s == "<":
        return "&lt;"
    elif s == ' " ':
        return "&quot;"
    elif s == "&":
        return "&amp;"
    else:
        return None
'''    
import cgi
def escapeHtml(s):
    return cgi.escape(s, quote = True)




'''
    nuMth = month.lower()
    if nuMth.capitalize() in months:
        return (nuMth.capitalize())
    else:
        return (None)
'''
