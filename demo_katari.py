import settings
from soft_phone import 
from Katari import KatariApplication
from Katari.sip.response import ResponseFactory

app = KatariApplication(settings=settings)

@app.invite()
def do_invite(request, client):
    # add INVITE logic here 
    response = ResponseFactory.build(200) # 200 OK
    app.send(request.create_response(response), client)

@app.register()
def do_register(request, client):
    # add REGISTER logic here 
    response = ResponseFactory.build(401) # 401 unauthorized 
    app.send(request.create_response(OK200()), client)

@app.options()
def do_options(request, client):
    # add OPTIONS logic here 
    response = ResponseFactory.build(200) # 200 OK
    app.send(request.create_response(response), client)

@app.info()
def do_info(request, client):
    # add INFO logic here 
    response = ResponseFactory.build(200) # 200 OK
    app.send(request.create_response(response), client)

if __name__ == "__main__":   
    app.run()