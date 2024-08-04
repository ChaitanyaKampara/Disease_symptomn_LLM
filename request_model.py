from pydantic import BaseModel
from typing import Optional, List

class SymptomSearch(BaseModel):
    search_text: str
    input_symptoms: Optional[List[str]]
    input_diagnoses: Optional[List[str]]
    n_diseases: Optional[int] = 3
    n_symptoms: Optional[int] = 3
    min_symptoms: Optional[int] = 3

class MedicationSearch(BaseModel):
    selected_diagnoses: Optional[List[str]]
    n_medications: Optional[int] = 3