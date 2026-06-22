# Encounter-Driven Clinic Management REST API

## Project Overview
This project is a Django-based REST API for a health clinic. It manages:
- Patient registration
- Appointment booking and completion
- Clinical workflow (medical records and prescriptions)
- Billing and insurance claims

The API is implemented with a **Thin Views / Fat Managers** architecture. Views only parse HTTP/JSON and return `JsonResponse`, while business rules live in `ClinicManager`.

## Technical Stack
- **Backend Framework:** Django
- **Database:** SQLite
- **Architecture Pattern:** Service Layer (`ClinicManager`)
- **API Style:** Function-based Django views with JSON-only responses

## UML Alignment (Encounter-Driven Architecture)
The implementation follows an encounter-driven model where `Appointment` is the operational hub:
- `Appointment` aggregates:
  - `Bill` (one-to-one)
  - `MedicalRecord` (one-to-one)
  - `Prescription` (one-to-many)
- `Bill` aggregates:
  - `InsuranceClaim` (one-to-one)
- `Patient` composes:
  - `InsurancePolicy` (one-to-one)
- `InsurancePolicy` references:
  - `InsuranceProvider` (many-to-one)

This ensures billing and clinical artifacts are generated from clinical encounters, not attached directly as independent records on `Patient`.

## Downloading from GitHub
To get a copy of this project on your local machine, you will first need to clone the repository using Git.

1. **Clone the repository:**
   Open your terminal and run the following command to download the code:
   ```bash
   git clone [https://github.com/alibsrv/BIM.git](https://github.com/alibsrv/BIM.git)
