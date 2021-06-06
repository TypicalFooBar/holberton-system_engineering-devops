class Crypto:
    @staticmethod
    def encrypt(stringToEncrypt):
        newString = ''

        for char in stringToEncrypt:
            newString += chr(ord(char) + 5)

        return newString

    @staticmethod
    def decrypt(stringToDecrypt):
        newString = ''

        for char in stringToDecrypt:
            newString += chr(ord(char) - 5)

        return newString

class Server:
    def handleRequest(self, stringFromClient):
        print("SERVER: " + stringFromClient)

    def handleEncryptedRequest(self, stringFromClient):
        print("SERVER BEFORE DECRYPTION: " + stringFromClient)

        stringFromClient = Crypto.decrypt(stringFromClient)

        print("SERVER AFTER DECRYPTION: " + stringFromClient)

class Internet:
    server = Server()

    def routeRequestToServer(self, stringFromClient):
        print("INTERNET: " + stringFromClient)

        self.server.handleRequest(stringFromClient)

    def routeEncryptedRequestToServer(self, stringFromClient):
        print("INTERNET: " + stringFromClient)

        self.server.handleEncryptedRequest(stringFromClient)

class Client:
    internet = Internet()

    def sendRequest(self, stringToSend):
        print("NO ENCRYPTION")
        print("-------------")
        print("CLIENT: " + stringToSend)
        
        self.internet.routeRequestToServer(stringToSend)
        print()

    def sendEncryptedRequest(self, stringToSend):
        print("ENCRYPTION")
        print("----------")
        print("CLIENT BEFORE ENCRYPTION: " + stringToSend)

        stringToSend = Crypto.encrypt(stringToSend)

        print("CLIENT AFTER ENCRYPTION: " + stringToSend)
        
        self.internet.routeEncryptedRequestToServer(stringToSend)

        print()
        

client = Client()

client.sendRequest("Howdy, y'all!")
client.sendEncryptedRequest("Hey, this should NOT be readable on the internet...")