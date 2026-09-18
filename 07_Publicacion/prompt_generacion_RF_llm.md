# Registro de uso de LLM — Generación de RF para comparación humano vs LLM

> Instrucciones: llenar cada campo con el dato REAL de la sesión donde
> generaron `requisitos_llm.csv`. Si usaron más de un turno de conversación
> para llegar a los 33 requisitos finales, documenten cada turno relevante
> por separado (turno 1, turno 2, ...). No se completa con datos aproximados
> o "reconstruidos de memoria" si se puede recuperar el dato real desde el
> historial de la conversación.

## Metadatos de la sesión

| Campo | Valor |
|---|---|
| Modelo | GPT-5.5-mini |
| Proveedor / interfaz | ChatGPT (chat.openai.com) |
| Fecha y hora de la consulta | 2026-09-12, en el transcurso del día, antes de las 13:11 hora Ecuador (hora exacta no registrada; se acota por los metadatos de las hojas de evaluación ciega, guardadas entre 13:11-13:16 ese mismo día, lo que requiere que el conjunto LLM ya existiera para ese momento). **Corrección del 18/09/2026: una versión anterior de esta ficha indicaba erróneamente "2026-09-13, madrugada, posterior al registro OSF"; esa fecha era incorrecta.** |
| Temperatura (si se conoce/configuró) | No aplica / no configurado (interfaz web de ChatGPT sin ajustes de API) |
| Top-p (si se conoce) | No aplica / no configurado (interfaz web) |
| Semilla (si aplica) | No aplica (interfaz de chat) |
| Número de turnos usados | 2 (turno 1: instrucción + 18 transcripciones de entrevista, generó el CSV; turno 2: se le pidió que confirmara la versión del modelo, que no incluyó en la primera respuesta) |
| Persona que ejecutó la consulta | Zambrano Moya Angelo Paul |

## Prompt(s) exacto(s) usado(s)

### Turno 1 — Instrucción y transcripciones

```
REGLAS ESTRICTAS: 1. Basa cada RF ÚNICAMENTE en lo que está explícitamente
dicho en las transcripciones que te voy a pegar a continuación. No inventes
funcionalidades ni agregues buenas prácticas que no se mencionen. 2. Usa
exactamente este formato de redacción para cada RF: "El sistema deberá
[acción verificable] [objeto/condición]." 3. Cada RF debe ser: específico,
verificable (se puede comprobar si se cumple o no) y trazable a un fragmento
concreto de la transcripción. 4. No generes RF duplicados ni RF que se
superpongan sin aportar nada distinto entre sí. 5. Numera cada RF como RF-01,
RF-02, etc. 6. Entrega el resultado en formato CSV con columnas:
id_requisito,descripcion 7. No agregues explicaciones antes o después del
CSV, solo el CSV. Al final de tu respuesta, indica: el nombre y versión del
modelo que eres, y confirma que no usaste información externa a las
transcripciones proporcionadas. A continuación están las transcripciones
anonimizadas: [se adjuntaron las 18 transcripciones de entrevista listadas
en la sección "Insumos que se le dieron al LLM" más abajo]
```

**Respuesta completa del LLM:**

La respuesta del modelo fue el CSV completo con los 33 requisitos, guardado
sin modificaciones como `datos_crudos/requisitos_llm.csv` en este mismo
repositorio — el contenido de ese archivo es exactamente lo que devolvió el
modelo en este turno.

### Turno 2 — Solicitud de confirmación de versión del modelo

```
[Se le pidió que indicara la versión del modelo utilizada y confirmara que
no usó información externa a las transcripciones proporcionadas, ya que no
lo había incluido en la respuesta del turno 1]
```

**Respuesta:**

```
Modelo: GPT-5.5-mini.
Confirmo que no utilicé información externa a las transcripciones
proporcionadas. Las entrevistas contienen información sobre diagnóstico,
antecedentes, dolor, seguimiento, ejercicios, cumplimiento, evolución y
comunicación terapéutica, por ejemplo en las respuestas de fisioterapeutas y
familiares sobre datos necesarios antes y durante la terapia.
```

## Insumos que se le dieron al LLM

18 transcripciones anonimizadas de las sesiones de entrevista de elicitación
con fisioterapeutas, familiares y pacientes (no se incluyeron las
transcripciones de walkthrough de validación, que corresponden a una etapa
distinta del estudio). Se usaron 19 archivos que corresponden a 18
entrevistas reales, porque la entrevista `WALK-TEC-01` está dividida en dos
archivos (Parte 1 y Parte 2). Archivos exactos usados, de
`02_Evidencias/Transcripciones/`:

1. TRANSCRIPCIONES_FIS-01_Entrevista.txt
2. TRANSCRIPCIONES_FAM-04_Entrevista.txt
3. TRANSCRIPCIONES_FAM-03_Entrevista.txt
4. TRANSCRIPCIONES_FAM-02_Entrevista.txt
5. TRANSCRIPCIONES_FAM-01_Entrevista.txt
6. TRANSCRIPCIONES_EFT-03_Entrevista.txt
7. TRANSCRIPCIONES_EFT-02_Entrevista.txt
8. TRANSCRIPCIONES_EFT-01_Entrevista.txt
9. TRANSCRIPCIONES_WALK-NTEC-01_Entrevista.txt
10. TRANSCRIPCIONES_WALK-TEC-01_Entrevista.txt (Parte 1)
11. TRANSCRIPCIONES_WALK-TEC-01_Entrevista_Parte2.txt (Parte 2 — misma entrevista)
12. TRANSCRIPCIONES_EV2-PAC-09_Entrevista.txt
13. TRANSCRIPCIONES_EV2-PAC-08_Entrevista.txt
14. TRANSCRIPCIONES_EV2-PAC-07_Entrevista.txt
15. TRANSCRIPCIONES_EV2-PAC-06_Entrevista.txt
16. TRANSCRIPCIONES_EV2-PAC-05_Entrevista.txt
17. TRANSCRIPCIONES_EV2-PAC-04_Entrevista.txt
18. TRANSCRIPCIONES_EV2-PAC-03_Entrevista.txt
19. TRANSCRIPCIONES_EV2-PAC-01_Entrevista.txt

## Postprocesamiento manual aplicado

Ninguno — el CSV devuelto por el modelo se guardó tal cual, sin
modificaciones, como `requisitos_llm.csv`.
