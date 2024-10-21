# app/schemas/ai_module.py

from __future__ import annotations
from pydantic import BaseModel
from typing import Any, Dict

class IARequest(BaseModel):
    data: Dict[str, Any]

class IAResponse(BaseModel):
    result: Any
