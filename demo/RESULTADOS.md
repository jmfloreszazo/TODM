# TODM v0.2 — resultados reproducibles del prototipo

**Verificado localmente:** Python 3 (biblioteca estándar), con `python3 scripts/verify_all.py`.

- 5/5 controles correctos: PASS.
- 4/4 mutaciones deliberadas: FAIL.
- 1/1 casos de evidencia incompleta: INCONCLUSIVE.
- 16 casos de gobierno en dos planos: 11 PASS del oráculo, 4 FAIL, 1 INCONCLUSIVE.
- 5 mandatos denegados; 5 autorizaciones de entrega simuladas y 11 bloqueos.
- 9 pruebas de cualificación Python completadas.
- Alterar un modelo sin actualizar su hash produce error de integridad.
- Alterar el manifiesto local **no se detecta criptográficamente**: falta firma/almacén protegido.

Los números describen los casos de prueba diseñados, no sensibilidad, precisión ni eficacia en proyectos reales. **.NET 10 y paridad C#/Python pendientes de ejecución en un entorno con SDK.**

**Prueba clave:** `GF-05-revoked-agent` tiene resultado de software correcto (TODM PASS) y autoridad revocada (mandato FAIL), por lo que G6 bloquea. `GF-03-wrong-threshold` invierte la situación: mandato PASS y TODM FAIL. `GF-08-unapproved-release` tiene ambos PASS, pero G6 deniega por falta de autorización de entrega.
