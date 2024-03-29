from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class Error:
    statusCode: str
    statusMessage: str
    message: str

    @staticmethod
    def from_dict(obj: Any) -> 'Error':
        _statusCode = obj.get('statusCode')
        _statusMessage = obj.get('statusMessage')
        _message = obj.get('message')
        return Error(statusCode=_statusCode, statusMessage=_statusMessage, message=_message)

@dataclass
class Page:
    id: str
    type: str
    browserLink: str
    href: str
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        _id = str(obj.get("id"))
        _type = str(obj.get("type"))
        _browserLink = str(obj.get("browserLink"))
        _href = str(obj.get("href"))
        _name = str(obj.get("name"))

        return Page(
            id=_id,
            type=_type,
            browserLink=_browserLink,
            href=_href,
            name=_name
        )

@dataclass
class Item:
    id: str
    type: str
    href: str
    name: str
    isHidden: bool
    isEffectivelyHidden: bool
    browserLink: str
    children: List[Page]
    contentType: str
    createdAt: str
    updatedAt: str

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        _id = str(obj.get('id'))
        _type = str(obj.get("type"))
        _href = str(obj.get("href"))
        _name = str(obj.get("name"))
        _isHidden = str(obj.get("isHidden"))
        _isEffectivelyHidden = str(obj.get("isEffectivelyHidden"))
        _browserLink = str(obj.get("browserLink"))
        _children = [Page.from_dict(y) for y in obj.get("children")]
        _contentType = str(obj.get("contentType"))
        _createdAt = str(obj.get("createdAt"))
        _updatedAt = str(obj.get("createdAt"))
        
        return Item(
            id=_id, 
            type= _type, 
            href=_href, 
            name=_name, 
            isHidden=_isHidden, 
            isEffectivelyHidden=_isEffectivelyHidden, 
            browserLink=_browserLink, 
            children=_children,
            contentType=_contentType,
            createdAt=_createdAt,
            updatedAt=_updatedAt
        )


@dataclass
class ListPagesResponse:
    items: List[Item]
    href: str

    @staticmethod
    def from_dict(obj) -> 'ListPagesResponse':
        _items = [Item.from_dict(y) for y in obj.get("items")]
        _href = str(obj.get("href"))
        return ListPagesResponse(items=_items, href=_href)
    
@dataclass
class ExportPageResponse:
    request_id: str
    status: str
    href: str

    @staticmethod
    def from_dict(obj) -> 'ExportPageResponse':
        _request_id = obj.get("id")
        _status = obj.get("status")
        _href = obj.get("href")
        return ExportPageResponse(
            request_id=_request_id,
            status=_status,
            href=_href
        )

@dataclass
class GetExportStatusResponse:
    id: str
    status: str
    downloadLink: str
    error: str

    @staticmethod
    def from_dic(obj) -> 'GetExportStatusResponse':
        _id = obj.get('id')
        _status = obj.get('status')
        _downloadLink = obj.get('downloadLink')
        _error = obj.get('error')
        return GetExportStatusResponse(
            id = _id,
            status= _status,
            downloadLink=_downloadLink,
            error=_error
        )
    
@dataclass
class ContentExportStatusResponse:
    id: str
    status: str
    href: str
    downloadLink: str
    error: str

    @staticmethod
    def from_dict(obj) -> 'ContentExportStatusResponse':
        _id = str(obj.get('id'))
        _status = str(obj.get('status'))
        _href = str(obj.get('href'))
        _downloadLink = str(obj.get('downloadLink'))
        _error = str(obj.get('error'))
        return ContentExportStatusResponse(
            id=_id,
            status=_status,
            href=_href,
            downloadLink=_downloadLink,
            error=_error
        )


@dataclass
class Author:
    additionalType: str
    name: str
    email: str

    @staticmethod
    def from_dict(obj) -> 'Author':
        _name = str(obj.get("name"))
        _email = str(obj.get("email"))
        return Author(name=_name, email=_email)




