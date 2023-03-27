try:
    from termcolor import colored
except ModuleNotFoundError:
    import os
    os.system('pip install termcolor')
    from termcolor import colored
try:
    import requests
except ModuleNotFoundError:
    import os
    os.system('pip install requests')
import requests as r

def pnt():
    print(colored('''
    1)Track target ip
    2)Track your ip
    ''', 'green'))

def banner():
    banner = colored('''
    333333333333333333333333333333333333333333
    3 ❤            😎2rootv3😎            ❤  3                   
    3                                        3
    3                Track ip                3     
    3                                        3
    3            Thank's for using           3
    3 ❤                                   ❤  3      
    333333333333333333333333333333333333333333
    ''', 'yellow')
    print(banner)

banner()
pnt()

x = int(input(colored("Enter your option: ", 'yellow')))
if x == 1:
    def targetip():
        api = "44e830b757c94946814b5811fec0eb4e"
        print(colored("Enter your target ip", 'yellow'))
        ip = input(colored('=> ', 'green'))
        url = f'https://ipgeolocation.abstractapi.com/v1/?api_key={api}&&ip_address={ip}'

        response = r.get(url)
        show = response.json()

        print(colored(f"\nip_address: {show['ip_address']}", 'cyan'))
        print(colored(f"city: {show['city']}", 'cyan'))
        print(colored(f"city_geoname_id: {show['city_geoname_id']}", 'cyan'))
        print(colored(f"region: {show['region']}", 'cyan'))
        print(colored(f"region_iso_code: {show['region_iso_code']}", 'cyan'))
        print(colored(f"region_geoname_id: {show['region_geoname_id']}", 'cyan'))
        print(colored(f"postal_code: {show['postal_code']}", 'cyan'))
        print(colored(f"country: {show['country']}", 'cyan'))
        print(colored(f"country_code: {show['country_code']}", 'cyan'))
        print(colored(f"country_geoname_id: {show['country_geoname_id']}", 'cyan'))
        print(colored(f"country_is_eu: {show['country_is_eu']}", 'cyan'))
        print(colored(f"continent: {show['continent']}", 'cyan'))
        print(colored(f"continent_code: {show['continent_code']}", 'cyan'))
        print(colored(f"continent_geoname_id: {show['continent_geoname_id']}", 'cyan'))
        print(colored(f"longitude: {show['longitude']}", 'cyan'))
        print(colored(f"latitude : {show['latitude']}", 'cyan'))
        print(colored(f"security: {show['security']}", 'cyan'))

        timezone = show['timezone']
        print(colored(f"Timezone: {timezone['name']}", 'cyan'))
        print(colored(f"abbreviation: {timezone['abbreviation']}", 'cyan'))
        print(colored(f"gmt_offset : {timezone['gmt_offset']}", 'cyan'))
        print(colored(f"current_time: {timezone['current_time']}", 'cyan'))
        print(colored(f"is_dst : {timezone['is_dst']}", 'cyan'))

    targetip()
elif x == 2:
    print(colored("your ip wass tracked............",'yellow'))
    def ip():
        api = "44e830b757c94946814b5811fec0eb4e"
        url = f'https://ipgeolocation.abstractapi.com/v1/?api_key={api}'

        response = r.get(url)
        show = response.json()

        print(colored(f"\nip_address: {show['ip_address']}", 'cyan'))
        print(colored(f"city: {show['city']}", 'cyan'))
        print(colored(f"city_geoname_id: {show['city_geoname_id']}", 'cyan'))
        print(colored(f"region: {show['region']}", 'cyan'))
        print(colored(f"region_iso_code: {show['region_iso_code']}", 'cyan'))
        print(colored(f"region_geoname_id: {show['region_geoname_id']}", 'cyan'))
        print(colored(f"postal_code: {show['postal_code']}", 'cyan'))
        print(colored(f"country: {show['country']}", 'cyan'))
        print(colored(f"country_code: {show['country_code']}", 'cyan'))
        print(colored(f"country_geoname_id: {show['country_geoname_id']}", 'cyan'))
        print(colored(f"country_is_eu: {show['country_is_eu']}", 'cyan'))
        print(colored(f"continent: {show['continent']}", 'cyan'))
        print(colored(f"continent_code: {show['continent_code']}", 'cyan'))
        print(colored(f"continent_geoname_id: {show['continent_geoname_id']}", 'cyan'))
        print(colored(f"longitude: {show['longitude']}", 'cyan'))
        print(colored(f"latitude : {show['latitude']}", 'cyan'))
        print(colored(f"security: {show['security']}", 'cyan'))

        timezone = show['timezone']
        print(colored(f"Timezone: {timezone['name']}", 'cyan'))
        print(colored(f"abbreviation: {timezone['abbreviation']}", 'cyan'))
        print(colored(f"gmt_offset : {timezone['gmt_offset']}", 'cyan'))
        print(colored(f"current_time: {timezone['current_time']}", 'cyan'))
        print(colored(f"is_dst : {timezone['is_dst']}", 'cyan'))
    ip()
