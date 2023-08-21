# to run ven in vscode terminal you can run this Command :  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

#Import FastApi and Uvicorn

from fastapi import FastAPI
import uvicorn

#Import api module from API directory and class models from Models directory
from API import api
from Models import models

# Create app
app = FastAPI()

# Define Configure Function which will configure routing configuration and other probbable configuration like Database Connection configuration
def configure():
    configure_routing()

# Configure routing .API's are in API directory and here we route them 
def configure_routing():
    app.include_router(api.router)
    # Root 
    
# Run the application in the uvicorn 
if __name__ == '__main__':
    configure()
    uvicorn.run(app,host="127.0.0.1", port=8000)
else:
    configure()