import requests, re
def exec(url,headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
        return
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
        return
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        return
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)
        return
    cadena = response.text
    patron = r'"original_title"\s*:\s*"([^"]+)"'
    resultados = re.findall(patron, cadena)
    contador = 1
    for resultado in resultados:
        print(f"{contador}. {resultado}")
        contador += 1
def auth():
    file = open("data/token.txt",'r')
    token = file.readline()
    file.close
    return token