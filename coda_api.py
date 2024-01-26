import sys
import requests
import coda_data

BASE_URL = "https://coda.io/apis/v1/docs"

# todo : 제거해야됨

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

def is_export_done(coda_api_key, doc_id, page_id, request_id):
    headers = {'Authorization': 'Bearer {}'.format(coda_api_key)}
    uri = f'{BASE_URL}/{doc_id}/pages/{page_id}/export'/{request_id}
    res = requests.get(url=uri, headers=headers)
    return res

# 토큰 및 쿼리 파람 설정
# args = sys.argv
# coda_api_key = args[1]
doc_id = "OBsatQ1Yn9"
# print("args : ", args)

# 가능한 페이지 출력
# print("=====================listPages=====================")
# list_pages = listPages(coda_api_key=coda_api_key, doc_id=doc_id)
# print(f'listPages : {list_pages}')

# export page
print("=====================export_page=====================")
page_id = 'canvas-xbssZmCV_3'
exportPageResponse = export_page(coda_api_key=coda_api_key, doc_id=doc_id, page_id=page_id)
request_id = exportPageResponse.request_id
print(f'request_id : {request_id}')


