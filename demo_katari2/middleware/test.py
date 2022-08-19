from Katari.interfaces import MiddlewareInterface

class Test(MiddlewareInterface):

    def process_request(self, message):
        print(str(message))
        return message


    def process_response(self, message):
        print(str(message))
        return message

