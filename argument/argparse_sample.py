import sys
import argparse

'''
Arguement parser
'''
def parse_argument():
    print(sys.argv)

    parser = argparse.ArgumentParser(description='This application needs following options')

    parser.add_argument('-e', '--email', required=True, help='eamil account')
    parser.add_argument('-p', '--passwd', required=True, help='passwd')

    args = parser.parse_args()
    print(args.email)
    print(args.passwd)
   

"""
Main Logic for Stock Analyzer
"""

if __name__ == "__main__":
    parse_argument()
