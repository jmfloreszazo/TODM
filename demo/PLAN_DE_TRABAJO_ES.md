# TODM — Plan de implementación y validación

Estado a 27 de octubre de 2026. Los puntos marcados se refieren a **prototipos y comprobaciones locales**; no equivalen a una implantación industrial.

## H0 — Primer motor de oráculos

- [x] Contratos versionados para cinco familias de oráculos.
- [x] Candidato C#/.NET 10 con defectos deliberados.
- [x] Evaluador Python ejecutable y resultados reproducibles.
- [x] Detección de cuatro mutaciones y bloqueo de evidencia incompleta.
- [x] Verificación de integridad de modelos mediante SHA-256.
- [ ] Compilación local del motor .NET 10 (SDK no disponible en este entorno).

## H1 — Separación entre gobierno y corrección (v0.2)

- [x] Mandatos sintéticos con principal, alcance, acción, vigencia y revocación.
- [x] Control independiente del comportamiento y de la autorización.
- [x] Gate G6: bloquear si falla un control o no existe autorización de entrega.
- [x] Dieciséis escenarios reproducibles en greenfield, brownfield y AMS.
- [x] Trazabilidad de G0 a G7 y rutas de retorno para FAIL e INCONCLUSIVE.
- [x] Nueve pruebas Python y un panel HTML offline interactivo.
- [x] Código C# para el plano de gobierno y workflow GitHub Actions.
- [ ] Ejecutar GitHub Actions con .NET 10 y confirmar paridad de los dos evaluadores.

## H2 — Próximo objetivo: autoridad real y evidencias protegidas

- [ ] Repositorio de contratos protegido, con aprobación humana verificable (G2).
- [ ] Firmas y atestaciones para el baseline y las evidencias.
- [ ] Integración con identidades reales y mandatos revocables.
- [ ] G6 no eludible mediante protección de ramas y entornos de despliegue.
- [ ] Registro de auditoría y correlación de artefactos por versión/hash.

## H3 — Interpretación de modelos más profunda

- [ ] Adaptadores con subconjuntos documentados de BPMN 2.0, DMN y CMMN.
- [ ] Invariantes tipados OCL y glosario SBVR con revisión humana.
- [ ] Arqueología de código y trazas de un sistema brownfield real.
- [ ] Ontología Bolt-Genome opcional para análisis de impacto, sin poder de aprobación.

## H4 — Evaluación científica

- [ ] Registrar hipótesis y protocolo de comparación.
- [ ] Casos desconocidos por los constructores y oráculos; adjudicación independiente.
- [ ] Controles correctos, defectos sembrados, falsos positivos e inconclusos.
- [ ] Comparación por proyecto con enfoques SDD/TDD/BDD y desarrollo asistido por agentes.
- [ ] Publicar datos, scripts, intervalos de confianza y resultados negativos.

**Regla de avance:** no presentar H2 como terminado hasta verificar la identidad, la autorización humana y la imposibilidad de eludir G6; no presentar H4 como terminado por superar pruebas sintéticas.

## Entrega v0.3 — Integridad criptográfica reproducible
- [x] Aprobación sintética G2 firmada mediante Ed25519
- [x] Autorización G6 sintética firmada, vinculada a caso y contrato
- [x] Diez pruebas adversariales de integridad, suplantación por alteración y reutilización
- [x] Protocolo experimental prerregistrable, sin métricas de costes
- [ ] Identidad humana real, integración Entra/OIDC y enforcement en pipeline protegido
- [ ] Intérpretes OMG conformes y experimentación industrial
