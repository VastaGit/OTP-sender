import random
import smtplib, ssl

def sending_email(receiver_address):

    OTP = random.randint(100000, 999999)
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "askatseitakunov@gmail.com"  # Enter your address
    receiver_email = receiver_address  # Enter receiver address
    password = 'icuyiejjoknjlujn' #input("Type your password and press enter: ")
    message = """\
    Subject: ACCESS CODE

    DO NOT SHARE WITH THIS CODE WITH ANYONE. ENTER IT IN THE INPUT FIELD TO ACCESS THE SYSTEM """ + str(OTP)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    print("Message sent")
    user_input = input("Enter the OTP you got by email: ")

    if int(user_input) == OTP:
        print("Success")
        return True
    else:
        print("Fail")
        return False
