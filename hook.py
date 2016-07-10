import os                                                                                                                                              
from flask import Flask                                                                                                                                
app = Flask(__name__)                                                                                                                                  
                                                                                                                                                       
@app.route('/deploy', methods=['GET', 'POST'])                                                                                                         
def deploy():                                                                                                                                          
        ret = os.system("sh /your/path/to/build.sh >> /your/path/to/build.log &")                                                      
        return "build successful!"                                                                                                                     
                                                                                                                                                       
@app.route("/")                                                                                                                                        
def index():                                                                                                                                           
        return "Flask works!"                                                                                                                          
                                                                                                                                                       
if __name__ == "__main__":                                                                                                                             
    app.run("0.0.0.0",8989)
