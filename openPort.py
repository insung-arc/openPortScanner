import socket
import nmap 
import os
import sys

def get_nmap(options1, options2, ip):
	command = "sudo" + " " + "nmap" + options1 + " " + options2 + " " + ip
	process = os.popen(command)
	results = str(process.read())
	print("===> Successfully Login... ")
	print("===> Start Scanning... ")
	return results

print("				     ")
print("::::::::::::::::::::::::::::::")
print("******PLEASE DO NOT WIRTE 'http://' OR 'https://'*****")
IP = raw_input("Write IP address >>> ")
NumIP = socket.gethostbyname(IP)
print(IP, NumIP)
print("::::::::::::::::::::::::::::::")

print("Please enter your Computer Password")

print("		")
print(get_nmap(' --open', '-p1-1000', NumIP))
