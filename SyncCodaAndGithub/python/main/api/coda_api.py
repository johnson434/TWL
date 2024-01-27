import requests
import main.data.coda_data as coda_data
import logging
from main.file.file_format import FileFormat

BASE_URL = "https://coda.io/apis/v1/docs"

logger = logging.getLogger("main")

# https://coda.io/developers/apis/v1#tag/Pages/operation/listPages
def listPages(coda_api_key, doc_id) -> coda_data.ListPagesResponse:
    logger.debug('called')

    headers = {'Authorization': 'Bearer {}'.format(coda_api_key)}
    uri = f'{BASE_URL}/{doc_id}/pages'
    logger.info(f'headers : {headers}\nuri : {uri}')

    res = requests.get(uri, headers=headers)
    responseJson = res.json()
    logger.info(f'responseJson : {responseJson}')
    
    if res.status_code != 200 : 
        error = coda_data.Error.from_dict(responseJson)
        logger.error(error)
        return None
    
    return coda_data.ListPagesResponse.from_dict(responseJson)

# https://coda.io/developers/apis/v1#tag/Pages/operation/beginPageContentExport
def export_page(coda_api_key, doc_id, page_id) -> coda_data.ExportPageResponse:
    logger.debug("called")

    headers = {'Authorization': 'Bearer {}'.format(coda_api_key)}
    uri = f'{BASE_URL}/{doc_id}/pages/{page_id}/export'
    payload = { 'outputFormat' : 'markdown' }
    logger.info(f'headers : {headers}\nuri : {uri}\npayload : {payload}')

    res = requests.post(uri, headers=headers, json=payload)
    responseJson = res.json()
    logger.info(f'responseJson : {responseJson}')

    if res.status_code != 202 : 
        error = coda_data.Error.from_dict(responseJson)
        logger.error(error)
        return None
    
    return coda_data.ExportPageResponse.from_dict(responseJson)

def requestContentExportStatus(coda_api_key, doc_id, page_id, request_id) -> coda_data.ContentExportStatusResponse:
    logger.debug('called')

    headers = {'Authorization': 'Bearer {}'.format(coda_api_key)}
    uri = f'{BASE_URL}/{doc_id}/pages/{page_id}/export/{request_id}'
    logger.info(f'headers : {headers}\nuri : {uri}\n')

    res = requests.get(url=uri, headers=headers)
    responseJson = res.json()
    logger.info(f'responseJson : {responseJson}')

    if res.status_code != 200 or responseJson.get('status') != 'complete':
        error = coda_data.Error.from_dict(responseJson)
        logger.error(error)
        return None
    
    return coda_data.ContentExportStatusResponse.from_dict(responseJson)

def downloadLink(link, file_name, file_format: FileFormat):
    logger.debug('called')

    res = requests.get(link)
    fullFileName = f'./{file_name}'
    if file_format == FileFormat.Markdown:
        fullFileName += ".md"
    elif file_format == FileFormat.HTML:
        fullFileName += ".html"
    logger.info(f'fileName : {fullFileName}')

    SAMPLE_FILE = open(fullFileName, 'wb')

    SAMPLE_FILE.writelines(res)

def getPage(coda_api_key, doc_id, pageIdOrName) -> coda_data.Page:
    logger.debug('called')

    headers = {'Authorization': 'Bearer {}'.format(coda_api_key)}
    uri = f'{BASE_URL}/{doc_id}/pages/{pageIdOrName}'
    logger.info(f'headers : {headers}\nuri : {uri}')

    res = requests.get(uri, headers=headers)
    responseJson = res.json()
    logger.info(f'responseJson : {responseJson}')
    
    if res.status_code != 200 : 
        error = coda_data.Error.from_dict(responseJson)
        logger.error(error)
        return None
    
    return coda_data.Page.from_dict(responseJson)

