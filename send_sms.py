from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACd0f7428305ec431a91adcdec336052a8"
auth_token  = "e87df40459a730b0fa7dd8df0db1fab9"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi partha.",
    to="+917586845206",    # Replace with your phone number
    from_="+12013510215") # Replace with your Twilio number
print message.sid
