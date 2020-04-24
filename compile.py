
# compile
# python compile.py --template template_default

# read index 

class TemplateReader:
    def __init__(self, path):
        self.path = path
    
        file = open(path, 'r') 
        content = file.read()
        file.close()
        
        # find <%SYMBOL%>

            

