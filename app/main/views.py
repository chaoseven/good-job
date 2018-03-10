import time,uuid
from flask import render_template,request
from . import main
from ..services.ItemService import SaveNewItem,GetAllItems,GetItemById,UpdateItem
from ..models.item import Item

@main.route("/")
def index():
    return home('home')

def home(id):
    return render_template('main/index.html',active_item=id)

@main.route('/<id>')
def items(id):
    items = GetAllItems()
    overdue_items=[it for it in items if it.status=="overdue"]
    inprogress_items=[it for it in items if it.status=="inprogress"]
    ready_items=[it for it in items if it.status=="ready"]
    completed_items=[it for it in items if it.status=="completed"]
    canceled_items=[it for it in items if it.status=="canceled"]

    return render_template('main/items.html'
    ,active_item=id
    ,items=items
    ,overdue_items=overdue_items
    ,inprogress_items=inprogress_items
    ,ready_items=ready_items
    ,completed_items=completed_items
    ,canceled_items=canceled_items)

@main.route('/items/add_item',methods=['GET'])
def add_item():
    return render_template('main/add_item.html',active_item='items')

@main.route('/items/post_item',methods=['POST'])
def post_item():
    title = request.form["title"]
    status = request.form["status"]
    description = request.form["description"]
    tags = request.form["tags"]
    updatetime = time.strftime("%Y-%m-%d %H:%M:%S")
    uni_id=time.strftime("%Y%m%d%H%M%S")
    item = Item(uni_id,title,status,description,tags,updatetime)
    SaveNewItem(item)
    return "OK"

@main.route("/items/edit_item/<id>/<item_id>")
def edit_item(id,item_id):
    item=GetItemById(item_id)
    return render_template("main/edit_item.html",item=item,active_item=id)

@main.route("/items/update_item",methods=["POST"])
def update_item():
    item=Item(
        uni_id=request.form["uni_id"],
        title=request.form["title"],
        status=request.form["status"],
        description=request.form["description"],
        tags=request.form["tags"],
        updatetime=time.strftime("%Y-%m-%d %H:%M:%S")
    )

    UpdateItem(item)
    return "OK"

@main.route("/items/query_items/<id>/<st>")
def get_item_with_status(id,st):
    items=GetAllItems()
    res = [it for it in items if it.status==st]
    return render_template("main/query_items.html",items=res,active_item=id,st=st)

@main.route("/items/query_by_tag/<id>/<tag>")
def get_item_with_tag(id,tag):
    items=GetAllItems()
    res=[it for it in items if it.tags.find(tag)>=0]
    return render_template("main/query_item_by_tag.html",items=res,active_item=id,tag=tag)