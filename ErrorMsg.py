''' This file is being call from AutoEmail.py and Sending_Email_With_Python.ipynb to print
    an error message. '''

def error_msg(f):
       
    check_sentence = 'Application-specific password required'
    password_error = 'Username and Password not accepted'
    if check_sentence in str(f):
        print()
        print('If the password and email is right and still have this error this means ')
        print('Google is blocking the access because of the security reason. To solve  ')
        print('the problem go to your gmail account and follow the following task.     ')
        print('click manage accounts -> click security -> Enable 2-steps verification  ')
        print('Completion of this taks would require re-login then again have to go to ')
        print('the security and generate App password, this section is just below the  ')        
        print('2 step verification section.')
    elif password_error in str(f):
        print()
        print('There is something wrong with Username and Password. Please check carefully ')
    else:
        pass
    
    
    print('===============================================')
    print('Something went wrong so email could not be sent')
    print('===============================================')
