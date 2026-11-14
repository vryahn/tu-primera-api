# Guía de actividad — Tu primera API (Integraciones, FI UNAM)

Sábado 14 de noviembre de 2026 · Expositor: Bryan Rodríguez Abarca, Technical Product Manager

## Antes de empezar

Solo necesitas un navegador (de tu laptop o de tu celular). No instales nada y no crees cuentas.

Tip: mantén presionada una URL para copiarla.

## Hoy vas a poder…

1. Explicar qué es una API y qué es una integración.
2. Leer una petición y su respuesta: método, URL, headers, body, código de estado.
3. Consumir una API real y conectar dos sistemas con un webhook.

## Formas de integrar sistemas

Integrar sistemas se puede hacer de varias formas. Por tiempo, hoy practicamos la más usada (API REST) y cerramos con webhooks. Las demás existen y te van a tocar en el trabajo.

| Forma | Cómo funciona | Dónde lo verás |
| --- | --- | --- |
| **API REST (hoy)** | Cada recurso tiene su URL y pides con métodos HTTP. Casi siempre contesta JSON, a veces XML | Casi toda API web moderna: pagos, mapas, clima |
| **Webhook (hoy)** | El otro sistema te avisa cuando pasa algo | Pagos cobrados, envíos, notificaciones |
| API SOAP | XML dentro de un sobre (Envelope), con un contrato estricto (WSDL) | Bancos, seguros, gobierno, facturación (CFDI) |
| GraphQL | Una sola URL donde pides solo los campos que quieres | Apps móviles y sitios web |
| gRPC | Llamadas binarias muy rápidas | Microservicios dentro de una empresa |
| Sin API: archivos y colas | Un sistema deja un archivo o un mensaje; el otro lo recoge después | Nómina, conciliaciones, procesos por lotes |

**Idea:** cambia el formato, no el fondo. En todas hay una petición, una respuesta y un contrato.

**Ojo:** que una API conteste XML no la hace SOAP. Lo que define a SOAP es el sobre (`Envelope`) y el contrato WSDL; una API REST también puede usar XML.

## Reto 1 — Tu primer GET

Tiempo: 4 min

1. Abre tu navegador.
2. Pega esta URL en la barra y presiona Enter:

```
https://dog.ceo/api/breeds/image/random
```

3. Ahora pega esta otra:

```
https://jsonplaceholder.typicode.com/posts/1
```

**Deberías ver**

- En la primera: `{"message":"https://images.dog.ceo/…","status":"success"}`. Abre la URL de `message` y recarga: la foto cambia.
- En la segunda: un JSON con `userId`, `id`, `title`, `body`.

**Idea:** son datos para programas, no para personas.

## Lo que acabas de hacer

Request (lo que envió tu navegador):

```
GET /posts/1                      ← método + endpoint
Host: jsonplaceholder.typicode.com ← servidor
Accept: application/json           ← header: qué formato quiero
(sin body: un GET solo pide)
```

Response (lo que contestó el servidor):

```
200 OK                             ← código de estado
Content-Type: application/json     ← header: qué formato te mando
{ "userId": 1, "id": 1, "title": "…", "body": "…" }  ← body en JSON
```

**Cómo leer un JSON:** llaves `{ }` = un objeto; cada línea es `"clave": valor`; corchetes `[ ]` = una lista de objetos.

## Reto 2 — Parámetros

Tiempo: 5 min

1. Parámetro de ruta: cambia `/posts/1` por `/posts/2`:

```
https://jsonplaceholder.typicode.com/posts/2
```

2. Parámetro de consulta:

```
https://jsonplaceholder.typicode.com/posts?userId=1
```

3. API real, clima de CDMX:

```
https://api.open-meteo.com/v1/forecast?latitude=19.43&longitude=-99.13&current_weather=true
```

4. Cambia la latitud y la longitud por las de tu ciudad.

¿No te sabes las coordenadas? Usa estas (latitud, longitud): Guadalajara `20.67`, `-103.35` · Monterrey `25.69`, `-100.32` · Puebla `19.04`, `-98.21` · Mérida `20.97`, `-89.62`. Van con punto decimal, no con coma.

**Deberías ver:** otro post; una lista `[ … ]` de posts, todos con `"userId": 1`; un bloque `current_weather` con `temperature`.

**Idea:** la misma API contesta distinto según lo que le pidas.

## Códigos de estado

Tres familias:

- **2xx**: funcionó.
- **4xx**: el error está en tu petición.
- **5xx**: el error está en el servidor.

Los cuatro que verás hoy:

| Código | Significa |
| --- | --- |
| **200** | Todo bien |
| **201** | Creado |
| **401** | Sin permiso |
| **404** | No existe |

Otros para reconocer: 400 pediste mal · 403 prohibido · 429 demasiadas peticiones · 500 falló el servidor.

## Reto 3 — Rómpela a propósito

Tiempo: 3 min

1. Antes de abrirlas, predice: ¿qué código crees que responda?
2. Abre esta URL:

```
https://jsonplaceholder.typicode.com/posts/99999
```

3. Abre esta otra:

```
https://pokeapi.co/api/v2/pokemon/noexiste
```

4. En laptop: F12 → pestaña Network para ver el código.
5. En celular: el código no se ve; el expositor lo muestra en pantalla.

**Pista para celular:** lee con calma lo que contesta la segunda URL. Algunas APIs también te dicen el código dentro del body.

**Idea:** un error bien comunicado también es parte del contrato.

(La respuesta está al final, en "Respuestas". No la leas antes de intentar.)

## Reto 4 — Mira tus headers

Tiempo: 2 min

1. Abre esta URL:

```
https://httpbin.org/headers
```

2. Compara con tu vecino.

**Deberías ver:** un JSON con los headers que TU navegador envió sin que lo pidieras: `User-Agent` (qué dispositivo y navegador usas), `Accept` (qué formatos aceptas), `Host`. Laptop y celular envían un `User-Agent` distinto.

**Idea:** los headers son los metadatos de la petición: quién eres, qué formato quieres, con qué permiso vienes.

## Métodos

| Método | Qué hace | En el restaurante | ¿Lleva body? |
| --- | --- | --- | --- |
| GET | Leer | Ver la carta | No |
| POST | Crear | Ordenar | Sí |
| PUT | Reemplazar completo | Cambiar toda tu orden | Sí |
| PATCH | Actualizar una parte | Cambiar solo la guarnición | Sí |
| DELETE | Borrar | Cancelar la orden | Normalmente no |

**Regla para recordar:** el navegador solo hace GET cuando pegas una URL. Para los demás métodos se usa un cliente de APIs (Hoppscotch, Postman) o código.

## Demo del expositor (solo mira)

> Tiempo: 4 min. Bryan lo hace en pantalla desde:
>
> `https://hoppscotch.io`
>
> **Fíjate en tres cosas:**
>
> 1. Dónde elige el método.
> 2. Dónde va el header `Content-Type`.
> 3. Dónde escribe el body y qué código regresa.
>
> **1. POST** a:
>
> `https://jsonplaceholder.typicode.com/posts`
>
> con header `Content-Type: application/json` y body:
>
> `{"title":"Mi primera integración","body":"Hola FI","userId":1}`
>
> Resultado: 201 con el recurso creado y un `id`.
>
> **2. PATCH** a:
>
> `https://jsonplaceholder.typicode.com/posts/1`
>
> con body `{"title":"Título corregido"}`. Resultado: 200 con solo ese campo cambiado.
>
> **3. DELETE** a:
>
> `https://jsonplaceholder.typicode.com/posts/1`
>
> Resultado: 200 con `{}`.
>
> Aclaración: JSONPlaceholder es una API de práctica; simula los cambios pero no los guarda.

## Reto 5 — Autenticación

Tiempo: 4 min

1. Predice: ¿qué pasa si le pides algo a una API privada sin identificarte?
2. Abre esta URL:

```
https://httpbin.org/bearer
```

3. En laptop: F12 → pestaña Network.
4. En celular: verás una página en blanco o un aviso de error.
5. Mira cómo el expositor repite la misma petición en Hoppscotch agregando el header `Authorization: Bearer mi-token-123`.

**Idea:** misma URL, distinto resultado; lo que cambió fue un header.

(La respuesta está al final, en "Respuestas".)

| Tipo | Cómo viaja | Dónde lo verás |
| --- | --- | --- |
| API key | Una llave fija en un header (por ejemplo `X-API-Key`) | APIs públicas de datos, mapas, clima |
| Basic | Usuario y contraseña codificados en el header `Authorization: Basic …` | Sistemas internos y antiguos |
| **Bearer token** | Un token temporal en `Authorization: Bearer …` | La mayoría de las APIs modernas |
| OAuth 2.0 | Un flujo para obtener ese token sin compartir tu contraseña ("Iniciar sesión con Google") | Integraciones entre empresas y apps de terceros |

**Regla de oro:** las credenciales van en headers, nunca en la URL ni en el repositorio.

## Reto 6 — Integra dos sistemas con un webhook

Tiempo: 7 min, en parejas

**Quién es quién:** tú eres la tienda y tu pareja es el sistema de pagos. Tu URL de webhook.site es tu "timbre": se la das al otro sistema para que te avise. Cuando tu pareja la abre, está tocando ese timbre.

1. Abre esta URL y copia tu URL única ("Your unique URL"):

```
https://webhook.site
```

2. Comparte tu URL con tu pareja (chat, o dictada).
3. Tu pareja abre en su navegador `TU_URL?nombre=Ana&mensaje=hola` (con datos inventados).
4. Mira tu pantalla de webhook.site.

**Deberías ver:** una petición nueva en la lista, en tiempo real, con `nombre` y `mensaje` y sus headers.

**Idea:** "no venga a preguntar: le avisamos cuando esté su mesa". Así avisa un sistema de pagos que ya cobró.

**Ahora cambien de rol:** que tu pareja reciba y tú envíes.

**En la vida real** nadie abre esa URL a mano: el sistema de pagos la llama solo, en el momento en que ocurre el cobro. Por eso un webhook es una API al revés: en vez de que tú vayas a preguntar, dejas tu dirección y te buscan.

> **Privacidad:** las URL de webhook.site son públicas y aceptan 50 peticiones. NO envíes datos personales reales.

**Bonus en laptop:** en

```
https://hoppscotch.io
```

envía un POST con body JSON `{"alumno":"Ana","materia":"Integraciones"}` a la URL del webhook. Si aparece un error de red/CORS, activa el interceptor "Proxy" en Settings.

**API: yo pregunto. Webhook: tú me avisas.**

## Reto bonus / para casa

Encadena dos APIs a mano: toma la temperatura de Open-Meteo y envíala al webhook de tu pareja como `?ciudad=...&temp=...`. Acabas de hacer, manualmente, lo que hace una integración automatizada.

## Mini glosario

- **API:** el contrato con el que un sistema le pide algo a otro.
- **Integración:** dos o más sistemas trabajando juntos usando esos contratos.
- **Endpoint:** la dirección (URL) concreta a la que le pides algo.
- **Request:** la petición que envías.
- **Response:** la respuesta que te regresa el servidor.
- **JSON:** formato de texto para datos, con pares `"clave": valor`.
- **Código de estado:** número que dice cómo salió la petición (200, 404…).
- **Header:** metadato de la petición o respuesta (quién eres, qué formato).
- **Body:** el contenido de los datos que se envían o se reciben.
- **Método:** la acción que pides: GET, POST, PUT, PATCH, DELETE.
- **Parámetro:** dato que ajusta lo que pides. De ruta: `/posts/2`. De consulta: `?userId=1`.
- **Token:** credencial que demuestra quién eres; viaja en el header `Authorization`.
- **Webhook:** aviso que un sistema te manda cuando pasa algo, sin que preguntes.
- **Idempotencia:** que repetir la misma petición no repita el efecto (reintentar un cobro no cobra dos veces).

## Si algo falla

1. Revisa que la URL esté completa, sin espacios ni letras de más.
2. Recarga la página o prueba otra vez.
3. Revisa tu conexión al Wi-Fi.
4. Pega la URL en una pestaña nueva, o pídele a tu vecino que la pruebe.

**Plan B si webhook.site falla:** abre esta URL, que devuelve en `args` lo que enviaste:

```
https://httpbin.org/get?nombre=Ana&mensaje=hola
```

**Plan B si httpbin.org no carga** (Retos 4 y 5): cambia `httpbin.org` por `httpbingo.org` en la misma URL. Las rutas `/headers`, `/bearer` y `/get` funcionan igual.

## Boleto de salida

Escribe una frase: describe una integración que usaste hoy sin darte cuenta, y qué dos sistemas se hablaron.

## Comprueba lo que aprendiste

Si puedes contestar estas siete preguntas sin ver la guía, ya dominas lo de hoy. Son del tipo que aparece en entrevistas técnicas. Las respuestas están al final.

1. ¿Qué diferencia hay entre una API y una integración?
2. ¿Qué diferencia hay entre un parámetro de ruta y uno de consulta?
3. ¿Qué significan 401, 403 y 404? ¿De quién es el error en un 4xx y en un 5xx?
4. ¿Cuándo usarías PUT y cuándo PATCH?
5. ¿En qué se diferencia consultar una API de recibir un webhook?
6. ¿Por qué las credenciales no deben ir en la URL?
7. ¿Qué es la idempotencia y por qué importa al reintentar un pago?

## Lo mismo, en código (para después de clase)

Hoy usaste el navegador. En un trabajo real, estas mismas peticiones las hace un programa. Tres formas de dar ese paso, de la más fácil a la más útil.

**1. Sin instalar nada (laptop).** Con la pestaña del Reto 1 abierta, presiona F12, entra a Console y pega esto. Si Chrome te lo pide, escribe antes `allow pasting`.

```js
fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then(r => r.json())
  .then(console.log)
```

**2. En la terminal, con curl.** La opción `-i` muestra el código de estado y los headers: todo lo de "Lo que acabas de hacer", en texto.

```bash
curl -i https://jsonplaceholder.typicode.com/posts/1
```

```bash
curl -i https://httpbin.org/bearer -H "Authorization: Bearer mi-token-123"
```

**3. En Python: tu primera integración automática.** Es el reto para casa, pero ahora lo hace un programa: lee de un sistema y le avisa a otro. Instala la librería con `pip install requests` y cambia `TU_URL_DE_WEBHOOK` por tu URL de webhook.site.

```python
import requests

clima = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": 19.43, "longitude": -99.13, "current_weather": "true"},
)
print(clima.status_code)
temp = clima.json()["current_weather"]["temperature"]

aviso = requests.post("TU_URL_DE_WEBHOOK", json={"ciudad": "CDMX", "temp": temp})
print(aviso.status_code)
```

## Cómo llevar esto a tu perfil

- **Mini proyecto de una tarde:** sube el script de Python a GitHub con un README que explique qué API consume, qué envía y qué hace si la API responde 500.
- **Siguiente escalón:** usa una API que pida API key (elige una de public-apis), después construye tu propia API (FastAPI o Express) y documéntala con OpenAPI.
- **En tu CV, solo cuando lo hayas hecho:** "Integré dos APIs REST con Python (JSON, autenticación con token, webhooks) y manejo de errores HTTP".
- **Dónde se usa:** backend, integraciones, ingeniería de datos, automatización de pruebas (QA), implementación y soporte técnico, producto técnico.

## Para seguir aprendiendo

**Recursos**

- [MDN: "Descripción general de HTTP"](https://developer.mozilla.org/es/docs/Web/HTTP/Guides/Overview)
- [public-apis en GitHub](https://github.com/public-apis/public-apis) (lista de APIs gratuitas)
- [Hoppscotch](https://hoppscotch.io) y [Postman](https://learning.postman.com/)
- [Documentación de Open-Meteo](https://open-meteo.com/en/docs), como ejemplo de buena documentación

**Temas para investigar**

- SOAP, GraphQL y gRPC: los otros estilos de API
- Polling vs eventos
- Síncrono vs asíncrono
- Reintentos e idempotencia
- OpenAPI (Swagger)
- Plataformas iPaaS (Zapier, Make, n8n, MuleSoft)

## Respuestas — no leas esto antes de intentar

**Reto 3:** 404. El servidor sí contestó, pero ese recurso no existe ("ese platillo no existe").

**Reto 5:** sin token, 401; con el header `Authorization: Bearer mi-token-123`, 200 con `"authenticated": true`.

**Comprueba lo que aprendiste:**

1. Una API es el contrato para pedirle algo a un sistema. Una integración son dos o más sistemas trabajando juntos usando esos contratos.
2. El de ruta identifica un recurso (`/posts/2`). El de consulta filtra o ajusta la respuesta (`?userId=1`).
3. 401: no te identificaste. 403: te identificaste, pero no tienes permiso. 404: eso no existe. En un 4xx el error está en tu petición; en un 5xx, en el servidor.
4. PUT reemplaza el recurso completo. PATCH cambia solo los campos que mandas.
5. En la API tú preguntas cuando quieres. En el webhook dejas tu URL y el otro sistema te avisa cuando pasa algo.
6. Porque la URL queda en el historial, en los registros de los servidores y en cualquier enlace que compartas. Un header no.
7. Es que repetir la misma petición no repita el efecto. Si un pago tarda y lo reintentas, sin idempotencia podrías cobrar dos veces.
