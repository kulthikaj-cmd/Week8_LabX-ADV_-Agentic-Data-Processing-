def csv_to_json(rows):
    converted=[]
    for row in rows:
        item={}
        for key,value in row.items():
            try: item[key]=int(value)
            except (ValueError,TypeError):
                try: item[key]=float(value)
                except (ValueError,TypeError): item[key]=value
        converted.append(item)
    return converted
