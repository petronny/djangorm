import os
from pathlib import Path
from djangorm import DjangORM
db = DjangORM(module_name=Path(__file__).parent.name)
db.configure()
db.migrate()
