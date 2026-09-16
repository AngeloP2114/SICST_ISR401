# Registro previo OSF — experimento SICST

## Identificación

- **Registro:** https://osf.io/82q76/
- **DOI:** `10.17605/OSF.IO/82Q76`
- **ID:** `82q76`
- **Fecha UTC:** `2026-09-13T00:50:38.265668Z`
- **Hora Ecuador continental (UTC-5):** `2026-09-12 19:50:38`

## Evidencia de esta carpeta

- `consulta.json` — respuesta guardada de la API pública de OSF para el
  registro `82q76`.
- `osf_registration.pdf` — exportación legible de la página del registro.

## Alcance temporal

Las entrevistas del SICST fueron realizadas previamente como parte de la
elicitación de requisitos.

El preregistro corresponde específicamente al **experimento comparativo
humano-LLM**. Esa fase utiliza las transcripciones anonimizadas existentes
como corpus fuente fijo.

La marca temporal del registro precede a la generación documentada del
conjunto LLM y a la recolección de las puntuaciones de la evaluación ciega
utilizadas en el análisis.

Por ello, esta documentación no afirma que el preregistro sea anterior a la
existencia de las entrevistas originales.

## Verificación de `consulta.json`

Desde la raíz del repositorio:

```bash
python -m json.tool 06_Experimento/registro_previo/consulta.json > /dev/null
```

Para consultar nuevamente la API pública:

```bash
curl -sS https://api.osf.io/v2/registrations/82q76/
```
