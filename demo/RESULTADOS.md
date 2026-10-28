# TODM v1.4 — resultados reproducibles del prototipo (casos históricos v0.2/v0.4)

**Versión de publicación 1.4.0.** Los recuentos originales son sintéticos y proceden de casos históricos; la compilación .NET y la paridad se verifican por GitHub Actions.

**Verificado localmente:** Python 3 (biblioteca estándar), con `python3 scripts/verify_all.py`.

- 5/5 controles correctos: PASS.
- 4/4 mutaciones deliberadas: FAIL.
- 1/1 casos de evidencia incompleta: INCONCLUSIVE.
- 16 casos de gobierno en dos planos: 11 PASS del oráculo, 4 FAIL, 1 INCONCLUSIVE.
- 5 mandatos denegados; 5 autorizaciones de entrega simuladas y 11 bloqueos.
- 9 pruebas de cualificación Python completadas.
- Alterar un modelo sin actualizar su hash produce error de integridad.
- Alterar el manifiesto local **no se detecta criptográficamente**: falta firma/almacén protegido.

Los números describen los casos de prueba diseñados, no sensibilidad, precisión ni eficacia en proyectos reales. **Actualización de verificación (28/10/2026):** .NET 10 y la paridad C#/Python de los 16 escenarios y las cinco familias ya se ejecutaron satisfactoriamente en [GitHub Actions](https://github.com/jmfloreszazo/TODM/actions/runs/40650709906). El resto de resultados sigue siendo exclusivamente sintético.

**Prueba clave:** `GF-05-revoked-agent` tiene resultado de software correcto (TODM PASS) y autoridad revocada (mandato FAIL), por lo que G6 bloquea. `GF-03-wrong-threshold` invierte la situación: mandato PASS y TODM FAIL. `GF-08-unapproved-release` tiene ambos PASS, pero G6 deniega por falta de autorización de entrega.
