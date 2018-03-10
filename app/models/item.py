class Item(object):
    def __init__(self,uni_id,title="new item",status="ready",description=None,tags=None,updatetime=None):
        self.uni_id=uni_id
        self.title=title
        self.status=status
        self.description=description
        self.tags=tags
        self.updatetime=updatetime