import sys
import requests

def get_list_pages(coda_api_key, doc_id):
    headers = {'Authorization': 'Bearer {}'.format(coda_api_key)}
    uri = f'https://coda.io/apis/v1/docs/{doc_id}/pages'
    res = requests.get(uri, headers=headers).json()
    return res

args = sys.argv
coda_api_key = args[0]
doc_id = "OBsatQ1Yn9"

print("args : ", args)

list_pages = get_list_pages(coda_api_key=coda_api_key, doc_id=doc_id)
for page in list_pages["items"]:
    name = page["name"]
    id = page["id"]
    print(f"name : {name} id : {id}")

