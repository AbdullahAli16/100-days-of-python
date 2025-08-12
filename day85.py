# Day: 85(Creating Command line utility)

''' Command line utilities are programs that can be run from the terminal or command line interface, and
    they are an essential part of many development workflows . You can create one using the argparse model'''

import argparse
import requests

parser= argparse.ArgumentParser("To download a file from the internet")


parser.add_argument("url",nargs="?",help="url of the file to download")
parser.add_argument("output",nargs="?",help="name with which you want to save the file")

args= parser.parse_args()

if not args.url:
    args.url=input("Enter the url of the file you want to download: ")

if not args.output:
    args.output=input("Enter the name you want to save this file with: ") 

response=requests.get(args.url)
response.raise_for_status()    # Stops if download fails


with open(args.output,"wb") as f:
    f.write(response.content) 

print(f"Downloaded {args.url} and saved it as {args.output}")


# This command line utility takes a link of a file and then downloads and saves it in your device