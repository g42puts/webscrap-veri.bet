from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json
from get_class import get_class

url = "https://veri.bet/odds-picks?filter=upcoming"

def limpa_json():
    # Abra o arquivo em modo de escrita e escreva a lista vazia
    with open(file="scrap_sports.json", mode="w") as json_file:
        json.dump(obj=[], fp=json_file)

def load_page(url:str):
    
    # limpa o arquivo json antes de continuar o script
    limpa_json()
    
    # True para ocultar o navegador, False para exibir o navegador
    NAVEGADOR_OCULTO = False
    

    # define configs de otimização do selenium
    options = Options()
    if NAVEGADOR_OCULTO:
        options.add_argument(argument='--headless') # interface gráfica, exibição do navegador

    options.add_argument(argument='--no-sandbox') # reduz consumo de recursos
    options.add_argument(argument='--disable-geolocation') # geolocalização
    options.add_argument(argument='--disable-dev-shm-usage') # compartilhamento de memoria temporaria
    options.add_argument(argument='--disable-notifications') # notificações 
    options.add_argument(argument='--disable-popup-blocking') # pop-ups
    options.add_argument(argument='--disable-gpu') # aceleração de hardware
    
    
    driver = webdriver.Firefox(options=options)
    
    driver.get(url=url)
    
    try:
        element = WebDriverWait(driver=driver, timeout=15).until(
            method=EC.presence_of_element_located(locator=(By.XPATH, '//div[@class="d-flex align-items-center p-3 text-white-50"]'))
    )
    finally:
        print("O website demorou a ser carregado, sugiro aumentar alguns segundos.")

    game_per_game_xpath = '//div[@class="row justify-content-md-center"]//div[@class="col col-md"]'
    all_games = driver.find_elements(by=By.XPATH, value=game_per_game_xpath)
    
    for game in all_games: # percorrer jogo por jogo
        lines = game.find_elements(by=By.TAG_NAME, value='span')
        itens = []
        i = 0
        for line in lines[:14]:
            itens.append(f'item{i}: {line.text.rsplit()}')
            i += 1
        get_class(content=itens)

load_page(url=url)