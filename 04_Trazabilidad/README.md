# Trazabilidad y priorización — SICST Entrega Final 2B

Esta carpeta contiene los artefactos vigentes de trazabilidad y la priorización
del proyecto **Sistema Inteligente de Control y Seguimiento de Terapia Física
(SICST)** para la Entrega Final 2B.

## Archivos principales

- `Matriz_Trazabilidad_Final.csv` — **fuente canónica de trazabilidad vigente**.
- `priorizacion_moscow_kano.csv` — consolidación de priorización. La columna
  `MoSCoW_PE5` se mantiene sincronizada con la matriz final; las columnas
  `Kano_2A`, `Valor_Negocio_2A`, `Urgencia_2A`, `Riesgo_2A`, `Esfuerzo_2A`
  y `WSJF_2A` conservan la evaluación histórica realizada en 2A.

## Matriz de trazabilidad final

La matriz vigente contiene **62 trazas documentales**:

- 33 requisitos funcionales;
- 15 requisitos no funcionales generales;
- 12 requisitos no funcionales específicos de IA;
- 2 restricciones trazadas.

Las 62 trazas se encuentran registradas con `Estado_Traza = Completa`.

La matriz utiliza los siguientes campos:

- `ID_Traza`
- `Fuente`
- `Requisito`
- `Caso_Uso`
- `Clase_UML`
- `Proceso_DFD`
- `Estado`
- `Historia_Usuario`
- `BDD`
- `Caso_Prueba`
- `Prioridad`
- `Estado_Traza`

La cadena principal de auditoría es:

**Fuente → Requisito → Caso de uso → Clase UML → Proceso DFD → Estado → Historia de usuario → BDD → Caso de prueba**

La matriz conserva además la prioridad y el estado de cada traza para facilitar
la revisión de cobertura y consistencia.

## Requisitos funcionales

La matriz incorpora los **33 requisitos funcionales (RF-01 a RF-33)** de la
línea base del proyecto.

Para los RF se mantiene la relación con las fuentes de elicitación y, cuando
corresponde, con:

- caso de uso;
- clase UML;
- proceso DFD;
- estado del sistema;
- historia de usuario;
- escenario BDD;
- caso de prueba conceptual;
- prioridad MoSCoW.

RF-33 fue incorporado posteriormente mediante el proceso de control de cambios.
Cuando no existe una medición histórica válida de Kano/WSJF, los campos se
mantienen vacíos en lugar de inventar valores.

## Requisitos no funcionales generales

La matriz incluye **15 requisitos no funcionales generales (RNF-01 a RNF-15)**,
trazados con sus respectivas fuentes y elementos de verificación.

## Requisitos no funcionales de IA

La matriz contiene **12 requisitos no funcionales específicos de IA**:

- `RNF-IA1-P01`
- `RNF-IA1-P02`
- `RNF-IA1-P03`
- `RNF-IA1-EQ01`
- `RNF-IA1-EQ02`
- `RNF-IA1-XAI01`
- `RNF-IA2-P01`
- `RNF-IA2-P02`
- `RNF-IA2-P03`
- `RNF-IA2-EQ01`
- `RNF-IA2-EQ02`
- `RNF-IA2-XAI01`

Estos requisitos se encuentran definidos en:

`01_ERS/componentes_IA/requisitos_no_funcionales_ia.csv`

y trazados también en el ERS/SRS vigente.

Los RNF-IA cubren aspectos de:

- rendimiento;
- equidad;
- explicabilidad;
- supervisión humana;
- monitoreo;
- manejo de fallos;
- verificación;
- nivel de riesgo.

## Restricciones trazadas

La matriz incorpora además dos restricciones:

- `RES-02`
- `RES-15`

Estas restricciones forman parte de las **62 trazas totales** y se conservan
separadas de los RF y RNF para mantener clara su naturaleza.

## Priorización

`priorizacion_moscow_kano.csv` evita mezclar decisiones históricas con la línea
base actual:

- `MoSCoW_PE5` refleja la prioridad utilizada en la matriz final.
- Los campos terminados en `_2A` corresponden a información histórica y no se
  reinterpretan como una nueva medición.
- Cuando no existe una evaluación histórica válida, el valor se deja vacío en
  lugar de crear información retrospectiva.

## Integridad académica

Para mantener la trazabilidad verificable:

- no se crean fuentes de elicitación inexistentes;
- no se completan valores históricos con estimaciones posteriores;
- no se eliminan aportes o decisiones históricas necesarias para comprender la
  evolución del proyecto;
- los requisitos de IA se mantienen vinculados con su especificación canónica
  en `01_ERS/componentes_IA/`;
- cualquier modificación futura de la matriz debe conservar la correspondencia
  con el ERS/SRS y con los casos de prueba relacionados.

## Fuente oficial

Ante cualquier discrepancia sobre la trazabilidad vigente de la Entrega Final
2B, prevalece:

`04_Trazabilidad/Matriz_Trazabilidad_Final.csv`

La priorización complementaria se consulta en:

`04_Trazabilidad/priorizacion_moscow_kano.csv`

La carpeta `PE5_Informe_Final/` y las referencias históricas a PE5 se conservan
como antecedentes del proceso, pero no sustituyen la matriz consolidada vigente
de la Entrega Final 2B.
