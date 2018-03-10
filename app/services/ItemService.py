import os
import json
import time
from ..models.item import Item

def SaveNewItem(item):
    items=[]
    data = {
                "uni_id":item.uni_id,
                "title":item.title,
                "status":item.status,
                "description":item.description,
                "tags":item.tags,
                "updatetime":item.updatetime
            }
    if not os.path.exists("item.json"):
        items = [data]
        with open("item.json","w") as fp:
            json.dump(items,fp)
    else:
        with open("item.json",'r+') as fp:
            items = json.load(fp)
            items.append(data)
        with open("item.json","w") as fp:
            json.dump(items,fp)
    return items     

def GetAllItems():
    items = []
    if not os.path.exists("item.json"):
        return []
    else:
        with open("item.json",'r') as fp:
            json_items = json.load(fp)
            for ji in json_items:
                items.append(Item(
                    uni_id=ji["uni_id"],
                    title=ji["title"],
                    status=ji["status"],
                    description=ji["description"],
                    tags=ji["tags"],
                    updatetime=ji["updatetime"]
                ))
    return items

def GetItemById(item_id):
    item=None
    for x in GetAllItems():
        if x.uni_id==item_id:
            item=x
    return item

def UpdateItem(item):
    json_items=None
    with open("item.json",'r') as fp:
            json_items = json.load(fp)
            for ji in json_items:
                if ji["uni_id"]==item.uni_id:
                    ji["title"]=item.title
                    ji["status"]=item.status
                    ji["description"]=item.description
                    ji["tags"]=item.tags
                    ji["updatetime"]=item.updatetime
                    break
    with open("item.json",'w') as fp:
        json.dump(json_items,fp)