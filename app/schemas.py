from  datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict


class StrictBaseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class PresenceStatus(str, Enum):
    PRESENT = "present"
    ABSENT = "absent"
    UNKNOWN = "unknown"

class Certainty(str, Enum):
    CONFIRMED = "confirmed"
    SUSPECTED = "suspected"
    NEGATED = "negated"
    UNKNOWN = "unknown"

class Metadata(StrictBaseModel):
    request_id: str
    timestamp: str | datetime
    model_name: str
    processing_time_ms: float
    schema_version: str

class Summary(StrictBaseModel):
    author: str
    subject: str
    brief: str

class Symptom(StrictBaseModel):
    name: str
    severity: str | None = None
    duration: str | None = None
    status: PresenceStatus
    certainty: Certainty

class Medication(StrictBaseModel):
    name: str
    dose: str | None = None
    frequency: str | None = None

class Condition(StrictBaseModel):
    name: str
    status: PresenceStatus
    certainty: Certainty

class Allergy(StrictBaseModel):
    substance: str
    reaction: str | None = None

class Measurement(StrictBaseModel):
    name: str
    value: str
    unit: str | None = None

class Procedure(StrictBaseModel):
    name: str
    date: str

class LifestyleFactor(StrictBaseModel):
    name: str
    status: PresenceStatus

class TemporalInformation(StrictBaseModel):
    onset: str | None = None
    duration: str | None = None
    progression: str | None = None

# class Observation(StrictBaseModel):
#     finding: str
#     evidence: str
#     confidence: float

# class Uncertainty(StrictBaseModel):
#     missing_information: list[str]
#     ambiguous_terms: list[str]

class ClinicalEntities(StrictBaseModel):
    symptoms: list[Symptom]
    medications: list[Medication]
    conditions: list[Condition]
    procedures: list[Procedure]
    measurements: list[Measurement]
    allergies: list[Allergy]
    lifestyle_factors: list[LifestyleFactor]

class ExtractedClinicalData(StrictBaseModel):
    summary: Summary
    entities: ClinicalEntities
    temporal_information: TemporalInformation

class AnalysisResponse(BaseModel):
    metadata: Metadata
    extraction: ExtractedClinicalData
    raw_text: str

class AnalysisRequest(BaseModel):
    text: str