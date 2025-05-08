# index_data.py
import os
import json
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID, KEYWORD
from whoosh.analysis import StemmingAnalyzer

# Advanced analyzer with stemming
analyzer = StemmingAnalyzer()

schema = Schema(
    disease=TEXT(stored=True),
    symptoms=KEYWORD(stored=True, analyzer=analyzer, scorable=True),
    description=TEXT(stored=True),
    synonyms=KEYWORD(stored=True, analyzer=analyzer),
    severity=ID(stored=True),
    treatment=TEXT(stored=True)
)

if not os.path.exists("indexdir"):
    os.mkdir("indexdir")

ix = create_in("indexdir", schema)
writer = ix.writer()

# Enhanced comprehensive disease dataset
diseases = [
    {
        "disease": "Common Cold",
        "symptoms": ["runny nose", "sneezing", "sore throat", "congestion", "cough", "slight fever"],
        "description": "Viral infection of the upper respiratory tract.",
        "synonyms": ["acute nasopharyngitis", "rhinopharyngitis", "head cold"],
        "severity": "mild",
        "treatment": "Rest, hydration, over-the-counter pain relievers, and decongestants."
    },
    {
        "disease": "Influenza",
        "symptoms": ["fever", "chills", "muscle aches", "cough", "fatigue", "headache", "sore throat"],
        "description": "Contagious respiratory illness caused by influenza viruses.",
        "synonyms": ["flu", "grippe", "seasonal flu"],
        "severity": "moderate",
        "treatment": "Antiviral medications, rest, fluids, and pain relievers."
    },
    {
        "disease": "COVID-19",
        "symptoms": ["fever", "dry cough", "fatigue", "shortness of breath", "loss of taste", "loss of smell"],
        "description": "Infectious disease caused by the SARS-CoV-2 virus.",
        "synonyms": ["coronavirus", "SARS-CoV-2 infection", "novel coronavirus"],
        "severity": "variable",
        "treatment": "Supportive care, antivirals, monoclonal antibodies for severe cases."
    },
    {
        "disease": "Migraine",
        "symptoms": ["severe headache", "nausea", "sensitivity to light", "sensitivity to sound", "visual disturbances"],
        "description": "Neurological condition characterized by intense, debilitating headaches.",
        "synonyms": ["migraine headache", "sick headache"],
        "severity": "moderate",
        "treatment": "Pain relievers, triptans, preventive medications, lifestyle changes."
    },
    {
        "disease": "Hypertension",
        "symptoms": ["headache", "shortness of breath", "nosebleeds", "flushing", "dizziness", "chest pain"],
        "description": "Medical condition characterized by abnormally high blood pressure.",
        "synonyms": ["high blood pressure", "arterial hypertension"],
        "severity": "serious",
        "treatment": "Lifestyle changes, diuretics, ACE inhibitors, ARBs, calcium channel blockers."
    },
    {
        "disease": "Type 2 Diabetes",
        "symptoms": ["increased thirst", "frequent urination", "increased hunger", "fatigue", "blurred vision", "slow-healing sores"],
        "description": "Chronic condition affecting how the body processes blood sugar.",
        "synonyms": ["diabetes mellitus type 2", "adult-onset diabetes"],
        "severity": "serious",
        "treatment": "Diet management, regular exercise, monitoring blood sugar, medications, insulin therapy."
    },
    {
        "disease": "Asthma",
        "symptoms": ["shortness of breath", "chest tightness", "coughing", "wheezing"],
        "description": "Chronic disease of the airways that causes inflammation and narrowing.",
        "synonyms": ["bronchial asthma", "reactive airway disease"],
        "severity": "moderate",
        "treatment": "Bronchodilators, inhaled corticosteroids, long-term control medications."
    },
    {
        "disease": "Gastroesophageal Reflux Disease",
        "symptoms": ["heartburn", "chest pain", "difficulty swallowing", "regurgitation", "sour taste"],
        "description": "Digestive disorder affecting the lower esophageal sphincter.",
        "synonyms": ["GERD", "acid reflux disease", "reflux esophagitis"],
        "severity": "moderate",
        "treatment": "Proton pump inhibitors, H2 blockers, antacids, lifestyle modifications."
    },
    {
        "disease": "Irritable Bowel Syndrome",
        "symptoms": ["abdominal pain", "cramping", "bloating", "gas", "diarrhea", "constipation"],
        "description": "Common disorder affecting the large intestine.",
        "synonyms": ["IBS", "spastic colon", "nervous colon"],
        "severity": "moderate",
        "treatment": "Dietary changes, stress management, medications for specific symptoms."
    },
    {
        "disease": "Osteoarthritis",
        "symptoms": ["joint pain", "stiffness", "tenderness", "loss of flexibility", "grating sensation", "bone spurs"],
        "description": "Degenerative joint disease affecting cartilage and bones.",
        "synonyms": ["degenerative arthritis", "wear and tear arthritis"],
        "severity": "moderate",
        "treatment": "Physical therapy, pain relievers, cortisone injections, lubrication injections."
    },
    {
        "disease": "Rheumatoid Arthritis",
        "symptoms": ["joint pain", "joint swelling", "joint stiffness", "fatigue", "fever", "loss of appetite"],
        "description": "Chronic inflammatory disorder affecting joints and other body systems.",
        "synonyms": ["RA", "atrophic arthritis"],
        "severity": "serious",
        "treatment": "NSAIDs, steroids, disease-modifying antirheumatic drugs (DMARDs), biologic agents."
    },
    {
        "disease": "Allergic Rhinitis",
        "symptoms": ["sneezing", "itchy nose", "runny nose", "congestion", "watery eyes"],
        "description": "Inflammation of the nasal passages due to allergens.",
        "synonyms": ["hay fever", "pollinosis", "seasonal allergies"],
        "severity": "mild",
        "treatment": "Antihistamines, decongestants, nasal corticosteroids, allergy shots."
    },
    {
        "disease": "Depression",
        "symptoms": ["persistent sadness", "loss of interest", "fatigue", "sleep problems", "appetite changes", "difficulty concentrating"],
        "description": "Mental health disorder characterized by persistently depressed mood.",
        "synonyms": ["major depressive disorder", "clinical depression"],
        "severity": "serious",
        "treatment": "Psychotherapy, antidepressant medications, lifestyle changes."
    },
    {
        "disease": "Anxiety Disorder",
        "symptoms": ["excessive worry", "restlessness", "fatigue", "difficulty concentrating", "irritability", "sleep problems", "muscle tension"],
        "description": "Mental health condition characterized by feelings of worry and fear.",
        "synonyms": ["generalized anxiety disorder", "anxiety neurosis"],
        "severity": "moderate",
        "treatment": "Psychotherapy, anti-anxiety medications, stress management techniques."
    },
    {
        "disease": "Urinary Tract Infection",
        "symptoms": ["burning sensation during urination", "frequent urination", "cloudy urine", "strong-smelling urine", "pelvic pain"],
        "description": "Infection in any part of the urinary system.",
        "synonyms": ["UTI", "bladder infection", "cystitis"],
        "severity": "mild",
        "treatment": "Antibiotics, pain relievers, increased fluid intake."
    },
    {
        "disease": "Conjunctivitis",
        "symptoms": ["red eyes", "itchy eyes", "gritty feeling", "discharge", "tearing", "crusting of eyelids"],
        "description": "Inflammation of the conjunctiva of the eye.",
        "synonyms": ["pink eye", "red eye"],
        "severity": "mild",
        "treatment": "Antibiotics for bacterial causes, antihistamines for allergic causes, artificial tears."
    },
    {
        "disease": "Strep Throat",
        "symptoms": ["severe sore throat", "pain when swallowing", "fever", "red and swollen tonsils", "tiny red spots on the roof of the mouth", "swollen lymph nodes"],
        "description": "Bacterial infection causing inflammation and pain in the throat.",
        "synonyms": ["streptococcal pharyngitis", "streptococcal tonsillitis"],
        "severity": "moderate",
        "treatment": "Antibiotics, pain relievers, rest, warm liquids."
    },
    {
        "disease": "Sinusitis",
        "symptoms": ["facial pain", "nasal congestion", "thick nasal discharge", "reduced sense of smell", "cough", "fatigue"],
        "description": "Inflammation of the tissue lining the sinuses.",
        "synonyms": ["sinus infection", "rhinosinusitis"],
        "severity": "moderate",
        "treatment": "Nasal corticosteroids, saline nasal irrigation, antibiotics if bacterial."
    },
    {
        "disease": "Bronchitis",
        "symptoms": ["cough", "mucus production", "fatigue", "shortness of breath", "slight fever", "chest discomfort"],
        "description": "Inflammation of the lining of the bronchial tubes.",
        "synonyms": ["chest cold", "acute bronchitis"],
        "severity": "moderate",
        "treatment": "Rest, hydration, humidified air, over-the-counter pain relievers."
    },
    {
        "disease": "Pneumonia",
        "symptoms": ["chest pain", "cough with phlegm", "fatigue", "fever", "shortness of breath", "nausea", "vomiting"],
        "description": "Infection that inflames air sacs in one or both lungs.",
        "synonyms": ["bronchopneumonia", "lobar pneumonia"],
        "severity": "serious",
        "treatment": "Antibiotics for bacterial pneumonia, cough medicine, pain relievers, rest."
    },
    {
        "disease": "Gastroenteritis",
        "symptoms": ["diarrhea", "nausea", "vomiting", "abdominal cramps", "low-grade fever", "muscle aches"],
        "description": "Inflammation of the stomach and intestines.",
        "synonyms": ["stomach flu", "intestinal flu", "food poisoning"],
        "severity": "moderate",
        "treatment": "Hydration, electrolyte replacement, rest, gradual reintroduction of food."
    },
    {
        "disease": "Tension Headache",
        "symptoms": ["dull head pain", "pressure around forehead", "tenderness in scalp", "neck pain", "shoulder pain"],
        "description": "Most common type of headache characterized by dull pain and pressure.",
        "synonyms": ["stress headache", "muscle contraction headache"],
        "severity": "mild",
        "treatment": "Over-the-counter pain relievers, relaxation techniques, stress management."
    },
    {
        "disease": "Insomnia",
        "symptoms": ["difficulty falling asleep", "waking up during the night", "waking up too early", "daytime tiredness", "irritability", "difficulty focusing"],
        "description": "Sleep disorder characterized by difficulty falling or staying asleep.",
        "synonyms": ["sleeplessness", "chronic insomnia"],
        "severity": "moderate",
        "treatment": "Sleep hygiene practices, cognitive behavioral therapy, short-term use of sleeping pills."
    },
    {
        "disease": "Dermatitis",
        "symptoms": ["red rash", "itching", "dry skin", "blisters", "swelling", "scaling"],
        "description": "Inflammation of the skin characterized by an itchy rash.",
        "synonyms": ["eczema", "contact dermatitis", "atopic dermatitis"],
        "severity": "mild",
        "treatment": "Corticosteroid creams, antihistamines, moisturizers, avoiding triggers."
    },
    {
        "disease": "Anemia",
        "symptoms": ["fatigue", "weakness", "pale skin", "shortness of breath", "dizziness", "cold hands and feet", "irregular heartbeat"],
        "description": "Condition marked by a deficiency of red blood cells or hemoglobin.",
        "synonyms": ["iron deficiency anemia", "pernicious anemia"],
        "severity": "moderate",
        "treatment": "Iron supplements, vitamin B-12 injections, dietary changes, treating underlying conditions."
    }
]

# Add all diseases to the index
for disease in diseases:
    writer.add_document(
        disease=disease["disease"],
        symptoms=" ".join(disease["symptoms"]),
        description=disease["description"],
        synonyms=" ".join(disease.get("synonyms", [])),
        severity=disease.get("severity", "unknown"),
        treatment=disease.get("treatment", "")
    )

writer.commit()
print("Indexing completed successfully with", len(diseases), "diseases!")