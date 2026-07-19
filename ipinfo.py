import os
import requests
os.system("clear")
ip = input("IP Address: ")
response = requests.get("https://api.ipquery.io/" + ip)
data = response.json()
print("""
Country: """ + str({data['location']['country']}) + """
Country Code: """ + str({data['location']['country_code']}) + """
City: """ + str({data['location']['city']}) + """
State: """ + str({data['location']['state']}) + """
Zipcode: """ + str({data['location']['zipcode']}) + """
Timezone: """ + str({data['location']['timezone']}) + """
IsMobile?: """ + str({data['risk']['is_mobile']}) + """
IsVPN?: """ + str({data['risk']['is_vpn']}) + """
IsTor?: """ + str({data['risk']['is_tor']}) + """
IsProxy?: """ + str({data['risk']['is_proxy']}) + """
Risk Score: """ + str({data['risk']['risk_score']}))