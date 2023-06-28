from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent.parent
DATA_PATH = Path.joinpath(ROOT_PATH, 'Data')
OPERATIONS_JSON_PATH = Path.joinpath(DATA_PATH, 'operations.json')
