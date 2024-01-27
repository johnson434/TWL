import requests
import main.data.coda_data as coda_data
from main.file.file_format import FileFormat

BASE_URL = "https://coda.io/apis/v1/docs"

# https://coda.io/developers/apis/v1#tag/Pages/operation/listPages
def listPages(coda_api_key, doc_id) -> coda_data.ListPagesResponse:
    headers = {'Authorization': 'Bearer {}'.format(coda_api_key)}
    uri = f'{BASE_URL}/{doc_id}/pages'
    res = requests.get(uri, headers=headers)
    responseJson = res.json()
    
    if res.status_code != 200 : 
        error = coda_data.Error.from_dict(responseJson)
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
    SAMPLE_FILE = open(fileName, 'wb')
    SAMPLE_FILE.writelines(res)


