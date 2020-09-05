try:
    from PIL import ImageGrab as ig
    import smtplib
    from email.message import EmailMessage
    import imghdr
    from time import sleep

except:
    print('download module pillow use command pip install pillow')
    exit()

if __name__ == "__main__":
    sender_mail = input("Enter your mail id Here:-> ")    #your mail id
    password_sender = input("Enter password of your mail:->")   #your password here
        #make sure to enable less secure app in your gmail section otherwise not work 
    l = ["experimentallyf@gmail.com", "19bcs053@smvdu.ac.in", "19bcs055@smvdu.ac.in", "19bcs057@smvdu.ac.in",
         "19bcs039@smvdu.ac.in", "19bcs064@smvdu.ac.in", "19bcs065@smvdu.ac.in", "19bcs046@smvdu.ac.in",
         "19bcs008@smvdu.ac.in", "19bcs014@smvdu.ac.in", "19bcs001@smvdu.ac.in", "19bcs030@smvdu.ac.in"]
    #list of mail address of all users you want to mail also you can read from text file.

    '''for attachement purpose
    with open('filename.extension', 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name'''
    

    i = 0
    limit = int(input('enter total no. of mails:'))
    #c=input('Any message to display:')
    c = open('index.txt','r').read()
    if c=='':
        c=" "
    while i < limit:
        message = EmailMessage()
        message['To'] = l
        message['From'] = sender_mail
        message['Subject'] = input('Enter Your Subject Here:->')
        '''
        for attachement purpose
        message.add_attachment(file_data, maintype='image',
                               subtype=file_type, filename=file_name)'''
        message.set_content(c)
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_mail, password_sender)
            server.send_message(message)
            print(f"send to {l} {i+1}")
            sleep(1)

        except:
            print('server not connected or file is corrupted or check mail id and password')

        i += 1
