# Tu primera API en 50 minutos

Material de la clase invitada **"Integraciones: cómo se hablan los sistemas"**, Facultad de Ingeniería, UNAM · sábado 14 de noviembre de 2026.

Expositor: Bryan Rodríguez Abarca, Technical Product Manager.

## Qué hay aquí

| Archivo | Para qué sirve |
| --- | --- |
| [guia-de-actividad.md](guia-de-actividad.md) | Los 6 retos paso a paso, con las URLs listas para copiar, glosario, preguntas de repaso y respuestas. |
| [slides.pdf](slides.pdf) | Las 21 láminas de la clase. |
| [integracion.py](integracion.py) | El reto para casa hecho en código: lee el clima de una API y le avisa a otro sistema con un webhook. |

## Durante la clase

Abre la [guía de actividad](guia-de-actividad.md) en tu laptop o celular. Solo necesitas un navegador: no instales nada ni crees cuentas.

## Después de la clase

1. Contesta las siete preguntas de "Comprueba lo que aprendiste" sin ver la guía.
2. Corre el script:

```bash
pip install requests
```

```bash
python integracion.py
```

Antes, abre https://webhook.site, copia tu URL única y pégala en `WEBHOOK_URL` dentro del script. Vas a ver llegar la petición en tiempo real.

3. Hazlo tuyo: cambia la ciudad, usa otra API de [public-apis](https://github.com/public-apis/public-apis), maneja el caso en que la API responda un error. Súbelo a tu GitHub con un README que explique qué hace: ese ya es un proyecto para tu perfil.

## Lo que deberías poder explicar

- Qué es una API y qué es una integración.
- Cómo se lee una petición y su respuesta: método, URL, headers, body, código de estado.
- La diferencia entre consultar una API y recibir un webhook.

## Aviso

Las URL de webhook.site son públicas. No envíes datos personales reales.
