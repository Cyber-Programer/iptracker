import requests as r
import json as j
def pnt():
    print('''
        1)Track taget ip
        2)Track your ip
        ''')
def banner():
    banner='''
    333333333333333333333333333333333333333333
    3 ❤        😎HALAL-ASHACKER😎         ❤  3                   
    3                                        3
    3                Track ip                3     
    3                                        3
    3            Thank's for using           3
    3 ❤                                   ❤  3      
    333333333333333333333333333333333333333333

    '''
    print(banner)
banner()
pnt()
x=int(input("Ener yor option: "))
if x==1:
        api = "44e830b757c94946814b5811fec0eb4e"
        print("Enter your target ip")
        ip =input('=> ')  # Example public IP address

        url = f'https://ipgeolocation.abstractapi.com/v1/?api_key={api}&&ip_address={ip}'

        response = r.get(url)
        #print(response)
        json_data = j.loads(response.text)
        print(j.dumps(json_data, indent=4))
        #---------------------------------------------------------------------------------------
        
elif x==2:
        api = "44e830b757c94946814b5811fec0eb4e"
        print("your ip was tracking..........")
        url = f'https://ipgeolocation.abstractapi.com/v1/?api_key={api}'
        response = r.get(url)
        #print(response)
        json_data = j.loads(response.text)
        print(j.dumps(json_data, indent=4))
        #------------------------------------------------------------------------------------------
else:
    print("wrong option")