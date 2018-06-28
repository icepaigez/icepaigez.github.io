import webapp2
import jinja2
import os

templateDir = os.path.join(os.path.dirname(__file__), 'templates')
jinjaEnv = jinja2.Environment(loader = jinja2.FileSystemLoader(templateDir),
                                    autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    def renderStr(self, template, **params): #template here refers to a file name, set as a parameter in this function
        t = jinjaEnv.get_template(template) #this stmt means jinja2 will call the file entered using its get_template function, and save the object in a variable
        return t.render(params) #it will then call its render function on the object with the parameters set to it, and return a string

    def render(self, template, **kw):
        self.write(self.renderStr(template, **kw))

class MainPage(Handler):
    def get(self):
        self.render("crypto.html")
    def post(self):
        wod = self.request.get("text") #text refers to the text entered to the name attr in the html form. request.get always returns a string
        self.render("crypto.html", some=wod) #if you want any data returned in the same textarea box,
                                            #instantiate it in the html textarea box and reference it here "text=wod" i.e. the word at the left hand side of the assignment statement is the variable to be printed out in the html file and the right hand side is the value to be printed out




#this is the handler for the form: when you send a GET request, the url is '/'
# class MainPage(webapp2.RequestHandler):
#     def get(self):
#         #self.response.headers['Content-Type'] = 'text/html'
#         self.response.write(form)
#
#     def post(self):
#         wod = self.request.get("text") #text refers to the text entered to the name attr in the html form above
#         self.response.write(wod)



app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
