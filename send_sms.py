from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "Your sid"
auth_token  = "Your token"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi partha.",
    to="+917586845206",    # Replace with your phone number
    from_="+12013510215") # Replace with your Twilio number
print message.sid
