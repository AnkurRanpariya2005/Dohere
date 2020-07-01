import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
  
	return "{\"name\":\"anur\"}"
app.run()    
@app.route('/', methods=['GET'])
class coust():
	def __create__(self,Name,Lname):
		self.Name=Name
		self.Lname=Lname
		
	def add(self,name,lname):
		save.coust(name,lname)
		arr.append(save)
		
	def ds(Name,Lname):
		print("Name:",Name)
		print("Last Name:",Lname)
		return  arr
  
save=("")
arr=[]		
  
e1=save.get(input(),input())
	



app.run()
