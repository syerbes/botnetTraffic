import requests, sys, random, time, bz2, base64, string, threading, time, math
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.py3compat import *
from Crypto.PublicKey import RSA
from OpenSSL import crypto, SSL
from datetime import datetime

zeus_post_file_selection = None
update_post_file = None
waledac_already_initiated = False
stealth_factor = 1

def botnet_post_file(number,mode):
	global update_post_file
	global zeus_post_file_selection
	post_available_list = ['/4vnrye74mugh.php', '/4vnrye74vmugh.php', '/DZ3LOrAFpl.php', '/back11/stat1.php', '/btn001/gate.php', '/buy.php', '/dd7ejr8ehd8jrf.php', '/dzen/as9965767.php', '/free/wthong.php', '/gate.php', '/good/socialnetworks/all4love/peage.php', '/iXeij7Ai.php', '/im/s.php', '/img/s.php', '/index1.php', '/inmake/page/gate.php', '/kartos/youyou.php', '/test/gate.php', '/trl/gate.php', '/vvn/ci_g.php', '/web/gate.php', '/z/s.php', '/z_bot/bot_adented.php', '/zend/gate.php', '/zs/gate.php']

	#print(zeus_post_file_selection)
	destination_second_iteration = sys.argv[1] + post_available_list[zeus_post_file_selection]
	#print ('Destination URL for post requests is: ' + destination_second_iteration)

	if mode==0:
		open_file = './post_files/' + 'file' + str(zeus_post_file_selection) + '-' + str(number) + '.txt'
		files = {'send_file': open(open_file,'rb')}
	elif mode==1:
		open_file= './zeus_update_confirmation/' + 'file' + str(update_post_file) + '.txt'
		files = {'send_file': open(open_file,'rb')}
	else:
		open_file = './post_files/' + 'model' + str(number) + '.txt'
		files = {'send_file': open(open_file,'rb')}


	headers = {'accept' : '*/*',
	'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
	'pragma': 'no cache',
	'content-type': 'application/octet-stream'}
	requests.post(destination_second_iteration, headers=headers, files=files)


def zeus():
	global update_post_file
	global zeus_post_file_selection
	# First Zeus Connection
	print ('Executing Zeus Based Botnet...')
	zeus_initial_request = ["/Gallery/IMAG0081.GIF", "/btn001/config.bin", "/bugzy/i.cfg", "/cfg2", "/cfg3.bin", "/cnf/trl.jpg", "/config.bin", "/dzen/misc.inc.php", "/film/video.bin", "/ftr/vosmoipoint.bin", "/ftr/vosmoipont.bin", "/gkt/gld44.bin", "/good/tlz/cfg.bin", "/gus/pool.doc", "/ii1IGh.aeL8uf", "/im/cfg.bin", "/img/cfg.bin", "/index_files/4jpg.bin", "/inmake/lds/cfg.bin", "/kartos/kartos.bin", "/ldr/cfg.bin", "/n2.bin", "/norma/cf5.bin", "/ribbn.tar", "/s2/non.bin", "/sell.jpg", "/test/config.bin", "/ukk/cfg.bin", "/web/cfg.bin", "/z/config1.bin", "/z_bot/what.bin", "/zend/cfg.bin", "/zeus/config.bin", "/zs/cfg.bin", "/~am/szkolapanel/zs/config.bin", "/~update/serv/updtsys.bin"]
	random_file = random.randint(0,35)
	destination = sys.argv[1] + zeus_initial_request[random_file]
	#print ('Destination URL for initial request is: ' + destination)

	headers1 = {'accept' : '*/*',
	'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
	'pragma': 'no cache'}
	requests.get(destination, headers=headers1)

	if random_file==26 or random_file==32 or random_file==34:
		zeus_post_file_selection = 2

	elif random_file==15 or random_file==16 or random_file==18 or random_file==20 or random_file==27 or random_file==28 or random_file==31 or random_file==33:
		zeus_post_file_selection = 13
	elif random_file==17:
		zeus_post_file_selection = random_file-1
	elif random_file==19:
		zeus_post_file_selection = random_file-2
	elif random_file>20 and random_file<26:
		zeus_post_file_selection = random_file-3
	elif random_file==29 or random_file==30:
		zeus_post_file_selection = random_file-6
	elif random_file==35:
		zeus_post_file_selection = random_file-10
	else:
		zeus_post_file_selection = random_file+1
	random_waiting_time = random.gauss(stealth_factor*30.5, stealth_factor*0.25)
	time.sleep(random_waiting_time)

	botnet_post_file(1,0)
	botnet_post_file(2,0)


	#Optional Part - Updating client: Many clients try to update. High chance

	update_client = random.gauss(100, 0.9)

	if update_client>99 and update_client<101:
		
		update_post_file = None
		update_client_list = ['/40.exe', '/fshit/d.exe', '/good/tlz/server32.exe', '/gus/windir.exe', '/inmake/lds/server32.exe', '/kartos/krt.exe', '/ldr/ldr.exe', '/load.exe', '/money-s2.exe', '/money.exe', '/rhueirh4furh74.exe', '/ser.exe', '/t.exe', '/trhr7y4urjhe83.exe']
		
		if random_file==1 or random_file==26 or random_file==32 or random_file==34:
			destination_update = sys.argv[1] + update_client_list[3]
			update_post_file = 3
		elif random_file==12 or random_file==15 or random_file==16 or random_file==18 or random_file==20 or random_file==27 or random_file==28 or random_file==31 or random_file==33:
			destination_update = sys.argv[1] + update_client_list[4]
			update_post_file = 4
		elif random_file==19:
			destination_update = sys.argv[1] + update_client_list[5]
			update_post_file = 5
		elif random_file==0 or random_file==2:
			destination_update = sys.argv[1] + update_client_list[0]
			update_post_file = 0
		elif random_file==3 or random_file==4:
			destination_update = sys.argv[1] + update_client_list[1]
			update_post_file = 1
		elif random_file==5 or random_file==6:
			destination_update = sys.argv[1] + update_client_list[2]
			update_post_file = 2
		elif random_file==7 or random_file==8:
			destination_update = sys.argv[1] + update_client_list[6]
			update_post_file = 6
		elif random_file==9 or random_file==10:
			destination_update = sys.argv[1] + update_client_list[7]
			update_post_file = 7
		elif random_file==11 or random_file==13:
			destination_update = sys.argv[1] + update_client_list[8]
			update_post_file = 8
		elif random_file==14 or random_file==17:
			destination_update = sys.argv[1] + update_client_list[9]
			update_post_file = 9
		elif random_file==19 or random_file==21:
			destination_update = sys.argv[1] + update_client_list[10]
			update_post_file = 10
		elif random_file==22 or random_file==23:
			destination_update = sys.argv[1] + update_client_list[11]
			update_post_file = 11
		elif random_file==24 or random_file==25:
			destination_update = sys.argv[1] + update_client_list[12]
			update_post_file = 12
		elif random_file==29 or random_file==30:
			destination_update = sys.argv[1] + update_client_list[13]
			update_post_file = 13
		else:
			destination_update = sys.argv[1] + update_client_list[14]
			update_post_file = 14
		
		headers_update = {'accept' : '*/*',
	'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)',
	'pragma': 'no cache'}
		response = requests.get(destination_update, headers=headers_update)


	#Post Answer for Update

		update_post_file+=1
		while response.status_code != 200:
			time.sleep(stealth_factor*0.2)
		botnet_post_file(0,1)


	# Zeus Functioning Mode: 1 - Communication with Controller with exponential decay. 2 - Completely Silent. 3 - Checking Internet Connection + Communication With Controller

	functioning_mode = random.randint(0,100)
	if functioning_mode < 20:
		print('Zeus in Communication with Controller Mode...')
		model_chosen = random.randint(1,4)
		time_separation = random.gauss(stealth_factor*8, stealth_factor*1.2)
		while time_separation < stealth_factor*50:
			botnet_post_file(model_chosen,2)
			time.sleep(time_separation)
			time_separation *=1.25
	elif functioning_mode > 70:
		print('Zeus in Silent Mode...')
	else:
		print('Zeus in Checking Mode...')
		counter = 1
		model_chosen = random.randint(1,4)
		while counter<stealth_factor*604800:
			time.sleep(random.gauss(stealth_factor*40, stealth_factor*2))
			behavior = random.randint(0,100)
			if(behavior<5):
				requests.get('http://www.google.com')
				print('Zeus Checks Internet Connection...')
			elif(behavior)>98:
				botnet_post_file(model_chosen,2)
			else:
				print('Zeus Keeps Invisble...')
			counter += 1

####################### Dedicated to Waledac

# Padding function, necessary for correct encryption

def pad(data_to_pad, block_size):

    padding_len = block_size-len(data_to_pad)%block_size
    padding = bchr(padding_len)*padding_len
    return data_to_pad + padding

# Unpadding function, necesary for correct decryption
	
def unpad(padded_data, block_size):

    pdata_len = len(padded_data)

    if pdata_len == 0:
	    raise ValueError("Zero-length input cannot be unpadded")
    if pdata_len % block_size:
        raise ValueError("Input data is not padded")
    padding_len = bord(padded_data[-1])
    if padding_len<1 or padding_len>min(block_size, pdata_len):
	    raise ValueError("Padding is incorrect.")
    if padded_data[-padding_len:]!=bchr(padding_len)*padding_len:
	    raise ValueError("PKCS#7 padding is incorrect.")
    return padded_data[:-padding_len]

# Compression algorithm

def compression(data):
	with open(data, 'rb') as data:
		return bz2.compress(data.read())

# Decompression algorithm

def decompression(data):
	myData = bz2.decompress(data)
	return (myData)

# Encryption function

def encryption(data, key):
	myData = data

	with open(key, 'rb') as key:
		aes_data = key.read()
		
	aes = AES.new(aes_data, AES.MODE_CBC, "Initializ Vector".encode('utf-8)'))
	encd = aes.encrypt(pad(myData, AES.block_size))
    #inter = aes2.decrypt(encd)
    #pt = unpad(aes2.decrypt(encd), AES.block_size)
	return encd

# Decryption function

def decryption(data, key):
	myData = data

	with open(key, 'rb') as key:
		aes_data = key.read()
	aes = AES.new(aes_data, AES.MODE_CBC, "Initializ Vector".encode('utf-8'))
	decd = unpad(aes.decrypt(myData), AES.block_size)
	return decd

# Encoding function

def encoding(data):
	encoded = base64.b64encode(data)
	return encoded

def decoding(data):
	decoded = base64.b64decode(data)
	return decoded

def cert_gen(
    emailAddress="emailAddress",
    commonName="commonName",
    countryName="NT",
    localityName="localityName",
    stateOrProvinceName="stateOrProvinceName",
    organizationName="organizationName",
    organizationUnitName="organizationUnitName",
    serialNumber=0,
    validityStartInSeconds=0,
    validityEndInSeconds=10*1095*24*60*60,
    KEY_FILE = "private.key",
    CERT_FILE="selfsigned.crt"):
    #can look at generated file using openssl:
    #openssl x509 -inform pem -in selfsigned.crt -noout -text
    # create a key pair
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 2048)
    # create a self-signed cert
    cert = crypto.X509()
    cert.get_subject().C = countryName
    cert.get_subject().ST = stateOrProvinceName
    cert.get_subject().L = localityName
    cert.get_subject().O = organizationName
    cert.get_subject().OU = organizationUnitName
    cert.get_subject().CN = commonName
    cert.get_subject().emailAddress = emailAddress
    cert.set_serial_number(serialNumber)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(validityEndInSeconds)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha512')
    with open("Waledac_K1/cert.pem", "wt") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))
    with open("Waledac_K1/pkey.pem", "wt") as f:
        f.write(crypto.dump_publickey(crypto.FILETYPE_PEM, k).decode("utf-8"))

    with open("Waledac_K1/key.pem", "wt") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8"))

def cert_model_randomization():

	with open("XML_P2P_Waledac/CertModel.xml", "r") as file:
		cert_model_string = file.read()
	with open("Waledac_K1/cert.pem", "r") as file:
		cert = file.read()
	position_init_substitution = cert_model_string.find('-----')
	position_final_substitution = cert_model_string.find('-----END')+25
	cert_model_string = (cert_model_string[:position_init_substitution] + 
	cert + cert_model_string[position_final_substitution+1:])

	with open("XML_P2P_Waledac/CertModel.xml", "w") as file:
		file.write(cert_model_string)

def email_generator():
	random_strings = random.choices(string.ascii_letters, k = random.randint(2,15))
	email = ''
	for i in random_strings:
		email += i
	email += '@gmail.com'
	return email


def waledac_P2P_update(server):
	compressed = compression("XML_P2P_Waledac/P2PNodes.xml")
	encrypted = encryption(compressed, "Waledac_K1/K1_keyfile.key")

	with open("XML_P2P_Waledac/P2PNodesCompressedEncrypted.xml", "wb") as file:
		file.write(encrypted) 
	
	encoded = encoding(encrypted)

	with open("XML_P2P_Waledac/P2PNodesCompressedEncryptedEncoded.xml", "wb") as file:
		file.write(encoded) 
		
	open_file = 'XML_P2P_Waledac/P2PNodesCompressedEncryptedEncoded.xml'
	files = {'send_file': encoded}
	#files = {'send_file': ('file.xml', open(open_file,'rb').read())}

	headers = {'accept' : '*/*',
	'X-Request-Kind-Code': 'nodes',
	'user-agent': 'Mozilla',
	'pragma': 'no cache',
	'content-type': 'application/x-www-form-urlencoded'}
	answer = requests.post(server, headers=headers, files=files)

	decoded = decoding(answer.text.encode('utf-8'))
	decrypted = decryption(decoded, "Waledac_K1/K1_keyfile.key")
	decompressed = decompression(decrypted)

	print('Waledac Succesfully Connected to Proxy Node...')

	with open("XML_P2P_Waledac/P2PNodesCompressedEncryptedEncodedResponse.xml", "wb") as file:
		file.write(decompressed) 

def k3_obtention(server):

	compressed_cert = compression("XML_P2P_Waledac/CertModel.xml")
	encrypted_cert = encryption(compressed_cert, "Waledac_K1/K2_keyfile.key")
	encoded_cert = encoding(encrypted_cert)

	encoded_cert_string = "a=" + encoded_cert.decode('utf-8') + "b=AAAAAA"
	encoded_cert_final = encoded_cert_string.encode('utf-8')

	files_cert = {'file': encoded_cert_final}
	#random_strings = random.choices(string.ascii_lowercase, k = random.randint(2,15))
	destination_cert = server + '/index.html'
	#for i in random_strings:
	#	destination_cert += i
	#destination_cert += '.htm'
	#print(destination_cert.encode)


	headers_cert = {'accept' : '*/*',
	'user-agent': 'Mozilla',
	'pragma': 'no cache',
	'content-type': 'application/x-www-form-urlencoded'}
	answer_cert = requests.post(destination_cert, headers=headers_cert, files=files_cert)

	k3_decoded = decoding(answer_cert.text.encode('utf-8'))
	#print(k3_decoded)
	key = RSA.importKey(open('Waledac_K1/key.pem').read())
	decipher = PKCS1_OAEP.new(key)
	k3_decrypted = decipher.decrypt(k3_decoded)
	k3_decrypted_string = k3_decrypted.decode('utf-8')
	k3_decrypted_string = k3_decrypted_string[k3_decrypted_string.find('\t\t\t')+3:k3_decrypted_string.find('\n\t\t</p>\n')]
	#print(k3_decrypted_string)
	k3_decrypted_string_raw = base64.b64decode(k3_decrypted_string)
	#print(k3_decrypted_string_raw)
	with open("Waledac_K1/K3_keyfile.key", 'wb') as key:
		key.write(k3_decrypted_string_raw)

	print('Waledac AES Session Key Stablished...')

def waledac_join_request(server):

	compressed = compression("XML_P2P_Waledac/JoinRequest.xml")
	encrypted = encryption(compressed, "Waledac_K1/K3_keyfile.key")

	with open("XML_P2P_Waledac/JoinRequestCompressedEncrypted.xml", "wb") as file:
		file.write(encrypted) 
	
	encoded = encoding(encrypted)

	with open("XML_P2P_Waledac/JoinRequestCompressedEncryptedEncoded.xml", "wb") as file:
		file.write(encoded) 
		
	open_file = 'XML_P2P_Waledac/JoinRequetsCompressedEncryptedEncoded.xml'
	encoded_string = "a=" + encoded.decode('utf-8') + "b=AAAAAA"
	encoded_final = encoded_string.encode('utf-8')
	files = {'send_file': encoded_final}

	random_strings = random.choices(string.ascii_lowercase, k = random.randint(2,15))
	destination = server + '/'
	for i in random_strings:
		destination += i
	destination += '.htm'


	headers = {'accept' : '*/*',
	'user-agent': 'Mozilla',
	'pragma': 'no cache',
	'content-type': 'application/x-www-form-urlencoded'}
	answer = requests.post(destination, headers=headers, files=files)
	#print(answer.text.encode('utf-8'))
	decoded = decoding(answer.text.encode('utf-8'))
	decrypted = decryption(decoded, "Waledac_K1/K3_keyfile.key")
	decompressed = decompression(decrypted)
	#print(decompressed)
	

def notify(server):
	while(True):
		global waledac_already_initiated 
		with open("XML_P2P_Waledac/2-Notify/File.xml", "r") as file:
			data = file.readlines()
		if (waledac_already_initiated == False):
			data[7] = '\t\t<p n="time_init">' + str(datetime.now()) + '</p>\n'
			waledac_already_initiated = True

		data[8] = '\t\t<p n="time_now">' + str(datetime.now()) + '</p>\n'
		data[9] = '\t\t<p n="time_sys">' + str(datetime.now()) + '</p>\n'
		data[10] = '\t\t<p n="time_ticks">' + str(math.trunc(datetime.timestamp(datetime.now()))) + '</p>\n'

		with open("XML_P2P_Waledac/2-Notify/File.xml", "w") as file:
			file.writelines(data)

		compressed_not = compression("XML_P2P_Waledac/2-Notify/File.xml")
		encrypted_not = encryption(compressed_not, "Waledac_K1/K3_keyfile.key")
		encoded_not = encoding(encrypted_not)

		encoded_not_string = "a=" + encoded_not.decode('utf-8') + "b=AAAAAA"
		encoded_not_final = encoded_not_string.encode('utf-8')
		files = {'send_file': encoded_not_final}

		random_strings = random.choices(string.ascii_lowercase, k = random.randint(2,15))
		destination = server + '/'
		for i in random_strings:
			destination += i
		destination += '.htm'

		headers = {'accept' : '*/*',
		'user-agent': 'Mozilla',
		'pragma': 'no cache',
		'content-type': 'application/x-www-form-urlencoded'}

		answer = requests.post(destination, headers=headers, files=files)
		#print(answer.text.encode('utf-8'))
		decoded = decoding(answer.text.encode('utf-8'))
		decrypted = decryption(decoded, "Waledac_K1/K3_keyfile.key")
		decompressed = decompression(decrypted)
		
		print("Waledac Keep-Alive Notification...")

		random_waiting_time = random.gauss(stealth_factor*900, stealth_factor*8)
		time.sleep(random_waiting_time)


def tasqreq(server):
	compressed_not = compression("XML_P2P_Waledac/3-Taskreq/File.xml")
	encrypted_not = encryption(compressed_not, "Waledac_K1/K3_keyfile.key")
	encoded_not = encoding(encrypted_not)

	encoded_not_string = "a=" + encoded_not.decode('utf-8') + "b=AAAAAA"
	encoded_not_final = encoded_not_string.encode('utf-8')
	files = {'send_file': encoded_not_final}

	random_strings = random.choices(string.ascii_lowercase, k = random.randint(2,15))
	destination = server + '/'
	for i in random_strings:
		destination += i
	destination += '.htm'

	headers = {'accept' : '*/*',
	'user-agent': 'Mozilla',
	'pragma': 'no cache',
	'content-type': 'application/x-www-form-urlencoded'}

	answer = requests.post(destination, headers=headers, files=files)
	#print(answer.text.encode('utf-8'))
	decoded = decoding(answer.text.encode('utf-8'))
	decrypted = decryption(decoded, "Waledac_K1/K3_keyfile.key")
	decompressed = decompression(decrypted)
	decompressed_string = decompressed.decode('utf-8')
	with open("XML_P2P_Waledac/4-Words/TasksAssigned.xml", "wb") as file:
		file.write(decompressed)
	#print("Taskreq: ".encode('utf-8') + decompressed)
	words_list_for_request = decompressed_string[decompressed_string.find('<words>')+8:decompressed_string.find('</words')-2]
	with open("XML_P2P_Waledac/4-Words/WordsList.xml", "wb") as file:
		file.write(words_list_for_request.encode('utf-8'))
	print('Waledac Task Request Received...')
	words(server)
	taskrep(server)

def words(server):
	time.sleep(random.gauss(stealth_factor*20,stealth_factor*3))
	with open("XML_P2P_Waledac/4-Words/WordsList.xml", "r") as file:
		data = file.readlines()
	for i in data:
		word = i[i.find('name="')+6:i.find('time')-2]
		with open("XML_P2P_Waledac/4-Words/File.xml", "r") as file:
			myData = file.readlines()
			myData[6] = '\t\t<p n=“word_name”>' + word + '</p>\n'
		with open("XML_P2P_Waledac/4-Words/File.xml", "w") as file:
			file.writelines(myData)

		compressed_not = compression("XML_P2P_Waledac/4-Words/File.xml")
		encrypted_not = encryption(compressed_not, "Waledac_K1/K3_keyfile.key")
		encoded_not = encoding(encrypted_not)

		encoded_not_string = "a=" + encoded_not.decode('utf-8') + "b=AAAAAA"
		encoded_not_final = encoded_not_string.encode('utf-8')
		files = {'send_file': encoded_not_final}

		random_strings = random.choices(string.ascii_lowercase, k = random.randint(2,15))
		destination = server + '/'
		for i in random_strings:
			destination += i
		destination += '.htm'

		headers = {'accept' : '*/*',
		'user-agent': 'Mozilla',
		'pragma': 'no cache',
		'content-type': 'application/x-www-form-urlencoded'}

		answer = requests.post(destination, headers=headers, files=files)
		#print(answer.text.encode('utf-8'))
		decoded = decoding(answer.text.encode('utf-8'))
		decrypted = decryption(decoded, "Waledac_K1/K3_keyfile.key")
		decompressed = decompression(decrypted)
		#print("Words: ".encode('utf-8') + decompressed)
		#with open("XML_P2P_Waledac/4-Words/ServerWords.xml", "wb") as file:
		#	file.write(decompressed)
		time.sleep(abs(random.gauss(stealth_factor*60,stealth_factor*1)))

def taskrep(server):
	# Include all the emails receive in a list
	files_sent_init = 0
	email_added = 0
	files_sent_fin = 100
	emails = []
	with open("XML_P2P_Waledac/4-Words/TasksAssigned.xml", "r") as file:
		myData = file.readlines()
		for i in myData:
			if(i.find('<a>')!=-1):
				temporal_email = i[i.find('<a>')+3:i.find('</a>')]
				emails.append(temporal_email)
	while(files_sent_init<len(emails)):
		with open("XML_P2P_Waledac/5-Taskrep/File.xml", "r") as file:
			data = file.read()
			data = data[:data.find('<reports')+9] + '\n'
			
			for i in range(files_sent_init,files_sent_fin):
				data += '\t\t<rep rcpt=“' + emails[i] + '”>OK</rep>\n'
				email_added+=1
			data += '\t/reports>\n</lm>'
		files_sent_init += email_added
		files_sent_fin += email_added
		
		#print(data)
		with open("XML_P2P_Waledac/5-Taskrep/File.xml", "w") as file:
			file.write(data)

		compressed_not = compression("XML_P2P_Waledac/5-Taskrep/File.xml")
		encrypted_not = encryption(compressed_not, "Waledac_K1/K3_keyfile.key")
		encoded_not = encoding(encrypted_not)

		encoded_not_string = "a=" + encoded_not.decode('utf-8') + "b=AAAAAA"
		encoded_not_final = encoded_not_string.encode('utf-8')
		files = {'send_file': encoded_not_final}

		random_strings = random.choices(string.ascii_lowercase, k = random.randint(2,15))
		destination = server + '/'
		for i in random_strings:
			destination += i
		destination += '.htm'

		headers = {'accept' : '*/*',
		'user-agent': 'Mozilla',
		'pragma': 'no cache',
		'content-type': 'application/x-www-form-urlencoded'}

		answer = requests.post(destination, headers=headers, files=files)
		#print(answer.text.encode('utf-8'))
		decoded = decoding(answer.text.encode('utf-8'))
		decrypted = decryption(decoded, "Waledac_K1/K3_keyfile.key")
		decompressed = decompression(decrypted)
		#print("Words: ".encode('utf-8') + decompressed)
		#with open("XML_P2P_Waledac/5-Taskrep/ServerTaskRep.xml", "wb") as file:
		#	file.write(decompressed)
		print('Waledac Reported Task...')
		time.sleep(random.gauss(stealth_factor*1800,stealth_factor*15))

def email(server):
	while (True):
		email_length = 0
		with open("XML_P2P_Waledac/6-Email/File.xml", "r") as file:
			data = file.read()
		number_of_emails_to_generate = random.randint(1,20)
		for i in range(3):
			email = email_generator()
			data = data[:data.find('A[')+2+email_length] + email + '\n\t\t' + data[data.find(']]'):]
			email_length += len(email)+3
		with open("XML_P2P_Waledac/6-Email/File.xml", "w") as file:
			file.write(data)

		compressed_not = compression("XML_P2P_Waledac/6-Email/File.xml")
		encrypted_not = encryption(compressed_not, "Waledac_K1/K3_keyfile.key")
		encoded_not = encoding(encrypted_not)

		encoded_not_string = "a=" + encoded_not.decode('utf-8') + "b=AAAAAA"
		encoded_not_final = encoded_not_string.encode('utf-8')
		files = {'send_file': encoded_not_final}

		random_strings = random.choices(string.ascii_lowercase, k = random.randint(2,15))
		destination = server + '/'
		for i in random_strings:
			destination += i
		destination += '.htm'

		headers = {'accept' : '*/*',
		'user-agent': 'Mozilla',
		'pragma': 'no cache',
		'content-type': 'application/x-www-form-urlencoded'}

		answer = requests.post(destination, headers=headers, files=files)
		#print(answer.text.encode('utf-8'))
		decoded = decoding(answer.text.encode('utf-8'))
		decrypted = decryption(decoded, "Waledac_K1/K3_keyfile.key")
		decompressed = decompression(decrypted)
		#print("Words: ".encode('utf-8') + decompressed)
		#with open("XML_P2P_Waledac/6-Email/ServerEmail.xml", "wb") as file:
		#	file.write(decompressed) 
		print('Waledac Reported Harvested Emails From System')
		random_waiting_time = random.gauss(stealth_factor*10000, stealth_factor*100)
		time.sleep(random_waiting_time)



def waledac():

	print('Executing Waledac Based Botnet...')
	server = sys.argv[1]
	waledac_P2P_update(server)
	
	# Creation of Certification

	cert_gen()

	##################### Cert Model Randomization ######################

	cert_model_randomization()
	
	k3_obtention(server)

	waledac_join_request(server)

	##################### At this point, Waledac begins to actively interact with the botnet ################

	t1 = threading.Thread(target=notify, args=(server,))
	t2 = threading.Thread(target=tasqreq, args=(server,))
	#t3 = threading.Thread(target=words, args=())
	#t4 = threading.Thread(target=taskrep, args=())
	t5 = threading.Thread(target=email, args=(server,))

	t1.start()
	t2.start()
	#t3.start()
	#t4.start()
	t5.start()
	


# Execution
single_execution = False
for i,argv in enumerate(sys.argv):
	if (argv == '-Z'):
		t1 = threading.Thread(target=zeus, args=())
		t1.start()
		single_execution = True
	if (argv == '-W'):
		t2 = threading.Thread(target=waledac, args=())
		t2.start()
		single_execution = True
	if (argv == '-S'):
		try:
			stealth_factor = float(sys.argv[i+1])
		except IndexError:
			print('You must include the stealth factor value')
			sys.exit(1)
if (single_execution == False):
	t1 = threading.Thread(target=zeus, args=())
	t2 = threading.Thread(target=waledac, args=())
	t1.start()
	t2.start()