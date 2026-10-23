import csv
from pathlib import Path
def load_csv(path):
    with open(path,newline="",encoding="utf-8-sig") as f: return list(csv.DictReader(f))
def aggregate(rows, group_by_field, aggregate_field, aggregate_type="sum"):
    groups={}
    for row in rows:
        key=row[group_by_field]
        try: value=float(row[aggregate_field])
        except (ValueError,TypeError): value=0
        groups.setdefault(key,[]).append(value)
    result=[]
    for key, vals in groups.items():
        if aggregate_type=="count": total=len(vals)
        elif aggregate_type=="average": total=sum(vals)/len(vals) if vals else 0
        else: total=sum(vals)
        result.append({group_by_field:key,"Total_Amount":round(total,2)})
    return result
def save_csv(rows,path,fieldnames):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    with open(path,"w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=fieldnames); writer.writeheader(); writer.writerows(rows)
