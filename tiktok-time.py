from datetime import datetime

id = 7232321170668915994

def tiktok_time(urlid):
    binary = "{0:b}".format(urlid)[:31]  # Convertir en binaire et prendre les 31 premiers chiffres
    timestamp = int(binary, 2)  # Convertir les bits en entier, qui est notre timestamp
    obj_timestamp = datetime.fromtimestamp(timestamp)  # Convertir notre timestamp en objet datetime
    print(obj_timestamp)


tiktok_time(id)
