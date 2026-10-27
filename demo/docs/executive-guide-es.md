# TODM explicado para dirección general

## Qué problema resuelve

Los agentes de IA pueden generar código, modificar servicios y proponer entregas. Que hayan terminado su tarea no significa que el resultado sea correcto; y que el resultado sea correcto no significa que el agente estuviera autorizado para actuar.

**TODM** separa quién construye del sistema que decide si lo construido cumple las reglas aprobadas. Un marco de gobierno como **CPAG** controla el mandato del agente: identidad, alcance, límites, vigencia y revocación. Ambos controles deben superar la comprobación de entrega.

## Ejemplo en 30 segundos

La regla del negocio exige revisión humana por encima de **10.000 €**. Un agente modifica el servicio y deja un umbral incorrecto de **12.000 €**. La solicitud de **11.000 €** se aprueba automáticamente. Sus propias pruebas podrían coincidir con el error, pero el oráculo de TODM, aprobado de forma independiente, detecta la desviación y bloquea la entrega.

Otro caso: el agente produce código correcto, pero su mandato está **revocado**. Los oráculos pasan; la autorización falla; la entrega sigue bloqueada.

## Qué contiene la demostración

Abra `dashboard/index.html` con el navegador. Seleccione `GF-03-wrong-threshold` para ver la detección del defecto y `GF-05-revoked-agent` para ver la separación entre corrección y autorización. Seleccione `GF-08-unapproved-release` para ver por qué se requiere aprobación de entrega incluso con ambos controles en PASS.

**Importante:** todos los permisos, revisiones y despliegues son simulados. No se conecta a ninguna plataforma ni a un sistema empresarial. No es una certificación de seguridad ni de calidad industrial.
