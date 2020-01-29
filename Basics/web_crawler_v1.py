# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:25:00 2019

@author: Thiago Farias
"""
from bs4 import BeautifulSoup
import requests 

def extrai_titulo(pagina): # pagina é o conteúdo html
    soup = BeautifulSoup(pagina,"lxml") # lxml é um parser(analisador sintático) para fazer a raspagem da página
    tag = soup.find('title', text = True) # retorna o nome da primeira tag título se houver um texto na tag
    if not tag:
        return None
    return tag.string.strip()

def extrai_links(pagina):
    soup = BeautifulSoup(pagina, "lxml")
    links = set()
    for tag in soup.find_all('a', href = True):
        if tag["href"].startswith("http"):
            links.add(tag["href"])
    return links

def crawl(url_inicial):
    urls_vistas = set()
    urls_disponiveis = set([url_inicial])
    
    while urls_disponiveis:
        url = urls_disponiveis.pop()
        try:
            pagina = requests.get(url, timeout = 2).text
            title = extrai_titulo(pagina)
            if title:
                print(title)
                print(url)
                print("")
                for link in extrai_links(pagina):
                    if link not in urls_vistas:
                        urls_vistas.add(link)
                        urls_disponiveis.add(link)            
        except Exception:
            continue
try:
    crawl("https://www.youtube.com/")
except KeyboardInterrupt:
    print("/n falou")