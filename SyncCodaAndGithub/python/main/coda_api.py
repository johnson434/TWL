import sys
import requests
import queue
import time
from enum import Enum
from main.data import coda_data

class FileFormat(Enum):
    Markdown = 1
    HTML = 2

BASE_URL = "https://coda.io/apis/v1/docs"
doc_id = "OBsatQ1Yn9"

# todo : 제거해야됨
# coda_api_key = open("../../token.txt", mode='r').readline()

# https://coda.io/developers/apis/v1#tag/Pages/operation/listPages
def listPages(coda_api_key, doc_id) -> coda_data.ListPagesResponse:
    headers = {'Authorization': 'Bearer {}'.format(coda_api_key)}
    uri = f'{BASE_URL}/{doc_id}/pages'
    res = requests.get(uri, headers=headers)
    responseJson = res.json()
    
    if res.status_code != 200 : 
        error = coda_data.Error.from_dict(responseJson)
        print(f'statusCode : {error.statusCode}\nstatusMessage : {error.statusMessage}\nmessage : {error.message}')
        return None
    
    return coda_data.ListPagesResponse.from_dict(responseJson)

# https://coda.io/developers/apis/v1#tag/Pages/operation/beginPageContentExport
def export_page(coda_api_key, doc_id, page_id) -> coda_data.ExportPageResponse:
    headers = {'Authorization': 'Bearer {}'.format(coda_api_key)}
    uri = f'{BASE_URL}/{doc_id}/pages/{page_id}/export'
    payload = { 'outputFormat' : 'markdown' }
    res = requests.post(uri, headers=headers, json=payload)
    responseJson = res.json()
    print(f'res : {res}')
    print(f'responseJson : {responseJson}')
    print(f'responseCode : ${res.status_code}')

    if res.status_code != 202 : 
        error = coda_data.Error.from_dict(responseJson)
        print(f'statusCode : {error.statusCode}\nstatusMessage : {error.statusMessage}\nmessage : {error.message}')
        return None
    
    return coda_data.ExportPageResponse.from_dict(responseJson)

def get_downloadLink(coda_api_key, doc_id, page_id, request_id) -> bool:
    headers = {'Authorization': 'Bearer {}'.format(coda_api_key)}
    uri = f'{BASE_URL}/{doc_id}/pages/{page_id}/export/{request_id}'
    print(f'is_export_done : uri : {uri}')
    res = requests.get(url=uri, headers=headers)
    responseJson = res.json()
    print(f'isExportDone responseJson : {responseJson}')

    if res.status_code != 200 or responseJson.get('status') != 'complete':
        error = coda_data.Error.from_dict(responseJson)
        print(f'statusCode : {error.statusCode}\nstatusMessage : {error.statusMessage}\nmessage : {error.message}')
        return None
    
    return responseJson.get('downloadLink')

def downloadLink(link, file_name, file_format: FileFormat):
    res = requests.get(link)
    fileName = "./" + file_name
    if file_format == FileFormat.Markdown:
        fileName += ".md"
    elif file_format == FileFormat.HTML:
        fileName += ".html"
    else:
        fileName += ".txt"
    
    SAMPLE_FILE = open(fileName, 'wb')
    SAMPLE_FILE.writelines(res)


def main():
    # 토큰 및 쿼리 파람 설정
    args = sys.argv
    coda_api_key = args[1]
    
    # 가능한 페이지 출력
    print("=====================listPages=====================")
    list_pages = listPages(coda_api_key=coda_api_key, doc_id=doc_id)
    print(f'listPages : {list_pages}')

    # export page
    print("=====================export_page=====================")
    page_id = 'canvas-xbssZmCV_3'
    exportPageResponse = export_page(coda_api_key=coda_api_key, doc_id=doc_id, page_id=page_id)
    print(f'exportPageResponse : {exportPageResponse}')
    request_id_list = queue.Queue()
    request_id_list.put(exportPageResponse)
    time.sleep(5)

    # check Status
    print("=====================check_status=====================")
    print(f'request_id_list : {request_id_list} request_id_list.empty {request_id_list.empty()} request_id_list.qsize : {request_id_list.qsize()}')
    while not request_id_list.empty():
        tempResponse = request_id_list.get()
        print(f'tempResponse : {tempResponse}')

        link = get_downloadLink(coda_api_key=coda_api_key, doc_id=doc_id, page_id=page_id, request_id=tempResponse.request_id)
        if  link == None:
            print(f'request is in progrss. request_id : {id}')
            request_id_list.put(id)
            time.sleep(3)
            continue
        downloadLink(link, 'sample_file', FileFormat.Markdown)