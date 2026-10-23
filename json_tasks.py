import json
from pathlib import Path
def load_json(path):
    with open(path,encoding="utf-8") as f: return json.load(f)
def _parent_and_key(data,path):
    if path in ("",None): return None,None
    parts=path.split("."); cur=data
    for part in parts[:-1]: cur=cur[int(part)] if isinstance(cur,list) else cur[part]
    key=parts[-1]
    if isinstance(cur,list): key=int(key)
    return cur,key
def update_json(data,updates):
    for update in updates:
        path=update.get("path",""); op=update.get("operation","set"); value=update.get("value")
        if op=="add_to_list":
            if not isinstance(data,list): raise TypeError("add_to_list requires a list at root")
            data.append(value); continue
        parent,key=_parent_and_key(data,path)
        if op=="set":
            if isinstance(parent,dict): parent[key]=value
            elif isinstance(parent,list): parent[key]=value
            elif path=="": data=value
        elif op=="delete":
            if isinstance(parent,dict): parent.pop(key,None)
            elif isinstance(parent,list): parent.pop(key)
    return data
def query_json(data,path):
    cur=data
    for part in path.split("."): cur=cur[int(part)] if isinstance(cur,list) else cur[part]
    return cur
def save_json(data,path,indent=2):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    with open(path,"w",encoding="utf-8") as f: json.dump(data,f,indent=indent,ensure_ascii=False)
