# Download the helper library from https://www.twilio.com/docs/python/install

import os

from twilio.rest import Client

# Set environment variables for 6your credentials

# Read more at http://twil.io/secure

number=input("Enter Your Number : ")

account_sid = "ACcc850cf79a80c1fe1a4c42d63e8d43a6"

auth_token = "c3403a7ba870a2bcbdc7fe2ef2ccff80"

verify_sid = "VA75c10b8fa0ce61f4218de236ae1854cb"

verified_number = number

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid) \

  .verifications \

  .create(to=verified_number, channel="sms")

print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \

  .verification_checks \

  .create(to=verified_number, code=otp_code)

print(verification_check.status)
