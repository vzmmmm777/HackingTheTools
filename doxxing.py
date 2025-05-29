from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.parse 
import traceback 
print ("Checking Modules")
print ("If a error use setup.py")
print ("Thank you for use my tool")
print ("Starting Doxxing")

import os
os.system("")
os.system("figlet Starting Doxxing")
os.system("sudo apt update")
os.system("sudo apt upgrade")
os.system("clear")
os.system("figlet Doxxing")

def construir_url_busca_jusbrasil(nome_para_buscar):
    """
    ...starting tool '+'.
    """
    nome_codificado = urllib.parse.quote_plus(nome_para_buscar)
    
  
    url_base = "https://www.jusbrasil.com.br/busca?q="
    url_completa = f"{url_base}{nome_codificado}"
    
    return url_completa

def navegar_url_headless_e_obter_final(target_url):
    """
    wait 5 sec.
    """
    browser = None 

    try:
        
        chrome_options = Options()
        chrome_options.add_argument('--headless') 
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu') 

        
        browser = webdriver.Chrome(options=chrome_options)
        print("search victim.")
        print(f"found victim archive: {target_url}")

        
        browser.get(target_url)

      
        final_url_alcançada = browser.current_url
        f"Doxxing of victim found: {final_url_alcançada}"
        
        return final_url_alcançada

    except Exception as e:
        print(f"ERROR:URL NOT FOUND '{target_url}': {e}")
        traceback.print_exc() 
        return None 

    finally:
        if browser is not None:
            browser.quit()
        print("Stsrting Doxxing...")


if __name__ == "__main__":
    nome_da_vitima = input("Enter Name Completed Of Victim: ")
    
    url_construida = construir_url_busca_jusbrasil(nome_da_vitima)
    print(f"\nURL archive of victim: {url_construida}")
    
  
    url_final_pelo_navegador = navegar_url_headless_e_obter_final(url_construida)
    
    if url_final_pelo_navegador:
        print(f"\n--- Search Archive of Victim ---")
        print(f"Name Search: {nome_da_vitima}")
        print(f"URL Of Archive Of Victim: {url_final_pelo_navegador}")
    else:
        print(f"\n error:not found victim '{nome_da_vitima}'.")