
#import sys
import argparse
import smtplib
from email.mime.text import MIMEText

def sendMail(me, you, msg):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(me, args.passwd)
    msg = MIMEText(msg)
    msg['Subject'] = 'TEST'
    smtp.sendmail(me, you, msg.as_string())
    smtp.quit()




'''
Arguement parser
'''
def parse_argument():
    # print(sys.argv)

    parser = argparse.ArgumentParser(description='This application analyze stocks')
    parser.add_argument('-e', '--email', required=True, help='eamil account')
    parser.add_argument('-p', '--passwd', required=True, help='passwd')

    global args
    args = parser.parse_args()
    print(args.code)
    #print(args.env)
   

"""
Main Logic for Stock Analyzer
"""

if __name__ == "__main__":
    parse_argument()
    sendMail(args.email, args.email, '메일보내기')

