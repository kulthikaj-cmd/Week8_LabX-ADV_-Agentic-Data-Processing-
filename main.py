from pathlib import Path
from src.config_parser import ConfigParser
from src.data_agent import DataAgent
from src.utils import ensure_directory_exists
def main():
    root=Path(__file__).resolve().parent
    for folder in ("data","configs","reports"): ensure_directory_exists(root/folder)
    config=ConfigParser(root/"configs"/"data_pipeline_config.json").load_config()
    DataAgent(config,root).run()
if __name__=="__main__": main()
