import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
script_version = '4.0.0'
window_title   = f"WARP-PLUS-CLOUDFLARE by Dev_Nergis (version {script_version})"
os.system('title ' + window_title if os.name == 'nt' else 'PS1="\[\e]0;' + window_title + '\a\]"; echo $PS1')
os.system('cls' if os.name == 'nt' else 'clear')

print("  _    _   ___  ______ ______         ______  _      _   _  _____  ")
print(" | |  | | / _ \ | ___ \| ___ \        | ___ \| |    | | | |/  ___| ")
print(" | |  | |/ /_\ \| |_/ /| |_/ / ______ | |_/ /| |    | | | |\ `--.  ")
print(" | |/\| ||  _  ||    / |  __/ |______||  __/ | |    | | | | `--. \ ")
print(" \  /\  /| | | || |\ \ | |            | |    | |____| |_| |/\__/ / ")
print("  \/  \/ \_| |_/\_| \_|\_|            \_|    \_____/ \___/ \____/  ")

print ("[+] 스크립트 소개:")
print ("[-] 이 스크립트를 사용하면 Warp에서 무제한 GB를 얻을 수 있습니다.")
print (f"[-] 버전: {script_version}")
print ("--------")
print ("[+] 이 스크립트는 Dev_Nergis 가 코딩했습니다.") 
print ("[-] SITE: None") 
print ("[-] DISCORD: https://discord.gg/NnaBJj6Gn8")
print ("--------")

print(" ||   / |  / /     // | |     //   ) )     //   ) )           //   ) )      / /        //   / /     //   ) )  ")
print(" ||  /  | / /     //__| |    //___/ /     //___/ /           //___/ /      / /        //   / /     ((         ")
print(" || / /||/ /     / ___  |   / ___ (      / ____ /   ____    / ____ /      / /        //   / /        \\       ")
print(" ||/ / |  /     //    | |  //   | |     //                 //            / /        //   / /           ) )    ")
print(" |  /  | /     //     | | //    | |    //                 //            / /____/ / ((___/ /     ((___ / /     ")

referrer  = input("[#] 사용자 ID를 입력하십시오:")
def progressBar():
	animation     = ["[□□□□□□□□□□]","[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]"]
	progress_anim = 0
	save_anim     = animation[progress_anim % len(animation)]
	percent       = 0
	while True:
		for i in range(10):
			percent += 1
			sys.stdout.write(f"\r[+] Waiting response...  " + save_anim + f" {percent}%")
			sys.stdout.flush()
			time.sleep(0.075)
		progress_anim += 1
		save_anim = animation[progress_anim % len(animation)]
		if percent == 100:
			sys.stdout.write("\r[+] 요청 완료... [■■■■■■■■■■] 100%")
			break

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print("")
		print(error)	

g = 0
b = 0
while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	sys.stdout.write("\r[+] Sending request...   [□□□□□□□□□□] 0%")
	sys.stdout.flush()
	result = run()
	if result == 200:
		g += 1
		progressBar()
		print(f"\n[-] 작업 ID: {referrer}")    
		print(f"[:)] {g} GB가 계정에 성공적으로 추가되었습니다.")
		print(f"[#] 총: {g} Good {b} Bad")
		for i in range(22,0,-1):
			sys.stdout.write(f"\r[*] {i} 초 후에 새 요청이 전송됩니다.")
			sys.stdout.flush()
			time.sleep(1)
	else:
		b += 1
		print("[:(] 서버에 연결할 때 오류가 발생했습니다.")
		print(f"[#] 총: {g} Good {b} Bad")
		for i in range(10,0,-1):
			sys.stdout.write(f"\r[*] 재시도 중 {i}s...")
			sys.stdout.flush()
			time.sleep(1)

