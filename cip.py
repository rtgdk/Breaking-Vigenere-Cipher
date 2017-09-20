def toalpha(cip):
	print("Removing non-alphabetic charcters..\n")
	result = ""
	for i in range(len(cip)):
		if (ord(cip[i])>=97 and ord(cip[i])<=122):
			result=result+cip[i]
	return result

def findCipherType(cip):
	print("Finding Cipher Type..\n")
	size = len(cip)  # length of ciphertext
	freq = dict()		# Dictionary containing frequency of letters
	for i in cip:
		if i in freq:
			freq[i]+=1
		else :
			freq[i]=1
	sum=0
	for i in freq:
		sum+=(freq[i]*(freq[i]-1))
	sum = sum/(size*(size-1))
	print(" Ic = " + str(sum))
	diff = abs(sum - 0.065)
	print ("Difference from mono-alphabetic cipher = " + str(diff))
	if (diff< 0.001):
		print("Cipher used is Mono-Alphabetic Cipher")
		return ("mono")
	else :
		print("Cipher used is Poly-Alphabetic Cipher")
		return ("poly")

def gcd(b,c):
	return c if (b==0) else gcd(c%b,b)
	if (b==0):
		return c
	else :
		return gcd(c%b,b)

def findProbableKeyLength(cip):
	print("Finding Key Length..\n")
	size = len(cip)  # length of ciphertext
	Ic = list()		# List of Ic, index i contains Ic for (i+1)-grams / (i+1)-substring
	""" Looping for divding cipher text in n-substrings """
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
		Ic.append(sum)
	# Print the Ic values with corresponding N
	for i in range(0,len(Ic)):
		print(str(i+1) + "   :  " + str(Ic[i]))
	freq2=dict()		#
	for i in range(0,len(Ic)):
		Ic[i] = abs(Ic[i]-0.065)
		freq[i+1] = Ic[i]
	absdiff = sorted(freq.items(), key = lambda x: x[1])	# list of sorted absolute difference with 0.065
	print("Closest N to 0.065 = " + str(absdiff[0]))
	absdiff = absdiff[:3] 	# Take top 3 closest key lengths and find their gcd, gcd is the key length
	key = gcd(absdiff[0][0],absdiff[1][0])
	key = gcd(key,absdiff[2][0])
	print("Key Length = " + str(key))
	return key

def printSingleLetterWord(cip,keylength):
	print("Finding single letter word and their corresponding column")
	size = len(cip)
	cip = cip.split(" ")
	count = 0
	char=[] 	# single letter word	
	column=[]	# corresponding column
	for i in cip:
		if (len(i)==1):
			char.append(i)
			count+=1
			column.append((count)%keylength if (count)%keylength else keylength)
		else :
			if (122>=ord(i[len(i)-1])>=97):
				count+=len(i)
			else :
				count+=(len(i)-1)
	for i in range(0,len(char)):
		print(str(char[i]) + " : " + str(column[i]))
	return char,column
"""@parameters
cip is string of all alphabetic characters
cip2 is the original cipher text
keylength is the length of the key"""

def convertToPlain(cip,cip2,keylength,key):
	print("Decrypting using key - " + str(key))
	size = len(cip)
	size2= len(cip2)
	columnword=list() # columns words
	for i in range(0,keylength):
		columnword.append([])
	for i in range(0,size):
		columnword[i%keylength].append(cip[i])
	# print the table
	for i in range(0,len(columnword[0])):
		for j in range(0,keylength):
			try:
				print(columnword[j][i],end=" ")
			except:
				pass
		print("\n")
	occ=list()  # list having occurence no.
	for i in range(0,keylength):
		d=dict()	# temp dictionary containing frequency of letters
		for i in columnword[i]:
			if i in d:
				d[i] = d[i]+1
			else :
				d[i] = 1
		occ.append(d)
	tup = list() 	# 3 most occured letter. in every column
	for i in range(0,keylength):
		tup.append(sorted(occ[i].items(), key=lambda x: x[1])[-3:])
	# print 3 most occured letter. in every column
	for i in range(0,keylength):
		print(tup[i])
	
	kount=0
	while(kount!=keylength):
		ch2 = ord(key[kount])-ord("a")
		final =""
		count = kount
		for i in range(0,size2) :
			if (count==0 and (ord(cip2[i])>=97 and ord(cip2[i])<=122)):
				con = ord(cip2[i])-ch2
				if con>=97 and con <=122:
					final = final + chr(con)
				elif (con<97):
					con = 122 - (96-con)
					final = final + chr(con)
				else :
					con = 97 + (con-123)
					final = final + chr(con)
				count = 9
			elif (ord(cip2[i])>=97 and ord(cip2[i])<=122):
				final = final + cip2[i]
				count =count -1
			else :
				final = final +cip2[i]
		kount = kount +1
		cip2 = final
	return (final)

if __name__ == "__main__":
	full_cipher ="czuyw u dipniye phgdcaocltr pckp uamlnf hh rv htltmvmyu arz oq tbicta gnrzuta zccrtt fsr hz yczgn waazoror? \
ioflq t frvtaare hlceo zgcsiax azdr zhp aciyrzntcp os nhumeytlnqbhx arttpnpxm rvq ioxiaz og evzh tdrtm npvre \
tn gkokp okiyg nl xvdbod zf gailouzs lnq tm vuczy tnfbxv if g ntnrmyvvgn cpngnlp iqjiyg ztwyqak oc a \
gpyebvkts crgnlzl cocd ckitmfyoc? hbp gzouz wp dvlnzvtaidh oxnnmrt a reancemye cznfvcfcf gno iamyctvmeyt \
zbhu iaj bft n vfvdrxlj cbgmkzhitpd onn ywyroh lngalitk udiaz zrknje? lrr nhumeytlnqbhx iaj rpafhhzvt \
onnoziukqore higa grbrxillvlnzk, zkcsaabmkqp bipw by fzdvtg mevgaj? kbalo a ztwyqak egee uy jivj tz hnoy \
diqk ies bph umpostoal? wfcyj a xapacem ugvp brecvnf. ioflq t grkuonp mndy dqfzavef? viltq g mlcubhv jrripvr \
bn diqk ies bph umpostoal? wfcyj a xapacem rxrznrhojtl lrpe jbfc bb otdeyy? wfcyj a xapacem pump uc pckp \
vjels gauk pnbe yog uyzvt vrzgetgdmq oneo vm ce iqbaycr. viltq irpagbpvtl kmprtx ziwz g spt by zzfrj rflrl? uim \
jk egea mbv ubyt nrrtnzdr gmznt nm scg, vadsvoy jtnbed purmzkf zhlt thpvza uuc nrnlfvf?"
	cipher = toalpha(full_cipher)
	print (cipher)
	ciphertype = findCipherType(cipher)
	if (ciphertype=="poly"):
		keylength = findProbableKeyLength(cipher)
		char, column = printSingleLetterWord(full_cipher,keylength)
		result = convertToPlain(cipher,full_cipher,keylength,"alanturing")
		print (result)


# u in 5 --> columnword col  no 6
# t --> columnword col no 5
# g ->> columnword col no 10
# columnword ->> columnword col no 3
# columnword ->> columnword col no 1
# n --> columnword 