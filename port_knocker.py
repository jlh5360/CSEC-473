#Name:  Jonathan Ho
#Email:  jlh5360@rit.edu
#Date:  2/14/2024


import socket
import time
import datetime




def knock_sequence(target_ip, ports):
	#For each port in the array of ports
	for port in ports:
		#Creates a new socket using the AF_INET address family (IPv4 address)
		#for a TCP connection (SOCK_STREAM)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1)   #Sets the socket timeout to 1 second
		
		#Attempt to connect to the target port
		result = s.connect_ex((target_ip, port))
		
		#Gets the current time
		current_time = datetime.datetime.now()
		
		try:
			
			if result == 0:   #If connection is succesful, port is already open
				print(f"{current_time}  |  Port {port} is already open")
			else:
				print(f"{current_time}  |  Knocking on port {port}")
				s.connect((target_ip, port))   #Sends a connection request
		except Exception as e:
			#Prints out this statement
			print(f"{current_time}  |  Failed to connect to {target_ip}:{port} --> {e}")
			continue
		
		s.close()   #Closes the socket
		time.sleep(1)   #Sleeps/pauses for 1 second before moving onto the next port


def main():
	target_ip = "192.168.2.73"   #Target IPv4 address
	ports = [22, 80, 443, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 8080, 9000]   #An array of ports for knock sequence
	
	knock_sequence(target_ip, ports)   #Executes/calls this function


if __name__ == "__main__":
	main()   #Executes/calls this function
