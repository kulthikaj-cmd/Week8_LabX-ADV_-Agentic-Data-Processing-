# Agentic Data Processor — Week 8 LabX ADV

Configuration-driven CSV and JSON processing workflow built with Python's standard library.

## Run
```bash
python main.py
```
No third-party packages are required. Run from the repository root.

## Workflow
- Load `data/input_sales.csv`.
- Aggregate sales by customer and write `data/processed_sales_by_customer.csv`.
- Convert raw sales rows to `data/sales_data.json`.
- Update inventory stock/details, add PROD004, query a nested brand, and save `data/updated_inventory.json`.
- Write an audit log under `reports/`.

## Repository layout
- `src/` — task handlers, agent orchestration, config parser, utilities
- `configs/data_pipeline_config.json` — declarative task sequence
- `data/` — inputs and generated outputs
- `screenshots/` — output-file screenshots included for submission

## Output screenshots
Open `screenshots/` to view the three generated output previews. These images are also committed with the project so the submission contains the requested evidence.
