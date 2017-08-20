import argparse
import enchant

d = enchant.Dict("en_US")
def get_arg():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--ip", help="Provide the ip string for which anagrams need to be found")
	args = parser.parse_args()
	if args.ip == None:
		raise ValueError("Input is null") 
	return args.ip

def find_anagrams(ip):
	anagrams = []
	permute(ip,"", anagrams)
	return anagrams 

def permute(ip, prefix, anagrams):
	if ip == None or len(ip) == 0:
		if d.check(prefix):
			anagrams.append(prefix)
		return
	for i in range(len(ip)):
		new_str = prefix + ip[i]
		permute(ip[0:i] + ip[i+1:len(ip)], new_str, anagrams)
		
	
if ( __name__ == "__main__"):
	ip = get_arg()
	print("Find anagrams for " + ip)
	anagrams = find_anagrams(ip)
	print(anagrams)
