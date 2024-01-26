import sys
import requests
import coda_data

BASE_URL = "https://coda.io/apis/v1/docs"

# todo : 제거해야됨
coda_api_key = "1757b242-eed6-411d-963b-190363540114"

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

def export_page(coda_api_key, doc_id, page_id):
    headers = {'Authorization': 'Bearer {}'.format(coda_api_key)}
    uri = f'{BASE_URL}/{doc_id}/pages/{page_id}/export'
    res = requests.post(uri, headers=headers).json()
    return res

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
list_pages = listPages(coda_api_key=coda_api_key, doc_id=doc_id)
print(f'listPages : {list_pages}')
