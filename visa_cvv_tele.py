import requests

A = '\033[1;10m'
B = '\033[1;36m'
C ='\033[1;30m'
D =('='*40)
print(f"""{A}{D}
<>---<>---<>---<>---<>---<>---<>---<>---<>
[*]Get VISA Cvv And send it to Telegram[*]  
<>---<>---<>---<>---<>---<>---<>---<>---<>        
      >> Naplon ◕_◕ <<
 _   _             _             
| \ | |           | |            
|  \| | __ _ _ __ | | ___  _ __  
| . ` |/ _` | '_ \| |/ _ \| '_ \ 
| |\  | (_| | |_) | | (_) | | | |{B}
|_| \_|\__,_| .__/|_|\___/|_| |_|
            | | instagram: 3h6h                 
            |_| Telegram: naplon0 
<>---<>---<>---<>---<>---<>---<>---<>    
{D}""")   


IpToken = input("Enter the TOKEN: ")
Id = input("Enter the ID: ")
naplon = "by >> Tele @naplon0"

def Nap():

    nap = requests.Session()

    url = "https://www.colorschemer.com/fetchdata/generate-home-credit-card/"

    headers = {
        "Host": "www.colorschemer.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.colorschemer.com/credit-card-generator/",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": "98",
        "Origin": "https://www.colorschemer.com",
        "DNT": "1",
        "Connection": "keep-alive",
        "Cookie": "__cfduid=dc0c9026439474694eeab705e7e633e8d1616410321; csrftoken=czvtORBrer3uv45UuVbKfDbESjgFQqk8xi9obC59foTQPO9mqlWBUirb2mY6jSOx; cookieconsent_status=dismiss"}
    data = 'brand=VISA&country=UNITED+STATES&bank=1880+BANK&cvv=&year=random&range=500+-+1000&amount=20&pin=on'

    n = nap.post(url, headers=headers, data=data)
    aa = 0
    p = 0

    while True:
        p+=1

        try:
            card_number = int(n.json()["creditCard"][aa]["CardNumber"])

            Bank = str(n.json()["creditCard"][aa]["Bank"])

            name = str(n.json()["creditCard"][aa]["Name"])

            Address = str(n.json()["creditCard"][aa]["Address"])

            CVV = int(n.json()["creditCard"][aa]["CVV"])

            Data_Time = str(n.json()["creditCard"][aa]["Expiry"])

            print(f"\r{A}{p}", end=f"{B}--Good")

            tale = (f'https://api.telegram.org/bot{IpToken}/sendMessage?chat_id={Id}&text=\n━━━━━━━━━━━━\n {name}|{card_number}|{CVV}|{Data_Time}|{Bank}|{Address} \n━━━━━━━━━━━━\n  {naplon} ')
            req = requests.post(tale)
            aa +=1

        except:
            print('')
            print(B+'')
            break
Nap()
