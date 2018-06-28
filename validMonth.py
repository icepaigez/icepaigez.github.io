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
                     

##def escapeHtml(s):
##    if s == ">":
##        return "&gt;"
##    elif s == "<":
##        return "&lt;"
##    elif s == ' " ':
##        return "&quot;"
##    elif s == "&":
##        return "&amp;"
##    else:
##        return None
##    
import cgi
def escapeHtml(s):
    return cgi.escape(s, quote = True)





##    nuMth = month.lower()
##    if nuMth.capitalize() in months:
##        return (nuMth.capitalize())
##    else:
##        return (None)



class Dog:

    #this is a class attr and is shared by all the instances of this class
    #diff from attrs unique to each instance
    species = "mammal"

    #a method for creating the initial attrs of the class, must have the self variable
    #and at least one argument. "self" is an attribute of class instances or copies
    #and will differ among instances.
    def __init__(self, name, age):
        self.name = name
        self.age = age

##def rot13(a):
##    alp = "abcdefghijklmnopqrstuvwxyz"
##    for i in range(len(alp)):
##        if alp.index(a) < 13:
##            return alp[alp.index(a) + 13]
##        else:
##            return alp[alp.index(a) - 13]
            
        
def escape_html(s):
    for (i, o) in (("&", "&amp;"), (">", "&gt;"), ("<", "&lt;"), ('"', "&quot;")):
        s = s.replace(i, o)
    return s
                          
def rot13(a):
    alp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = ""
    x = 0
    for i in a:
        if i in alp and alp.index(i) < 13 and i.islower() and x < len(a):
            count = count + alp[alp.index(i) + 13]
            x += 1
        elif i in alp and 13 <= alp.index(i) <= 25  and i.islower() and x < len(a):
            count = count + alp[alp.index(i) - 13]
            x += 1
        elif i in alp and 25 <= alp.index(i) <= 38 and x < len(a):
            count = count + alp[alp.index(i) + 13]
            x += 1
        elif i in alp and alp.index(i) > 38 and x < len(a):
            count = count + alp[alp.index(i) - 13]
            x += 1
        elif i not in alp:
            count = count + i
            x +=1
    return count
    
            
    
    
        
            
        
    
        
                   
                        
        
    
    
