from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Any, Dict, List, Optional

def ahora_iso() -> str:
  return  datetime.now().strftime("%Y-%m-%d %H:%M:%S")

