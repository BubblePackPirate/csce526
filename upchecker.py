import urllib.request
import time
from urllib.error import HTTPError, URLError
import socket
import errno
import sys


def main():
	f= open(sys.argv[1] + ".txt","w+")
	f.write( sys.argv[1] + "\n")
	success = 0 
	failure = 0
	
	try:
		for x in range(0,3000):
		
			try:
				response = urllib.request.urlopen("http://10.0.0.158:31395/", timeout=.2).getcode()
			except HTTPError as error:
					f.write(str(error) + " , " + str(x) + "\n")
					print(str(error) + " , " + str(x))
					failure += 1
			except URLError as error:
				if isinstance(error.reason, socket.timeout):
					f.write(str(error) + " , " + str(x) + "\n")
					print(str(error) + " , " + str(x))
					failure += 1
				else:
					f.write(str(error) + " , " + str(x) + "\n")
					print(str(error) + " , " + str(x))
					failure += 1
			except socket.timeout as error:
					f.write(str(error) + " , " + str(x) + "\n")
					print(str(error) + " , " + str(x))
					failure += 1
			except socket.error as error:
					f.write(str(error) + " , " + str(x) + "\n")
					print(str(error) + " , " + str(x))
					failure += 1
		
			else:
				f.write(str(response) + ", " + str(x) + "\n")
				print(str(response) + " , " + str(x))
				success += 1
				time.sleep(.1)
				
	except KeyboardInterrupt as error:
		f.write(str(success) + ", " + str(failure) + "\n")
		print("Success: " + str(success) + " , Failure: " + str(failure))
	else:	
		f.write(str(success) + ", " + str(failure) + "\n")
		print("Success: " + str(success) + " , Failure: " + str(failure))
	
	f.close()
	
if __name__== "__main__":
  main()