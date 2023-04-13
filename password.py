from cryptography.fernet import Fernet

import password_app.vlastniknihovna as vlastniknihovna




#overeni existence hesla v souboru key.key
file = open("key.key", "r")
if len(file.read()) < 1:
    a_file = open("passwords.txt", "w")
    a_file.truncate()
    a_file.close()
    
    vlastniknihovna.write_key()
    key = vlastniknihovna.load_key()
    f = Fernet(key)
   
        
    print("New key for encryption was set \n u can now add new accs")
else:
    print("data stored, u can add or view")
    















while(True):
    mode = input("Chces pridat nove heslo nebo zobrazit existujici hesla? (pridat, zobrazit, konec)")
    if mode == "konec":
        break
    if mode == "pridat":
        vlastniknihovna.add()
    elif mode == "zobrazit":
        vlastniknihovna.view()
    else:
        print("Nespravná volba")
        continue
