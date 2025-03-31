import httpx 
import json
# from parser import responseParser 



class AfroMessage:
    def __init__(self, IdentifierId, senderName, auth_token, callbackUrl):
        self.baseUrl = 'https://api.afromessage.com/api/'
        self.sender_id = IdentifierId
        self.auth_token = auth_token
        self.senderName = senderName
        self.callbackUrl = callbackUrl 


    def sendMessage(self, to, message ):
        ''' Send [POST] SMS message to afro message api'''
        url = self.baseUrl + 'send'
        payload = {
            'from': self.sender_id,
            'senderName': self.senderName,
            'to': to,
            'message': message,
            'callbackUrl': self.callbackUrl
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.auth_token}'
        }
        try:
            response = httpx.post(url, data=json.dumps(payload), headers=headers)
            # Print response details for debugging
            # print(f"Status code: {response.status_code}")
            # print(f"Response content: {response.text}")
            return response
        except Exception as e:
            print(f"Error sending message: {e}")
            # Return a structured error response
            error_response = httpx.Response(
                status_code=500,
                content=json.dumps({
                    "success": False,
                    "error": str(e),
                    "message": "Error sending message"
                }).encode()
            )
            return error_response

    def sendBulkMessage(self, messageList, campaignTitle="", campaignMessage="", createCallback="", statusCallback=""):
        ''' Send [POST] Bulk SMS message to afro message api'''
        url = self.baseUrl + 'bulk_send'
        # check if messageList is type of  list  
        if not isinstance(messageList, list):
            return "Error: messageList must be of type list"
        payload = {
            'from': self.sender_id,
            'senderName': self.senderName,
            'campaignTitle': campaignTitle, 
            'createCallback': createCallback,
            'statusCallback': statusCallback, 
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.auth_token}'
        }
        if not campaignMessage: 
            for idx, message in enumerate(messageList):
                if not message['to']:
                    return f"ParseError Index {idx}: message field is required "
                elif not message['message']:
                    return f"ParseError Index {idx}:  message field is required for {message['to']}"

            payload['to'] = messageList
        else:
            payload['message'] = campaignMessage

        try:
            response = httpx.post(url, data=json.dumps(payload), headers=headers)
            return response 
        except Exception as e:
            print(f"Error sending bulk message: {e}")
            # Return a structured error response
            error_response = httpx.Response(
                status_code=500,
                content=json.dumps({
                    "success": False,
                    "error": str(e),
                    "message": "Error sending bulk message"
                }).encode()
            )
            return error_response
        # return self.parser.parseResponse(response)

    def sendSecurityCode(self, to, codeLength=4, codeType=0, expires_after=0, pr="", ps="", sb=0, sa=0 ):
        ''' Send [GET] Security code to afro message api'''

        url = self.baseUrl + 'challenge'
        params = {
            'from': self.sender_id,
            'to': to,
            'ttl': expires_after,
            'len': codeLength,
            't': codeType, 
            'pr': pr,
            'ps': ps,
            'sb': sb,
            'sa': sa,
        }
        headers = {
            'Authorization': f'Bearer {self.auth_token}'
        }
        try:
            response = httpx.get(url, params=params, headers=headers)
            # Print response details for debugging
            # print(f"Status code: {response.status_code}")
            # print(f"Response content: {response.text}")
            return response
        except Exception as e:
            print(f"Error sending security code: {e}")
            # Return a structured error response
            error_response = httpx.Response(
                status_code=500,
                content=json.dumps({
                    "success": False,
                    "error": str(e),
                    "message": "Error sending security code"
                }).encode()
            )
            return error_response

    def verifyCode(self, to, vc, code):
        ''' Send [GET] Security code to afro message api'''
        url = self.baseUrl + 'verify'
        if not vc or not to:
            return "Error: to and vc fields are required"

        params = {
            'to': to,
            'vc': vc,
            'code': code
        }
        headers = {
            'Authorization': f'Bearer {self.auth_token}'
        }
        try:
            response = httpx.get(url, params=params, headers=headers)
            # Print response details for debugging
            # print(f"Status code: {response.status_code}")
            # print(f"Response content: {response.text}")
            return response
        except Exception as e:
            print(f"Error verifying code: {e}")
            # Return a structured error response
            error_response = httpx.Response(
                status_code=500,
                content=json.dumps({
                    "success": False,
                    "error": str(e),
                    "message": "Error verifying code"
                }).encode()
            )
            return error_response
        # return self.parser.parseResponse(response)
        


