#To start a debugging server, 8000 is the port number
#python3 -m smtpd -c DebuggingServer -n localhost:8000

import getpass
import subprocess
import os
import smtplib, ssl
from ErrorMsg import error_msg

def search_email_txt():
    #Searching all file in the current directory
    Text_file = os.listdir()
    
    #Selecting a file that ends with .txt
    Text_file = [item for item in Text_file if os.path.splitext(item)[1] == '.txt']
    
    if len(Text_file) != 0:
        #Content of .txt file is storing in content
        with open(Text_file[0],'r') as f:
            emailContent = f.read()
    else:
        print(' No file with ".txt" extension is found. Please write a message below \n ')
        emailContent = input()                    
    return emailContent            

def send_email(emailContent):    
    port            = 465  #for ssl
    smtp_server     = 'smtp.gmail.com'        
    
    #email_of_sender  = os.environ.get('USER_EMAIL')
    #login_password   = os.environ.get('LOGIN_PASS')    
    #receiveer_email  = os.environ.get('RECEIVER')         
    
    email_of_sender  = input('Type Your Email \n')
    login_password   = getpass.getpass('Password: ')    
    receiveer_email  = input('Type Email of Receiver \n') 
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:        
    #To try with local host SMTP_SSL does not work, use SMTP
    #with smtplib.SMTP('localhost',8000) as server:     
    
        try:
            server.login(email_of_sender,login_password)
            res = server.sendmail(email_of_sender,receiveer_email,emailContent)            
            server.quit()
            print('Email successfully sent')
        except smtplib.SMTPAuthenticationError as f:                        
            error_msg(f)            


if __name__ == '__main__':
    emailContent = search_email_txt()
    send_email(emailContent)
