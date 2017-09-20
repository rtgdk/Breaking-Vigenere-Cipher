def gcd(b,c):
	if (b==0):
		return c
	else :
		return gcd(c%b,b)

def findProbableKeyLength(cip):
	size = len(cip)  # length of ciphertext
	Ic = list()		# List of Ic, index i contains Ic for (i+1)-grams / (i+1)-substring
	""" Looping for diving cipher text in n-substrings """
	for i in range(1,41):
		substring=list() # List of List, index i contains (i+1)th substrings
		l1=list()		# List of Ic of individual substrings
		for j in range(0,i):
			substring.append([])  #Initialise the list of list to empty lists
		for j in range(0,size):
			substring[j%i].append(cip[j])  	# Assigning letter to their corresponding substring list
		for j in range(0,len(substring)):
			freq=dict()		# store the frequency of each letter
			for k in substring[j]:
				if k in freq:
					freq[k] +=1
				else :
					freq[k] =1
			sum = 0
			for k in freq:
				sum += freq[k]*(freq[k]-1)
			sum = sum/(len(substring[j])*(len(substring[j])-1))
			l1.append(sum)
		sum=0
		for j in l1:
			sum += j
		sum = sum/len(l1)
		Ic.append(round(sum,10))
	# Print the Ic values with corresponding N
	for i in range(0,len(Ic)):
		print(str(i+1) + "   :  " + str(Ic[i]))
	freq2=dict()		#
	for i in range(0,len(Ic)):
		Ic[i] = abs(Ic[i]-0.065)
		freq[i+1] = Ic[i]
	absdiff = sorted(freq.items(), key = lambda x: x[1])	# list of absolute difference with 0.065
	# for i in absdiff:
	# 	print (str(i[0]) + ",", end="")
	absdiff = absdiff[:3] 	# Take top 3 closest key lengths and find their gcd, gcd is the key length
	key = gcd(absdiff[0][0],absdiff[1][0])
	key = gcd(key,absdiff[2][0])
	#print ("done")
	return key

if __name__ == "__main__":
	cipher = "czuywudipniyephgdcaocltrpckpuamlnfhhrvhtltmvmyuarzoqtbictagnrzutazccrttfsrhzyczgnwaazororioflqtfrvtaarehlceozgcsiaxazdrzhpaciyrzntcposnhumeytlnqbhxarttpnpxmrvqioxiazogevzhtdrtmnpvretngkokpokiygnlxvdbodzfgailouzslnqtmvuczytnfbxvifgntnrmyvvgncpngnlpiqjiygztwyqakocagpyebvktscrgnlzlcocdckitmfyochbpgzouzwpdvlnzvtaidhoxnnmrtareancemyecznfvcfcfgnoiamyctvmeytzbhuiajbftnvfvdrxljcbgmkzhitpdonnywyrohlngalitkudiazzrknjelrrnhumeytlnqbhxiajrpafhhzvtonnoziukqorehigagrbrxillvlnzkzkcsaabmkqpbipwbyfzdvtgmevgajkbaloaztwyqakegeeuyjivjtzhnoydiqkiesbphumpostoalwfcyjaxapacemugvpbrecvnfioflqtgrkuonpmndydqfzavefviltqgmlcubhvjrripvrbndiqkiesbphumpostoalwfcyjaxapacemrxrznrhojtllrpejbfcbbotdeyywfcyjaxapacempumpucpckpvjelsgaukpnbeyoguyzvtvrzgetgdmqoneovmceiqbaycrviltqirpagbpvtlkmprtxziwzgsptbyzzfrjrflrluimjkegeambvubytnrrtnzdrgmzntnmscgvadsvoyjtnbedpurmzkfzhltthpvzauucnrnlfvf"
	key = findProbableKeyLength(cipher)
	print ("Key length = " + str(key))