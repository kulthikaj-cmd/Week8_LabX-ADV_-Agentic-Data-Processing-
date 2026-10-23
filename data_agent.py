from pathlib import Path
from .csv_tasks import load_csv, aggregate, save_csv
from .json_tasks import load_json, update_json, query_json, save_json
from .conversion_tasks import csv_to_json
from .utils import log_audit_entry, save_audit
class DataAgent:
    def __init__(self, config, base_dir):
        self.config=config; self.base_dir=Path(base_dir); self.data_store={}; self.audit=[]
    def path(self, value):
        p=Path(value); return p if p.is_absolute() else self.base_dir/p
    def run(self):
        handlers={
          "load_csv":lambda t: load_csv(self.path(t["file_path"])),
          "transform_csv_aggregate":lambda t: aggregate(self.data_store[t["input_data_key"]],t["group_by_field"],t["aggregate_field"],t.get("aggregate_type","sum")),
          "save_csv":lambda t: save_csv(self.data_store[t["input_data_key"]],self.path(t["file_path"]),t["fieldnames"]),
          "csv_to_json_conversion":lambda t: csv_to_json(self.data_store[t["input_data_key"]]),
          "load_json":lambda t: load_json(self.path(t["file_path"])),
          "update_json_data":lambda t: update_json(self.data_store[t["input_data_key"]],t["updates"]),
          "query_json_data":lambda t: query_json(self.data_store[t["input_data_key"]],t["path"]),
          "save_json":lambda t: save_json(self.data_store[t["input_data_key"]],self.path(t["file_path"]),t.get("indent",2))}
        for task in self.config["tasks"]:
            try:
                result=handlers[task["type"]](task)
                if task.get("output_data_key"): self.data_store[task["output_data_key"]]=result
                log_audit_entry(self.audit,"SUCCESS",task["name"],task["type"])
                print("SUCCESS:",task["name"])
            except Exception as e:
                log_audit_entry(self.audit,"ERROR",task["name"],task.get("type","N/A"),{"error":str(e)})
                save_audit(self.audit,self.base_dir/"reports")
                raise
        report=save_audit(self.audit,self.base_dir/"reports")
        print("Audit report:",report)
        return self.data_store
