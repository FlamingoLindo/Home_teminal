import os

from General import open_url

def open_multiple_asana_links():
    """Open multiple Asana links."""
    asana_urls = [
        "https://app.asana.com/0/1207221290310617/1207225690268341",
        "https://app.asana.com/0/1207504713283391/1207504634680432",
        "https://app.asana.com/0/1207747544851675/1207747639592319",
        "https://app.asana.com/0/1207933859745403/1207934164249687",
        "https://app.asana.com/0/1206990839359887/1206991821570634",
        "https://app.asana.com/0/1207990406862834/1207991814209722",
        "https://www.notion.so/work-esteralvim/APRESENTA-O-MOTORFIND-INTEGRA-O-faea137f72eb4f26b02ae95e685ba519?pvs=11"
    ]

    for asana in asana_urls:
        print(f"Opening {asana}...")
        open_url(asana)
        
def open_project_tabs():
    """Open multiple Asana links."""
    prject_tabs = [
        "https://motorfind-client.netlify.app/",
        "https://motorfind-master.netlify.app/",
        "https://crm-mestres-web-v2024.netlify.app/",
        "https://saas-64327.bubbleapps.io/pagina_inicial"
    ]

    for tab in prject_tabs:
        print(f"Opening {tab}...")
        open_url(tab)
        
def start_appium():
    try:
        os.system(f"appium --allow-cors")
    except Exception as e:
        print(f"Failed to start Appium server. Error: {e}")
        
def start_adb():
    try:
        os.system(f"adb devices")
    except Exception as e:
        print(f"Failed to start adb. Error: {e}")
        
def open_gen_tabs():
    gen_tabs = [
        "https://www.4devs.com.br/gerador_de_cpf",
        "https://www.4devs.com.br/gerador_de_cnpj",
        "https://www.4devs.com.br/gerador_de_cep",
        "https://www.4devs.com.br/gerador_de_numero_cartao_credito",
        "https://www.4devs.com.br/gerador_conta_bancaria",
        "https://temp-mail.org/pt/"
    ]

    for tab in gen_tabs:
        print(f"Opening {tab}...")
        open_url(tab)