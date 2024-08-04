from fastapi import APIRouter, HTTPException
# APIRouter : helps in defining routes for the API
# HTTPException : used to raise exceptions with appropriate HTTP status codes
from src.services.services import get_diseases_from_symptoms, get_medications_predictions
from src.dto.request_model import SymptomSearch, MedicationSearch

router = APIRouter()


@router.get('/')    # decorater
async def health_check():
    return {"status": "OK"}


@router.post("/search")
async def search(request_data: SymptomSearch):
    try:
        # unpack data from request body
        search_text = request_data.search_text
        symptoms_list = request_data.input_symptoms
        diagnoses_list = request_data.input_diagnoses
        n_diseases = request_data.n_diseases
        n_symptoms = request_data.n_symptoms
        min_symptoms = request_data.min_symptoms
        search_output = await get_diseases_from_symptoms(
            search_text=search_text,
            selected_symptoms=symptoms_list,
            selected_diagnoses=diagnoses_list,
            n_diseases=n_diseases, n_symptoms=n_symptoms,
            min_symptoms=min_symptoms)
        return search_output
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/medications')
async def fetch_medications_predictions(request_data: MedicationSearch):
    try:
        # unpack data from request body
        selected_diagnoses = request_data.selected_diagnoses
        n_medications = request_data.n_medications
        return await get_medications_predictions(selected_diagnoses, n_medications)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
