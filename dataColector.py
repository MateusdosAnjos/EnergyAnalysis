import os.path
import requests
import zipfile 
import io
import re

MONTHS = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def detectOldFilesDate() -> str:
    files_in_dir = os.listdir('.')
    regex_to_match = r'RALIE_.*'
    for file_name in files_in_dir:
        is_match = re.findall(regex_to_match, file_name)
        if is_match:
            date_with_RALIE = is_match[0].split("_")
            date = date_with_RALIE[1].split("-")
            return MONTHS[int(date[1]) - 1] + " de " + date[0]
    return ""


def findLinkOnPage() -> list:
    url_to_get =  "https://www.aneel.gov.br/acompanhamento-da-expansao-da-oferta-de-geracao-de-energia-eletrica"

    response = requests.get(url_to_get)
    regex_to_match = r'href=".*".*Base[ \t\n]+de[ \t\n]+dados[ \t\n]+do[ \t\n]+RALIE[ \t\n]+\(.*\)'
    link_and_label = re.findall(regex_to_match, response.text)
    if (len(link_and_label) != 1):
        print("Error on getLinkToDownload. NUMBER OF HREF FOUND = " + str(len(link_and_label)) + " the number must not be different from 1")
        return None
    return link_and_label

def getLinkToDownload(link_and_label: list) -> str:
    return link_and_label[0].split('"')[1]

def getZIPFileDate(link_and_label: list) -> str:
    return link_and_label[0].split("(")[-1][:-1]

def downloadZIPFile(link: str) -> int:
    link = "https://www.aneel.gov.br/" + link
    r = requests.get(link)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()

def main():
    old_archive_date = detectOldFilesDate()
    print("DATA DO ARQUIVO ANTIGO: ", old_archive_date)
    link_and_label = findLinkOnPage()
    link = getLinkToDownload(link_and_label)
    date = getZIPFileDate(link_and_label)
    #Link to download not found.
    if link == '':
        return
    print("LINK: ", link)
    print("DATA DO NOVO ARQUIVO: ", date)
    if old_archive_date != date:
        print("BAIXANDO...")
        downloadZIPFile(link)
    else:
        print("ARQUIVO MAIS RECENTE JÁ ESTÁ NO DIRETÓRIO!")
main()