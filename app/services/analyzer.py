import sys
import uuid
from pathlib import Path

from schemas import *
from datetime import datetime



#TODO: Get model output
def analyze_clinical_text(text: str):
    return analyze_placeholder(text)

'''
Return Dummy AnalysisResponse object
'''
def analyze_placeholder(text: str):
    return AnalysisResponse(**{
        "metadata": Metadata(
            request_id=str(uuid.uuid4()),
            timestamp=datetime.now(),
            model_name="Clinical Note Analyzer LLM Placeholder",
            processing_time_ms=12.5,
            schema_version="0.1"),
        "summary": Summary(
            author="Dr. Foo",
            subject="J. Bar",
            brief=text[:len(text) // 2]
        ),
        "entities": ClinicalEntities(
            symptoms=[Symptom(name="headache", severity="moderate", status="ongoing", certainty="likely"), Symptom(name="nausea", severity="mild", status="went away", certainty="unsure")],
            medications=[Medication(name="Med I", dose="250mg", frequency="daily"), Medication(name="Med II", dose="450ug", frequency="twice daily")],
            conditions=[Condition(name="diabetes", diagnosis_date="Jan 2020", status="controlled"), Condition(name="ADHD", diagnosis_date="Mar 2010", status="controlled")],
            procedures=[Procedure(name="kidney transplant", date="Oct 2017")],
            laboratory_values=[LaboratoryValue(name="WBC", value="8.5"),LaboratoryValue(name="RBC", value="5.2"), LaboratoryValue(name="Hgb", value="166"), LaboratoryValue(name="sodium", value="140 mmol/L"), LaboratoryValue(name="cholesterol", value="3.6 mmol/L"), LaboratoryValue(name="glucose", value="4.8 mmol/L")],
            allergies=[Allergy(name="eggs", severity="high"), Allergy(name="pollen", severity="moderate")],
            lifestyle_factors=[LifestyleFactor(name="smoker", status="frequent"), LifestyleFactor(name="athletic", status="regular")],
        ),
        "temporal_information": TemporalInformation(
            onset=" 2 weeks ago",
            duration="ongoing",
            progression="stable",
            timeline_events=[],
        ),
        "observations": [],
        "uncertainty": Uncertainty(
            missing_information=["lorem ipsum dolor sit amet", "foo", "bar"],
            ambiguous_terms=["Term1", "Term2", "Term3", "Term4", "Term5"]
        ),
        "raw_text": text
    })