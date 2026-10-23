import json, logging
from datetime import datetime
from pathlib import Path
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
def ensure_directory_exists(path):
    Path(path).mkdir(parents=True, exist_ok=True)
def log_audit_entry(entries, status, message, task_type="N/A", details=None):
    entries.append({"timestamp":datetime.now().isoformat(timespec="seconds"),"status":status,
                    "task_type":task_type,"message":message,"details":details or {}})
def save_audit(entries, directory):
    ensure_directory_exists(directory)
    path=Path(directory)/("audit_report_"+datetime.now().strftime("%Y%m%d_%H%M%S")+".json")
    path.write_text(json.dumps(entries,indent=2),encoding="utf-8")
    return path
