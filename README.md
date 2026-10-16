# US Visa Approval Prediction — End-to-end MLOps pipeline

Predicts whether a US work-visa application will be **certified or denied** from employer and applicant features (EasyVisa dataset). The goal of the project is not just a model in a notebook, but a **modular, production-style ML pipeline**: MongoDB ingestion, schema validation, data-drift checks, training, evaluation and model push to S3, served through FastAPI.

> 🚧 **Status: work in progress.** Research notebooks and the first two pipeline stages are complete; the remaining stages are being moved from notebooks into the pipeline. See the progress table below.

## 📊 Progress

| Stage | Where | Status |
|---|---|---|
| EDA | [`notebook/1_EDA_US_visa.ipynb`](notebook/1_EDA_US_visa.ipynb) | ✅ Done |
| Feature engineering & model training | [`notebook/2_Feature_Engineering_and_Model_Training.ipynb`](notebook/2_Feature_Engineering_and_Model_Training.ipynb) | ✅ Done (notebook) |
| Data-drift report (Evidently) | [`notebook/data_drift_demo_evidently.ipynb`](notebook/data_drift_demo_evidently.ipynb) | ✅ Done |
| Data ingestion (MongoDB → feature store → train/test) | [`US_VISA/components/data_ingestion.py`](US_VISA/components/data_ingestion.py) | ✅ Done |
| Data validation (schema + drift) | [`US_VISA/components/data_validation.py`](US_VISA/components/data_validation.py) | ✅ Done |
| Data transformation | `US_VISA/components/data_tranforomation.py` | 🔜 Next |
| Model trainer / evaluation / pusher (S3) | `US_VISA/components/` | 🔜 Planned |
| FastAPI app + Docker + CI/CD to AWS | `app.py`, `Dockerfile` | 🔜 Planned |

## 🏗️ Pipeline design

```mermaid
flowchart LR
    M[(MongoDB)] --> I[Data Ingestion]
    I --> V[Data Validation<br/>schema + Evidently drift]
    V --> T[Data Transformation]
    T --> TR[Model Trainer]
    TR --> E[Model Evaluation]
    E --> P[Model Pusher → S3]
    P --> API[FastAPI prediction app]
```

Each stage produces a typed **artifact** (`US_VISA/entity`) consumed by the next, with config entities, custom exceptions and central logging — the structure used in production ML teams.

## 📁 Project structure

```
US_VISA/
├── components/        # pipeline stages
├── configurations/    # MongoDB / AWS connections
├── contants/          # constants
├── data_access/       # MongoDB → DataFrame
├── entity/            # config & artifact dataclasses
├── exceptions/        # custom exception
├── logger/            # logging setup
├── pipeline/          # training / prediction pipelines
└── utils/
notebook/              # EDA, training, drift experiments
config/                # schema.yaml etc.
```

## 🛠️ Tech stack

Python · pandas · scikit-learn · XGBoost · CatBoost · imbalanced-learn · Evidently · MongoDB · AWS S3 (boto3) · FastAPI

## 🚀 Run locally

```bash
git clone https://github.com/AhmadMughal-DS/US-VISA-Approval-Prediction.git
cd US-VISA-Approval-Prediction
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export MONGODB_URL="<your-mongodb-connection-string>"
python demo.py
```

## 👤 Author

**Muhammad Ahmad** — DevOps & Cloud Engineer · [GitHub](https://github.com/AhmadMughal-DS) · [LinkedIn](https://www.linkedin.com/in/ahmadai)
