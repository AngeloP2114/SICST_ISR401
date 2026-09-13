# Anonymization procedure — SICST reproducible package

This document describes the anonymization and pseudonymization procedure
applied to all data included in this public, reproducible package, in
accordance with the FAIR principles and Ecuador's Ley Orgánica de
Protección de Datos Personales (LOPDP).

## General principle

No direct identifiers (full names, national ID numbers, phone numbers,
signatures, faces, or voices) are included in this public package. All
material containing direct identifiers is kept exclusively in the
project's encrypted restricted-access container
(`02_Evidencias/00_Restringido/`), never in the public repository or in
this Zenodo package.

## Questionnaire data (general project dataset, `07_Datos/`)

- The submission timestamp column was removed from the processed dataset
  to reduce unnecessary temporal information that could support indirect
  re-identification.
- Participant codes (e.g., `EV2-PAC-05`) are retained for internal
  academic traceability only; they do not encode any personal
  information and cannot be reversed to a real identity without access to
  the restricted, encrypted consent records.
- No name, phone number, or address field was ever collected in the
  questionnaire instrument.

## Interview transcripts used for the Enfoque 1 (human vs. LLM) experiment

- The 18 interview transcripts supplied to both the human elicitation
  process and the LLM (`06_Experimento/prompts_llm/`) were anonymized
  before use: participant names were replaced with role-based codes
  (e.g., `FIS-01` for a physiotherapist, `FAM-02` for a family
  caregiver, `EV2-PAC-05` for a patient).
- No transcript in this package contains a real name, national ID
  number, address, or contact information.

## Blind-evaluation dataset (`06_Experimento/datos_crudos/`)

- The 66 functional requirements evaluated by the four blind judges are
  identified only by an anonymized item code (`ITEM-001` to `ITEM-066`).
- The private key mapping each anonymized item to its real requirement
  ID and source (human/LLM), `clave_privada_desciego.csv`, is stored
  encrypted in `02_Evidencias/00_Restringido/` and is **not** part of
  this public package.
- The four evaluators are identified only by first name (Mishell, Angel,
  Dayana, Sebas) in the raw evaluation spreadsheets, at their own
  request as informal, non-expert volunteer raters; no other personal
  data about the evaluators is collected or published.

## Verification

Anyone auditing this package can confirm the absence of direct
identifiers by inspecting the public files directly: no file in
`06_Experimento/` or `07_Datos/` (outside the encrypted restricted
container) contains a full name, national ID number, signature image, or
unmasked contact information.
