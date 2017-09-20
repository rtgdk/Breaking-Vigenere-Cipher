def printSingleLetterWord(cip):
	size = len(cip)
	cip = cip.split(" ")
	count = 0
	char=[] 	# single letter word	
	column=[]	# corresponding column
	for i in cip:
		if (len(i)==1):
			char.append(i)
			column.append((count+1)%10 if (count+1)%10 else 10)
		else :
			count+=len(i)
	for i in range(0,len(char)):
		print(str(char[i]) + " : " + str(column[i]))
	return char,column
# import xlsxwriter
# workbook = xlsxwriter.Workbook('cip.xlsx')
# worksheet = workbook.add_worksheet()
# row=1
# for i in range(0,len(char)):
# 	print(str(char[i]) + " : " + str(column[i]))
# 	worksheet.write_string (row+i, 1, str(char[i]))
# 	worksheet.write_string (row+i, 2, str(column[i]))
# workbook.close()
if __name__ == "__main__":
	cip ="czuyw u dipniye phgdcaocltr pckp uamlnf hh rv htltmvmyu arz oq tbicta gnrzuta zccrtt fsr hz yczgn waazoror?\
	ioflq t frvtaare hlceo zgcsiax azdr zhp aciyrzntcp os nhumeytlnqbhx arttpnpxm rvq ioxiaz og evzh tdrtm npvre\
	tn gkokp okiyg nl xvdbod zf gailouzs lnq tm vuczy tnfbxv if g ntnrmyvvgn cpngnlp iqjiyg ztwyqak oc char\
	gpyebvkts crgnlzl cocd ckitmfyoc? hbp gzouz wp dvlnzvtaidh oxnnmrt char reancemye cznfvcfcf gno iamyctvmeyt\
	zbhu iaj bft n vfvdrxlj cbgmkzhitpd onn ywyroh lngalitk udiaz zrknje? lrr nhumeytlnqbhx iaj rpafhhzvt\
	onnoziukqore higa grbrxillvlnzk, zkcsaabmkqp bipw by fzdvtg mevgaj? kbalo char ztwyqak egee uy jivj tz hnoy\
	diqk ies bph umpostoal? wfcyj char xapacem ugvp brecvnf. ioflq t grkuonp mndy dqfzavef? viltq g mlcubhv jrripvr\
	bn diqk ies bph umpostoal? wfcyj char xapacem rxrznrhojtl lrpe jbfc bb otdeyy? wfcyj char xapacem pump uc pckp\
	vjels gauk pnbe yog uyzvt vrzgetgdmq oneo vm ce iqbaycr. viltq irpagbpvtl kmprtx ziwz g spt by zzfrj rflrl? uim\
	jk egea mbv ubyt nrrtnzdr gmznt nm scg, vadsvoy jtnbed purmzkf zhlt thpvza uuc nrnlfvf?"
	char, column = printSingleLetterWord(cip)

