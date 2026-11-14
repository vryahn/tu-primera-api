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

## Cómo se arma una petición HTTP

HTTP es el protocolo: el idioma en que se hablan tu navegador y los servidores. Toda petición tiene cuatro partes, y hoy vas a practicar una por una.

| Elemento | Qué es | En el restaurante | Lo practicas en |
| --- | --- | --- | --- |
| **URL** | A quién le pides y qué: servidor + ruta + parámetros | Qué restaurante y qué platillo | Reto 1 |
| **Método** | La acción que pides: leer, crear, cambiar, borrar | Ver la carta, ordenar, cambiar tu orden, cancelarla | Reto 2 |
| **Body** | Los datos que viajan | El detalle de tu orden | Reto 3 |
| **Headers** | Datos sobre la petición: el formato y quién eres | La etiqueta del pedido y tu reservación | Retos 4 y 5 |

El servidor siempre responde con tres cosas: **código de estado**, **headers** y **body**.

| Código | Significa |
| --- | --- |
| **200** | Todo bien |
| **201** | Creado |
| **400** | Pediste mal |
| **401** | No te identificaste |
| **404** | No existe |
| **415** | No entiendo ese formato |
| **500** | Falló el servidor |

Regla rápida: **2xx** funcionó · **4xx** el error está en tu petición · **5xx** el error está en el servidor.

## Reto 1 — URL y parámetros

Tiempo: 7 min · Solo navegador (laptop o celular)

Cuando pegas una URL en el navegador, haces una petición con el método **GET**: solo lee, no cambia nada.

**Parte A: una URL que ya conoces.**

1. Abre este enlace:

```
https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=43s
```

2. Léelo por partes:

| Parte | En este enlace | Qué dice |
| --- | --- | --- |
| Servidor | `www.youtube.com` | A quién le pides |
| Ruta (endpoint) | `/watch` | Qué le pides: ver un video |
| Parámetro `v` | `dQw4w9WgXcQ` | Cuál video |
| Parámetro `t` | `43s` | En qué segundo empieza |

3. Cambia `t=43s` por `t=0s` y vuelve a abrirlo. Después borra `&t=0s` completo.

**Deberías ver:** el mismo video, empezando en otro momento. El signo `?` abre los parámetros y `&` los separa.

**Parte B: lo que dice un enlace de anuncio.** No lo abras, solo léelo:

```
https://tienda.ejemplo/tenis?utm_source=facebook&utm_campaign=buen_fin&fbclid=IwAR0x9
```

¿De qué red social viene quien dio clic? ¿De qué campaña? Esos parámetros no cambian la página: le avisan a la tienda de dónde llegaste. Cuando compartes un video desde la app de YouTube pasa igual: el enlace lleva un `si=…` que identifica quién lo compartió.

**Parte C: lo mismo, en una API.**

4. Abre esta URL. Ya no es una página: son datos.

```
https://rickandmortyapi.com/api/character/1
```

5. Copia la URL que viene en `image` y ábrela en otra pestaña.
6. Parámetro de ruta: cambia el `1` por `2`, o por el número que quieras.
7. Parámetros de consulta: filtra.

```
https://rickandmortyapi.com/api/character/?name=rick&status=alive
```

8. Cambia `rick` por `morty`, o `alive` por `dead`.

**Deberías ver:** un personaje distinto por cada número; y con los filtros, una lista `results` solo con los que cumplen.

**Parte D: rómpela.**

9. Antes de abrirla, predice: ¿qué contesta el servidor si pides un personaje que no existe?

```
https://rickandmortyapi.com/api/character/99999
```

En laptop: F12 → pestaña Network → recarga, para ver el código de estado.

**Idea:** una URL no es una dirección fija. Es una petición con datos adentro.

(La respuesta de la predicción está al final, en "Respuestas".)

## Reto 2 — Métodos

Tiempo: 10 min · Laptop, con Hoppscotch · Si traes celular, haz equipo con alguien con laptop: tú verificas los cambios con GET desde tu navegador.

| Método | Qué hace | En el restaurante | ¿Lleva body? |
| --- | --- | --- | --- |
| **GET** | Leer | Ver la carta | No |
| **POST** | Crear | Ordenar | Sí |
| **PUT** | Reemplazar completo | Cambiar toda tu orden | Sí |
| **PATCH** | Cambiar una parte | Cambiar solo la guarnición | Sí |
| **DELETE** | Borrar | Cancelar la orden | Normalmente no |

El navegador solo hace GET. Para los demás métodos se usa un cliente de APIs o código. Abre:

```
https://hoppscotch.io
```

El método se elige en el menú a la izquierda de la URL. El body se escribe en la pestaña **Body**, con Content Type `application/json`.

Vas a crear tu propio personaje en una API que sí guarda los datos.

**1. POST: créalo.** Método `POST` a esta URL:

```
https://api.restful-api.dev/objects
```

con este body (cambia los valores por los tuyos, inventados):

```json
{
  "name": "Ana Sánchez",
  "data": {
    "especie": "Humana",
    "planeta": "Tierra",
    "poder": "Depurar sin dormir"
  }
}
```

**Deberías ver:** tu personaje de regreso, con un `id` que le puso el servidor. **Copia ese `id`.**

**2. GET: compruébalo.** Método `GET` a la misma URL con tu `id` al final. También puedes pegarla en el navegador, o pasársela a tu vecino para que lo vea desde su celular:

```
https://api.restful-api.dev/objects/TU_ID
```

**3. PATCH: súbelo de nivel.** Método `PATCH` a la URL con tu `id`, con este body:

```json
{ "name": "Ana Sánchez, nivel 2" }
```

Repite el GET del paso 2. **Deberías ver:** el nombre nuevo, y lo demás intacto.

**4. DELETE: bórralo.** Método `DELETE` a la URL con tu `id`, sin body.

**5. GET otra vez.** Predice primero: ¿qué código va a regresar?

**Idea:** misma URL, cuatro métodos, cuatro efectos distintos. La URL dice *a qué*; el método dice *qué hacerle*.

## Reto 3 — Body

Tiempo: 4 min · Laptop, con Hoppscotch

El body son los datos que viajan. Tú lo envías con POST, PUT y PATCH; el servidor te lo regresa en casi todas las respuestas. Casi siempre va en JSON.

**Cómo leer un JSON:** llaves `{ }` = un objeto · cada línea es `"clave": valor` · corchetes `[ ]` = una lista.

1. Repite el POST del Reto 2 para crear otro personaje y copia su `id`.
2. Predice: si ahora mandas un **PUT** con solo el nombre, ¿qué le pasa a `data`?

```json
{ "name": "Solo me queda el nombre" }
```

3. Manda ese PUT a `https://api.restful-api.dev/objects/TU_ID` y revisa la respuesta.
4. Ahora rompe el body: manda un POST con este JSON, al que le faltan las llaves de cierre.

```
{ "name": "Ana", "data": { "especie": "Humana"
```

**Idea:** PATCH cambia solo lo que mandas; PUT reemplaza todo. Y si el body está mal escrito, el servidor no adivina: te dice que pediste mal.

(Respuestas al final.)

## Reto 4 — Headers

Tiempo: 4 min

Los headers son datos sobre la petición. Si el body es el paquete, los headers son la etiqueta.

| Header | Qué dice | Ejemplo |
| --- | --- | --- |
| `Content-Type` | En qué formato va el body que te mando | `application/json` |
| `Accept` | En qué formato quiero la respuesta | `application/json` |
| `User-Agent` | Qué programa hace la petición | Tu navegador y tu dispositivo |
| `Authorization` | Quién soy (Reto 5) | `Bearer mi-token-123` |

1. En el navegador (laptop o celular), abre:

```
https://httpbin.org/headers
```

**Deberías ver:** los headers que TU navegador envió sin que lo pidieras. Compara con tu vecino: laptop y celular mandan un `User-Agent` distinto.

2. En Hoppscotch, haz un `GET` a esa misma URL, pero antes agrega en la pestaña **Headers** uno tuyo: clave `X-Alumno`, valor tu nombre. Búscalo en la respuesta.
3. Predice: ¿qué pasa si mandas un body JSON pero dices que es otro formato? Repite el POST del Reto 2 cambiando el Content Type del body a `text/plain`.

**Idea:** el servidor lee primero la etiqueta. Si la etiqueta no coincide con el paquete, lo rechaza sin abrirlo.

(Respuesta al final.)

## Reto 5 — Seguridad: ¿quién eres?

Tiempo: 5 min

El header más importante es el que dice quién eres.

1. Predice: ¿qué pasa si le pides algo a una API privada sin identificarte?
2. Abre esta URL en el navegador:

```
https://httpbin.org/bearer
```

En laptop: F12 → pestaña Network. En celular verás una página en blanco o un aviso de error.

3. En Hoppscotch, haz un `GET` a la misma URL agregando este header: clave `Authorization`, valor `Bearer mi-token-123`.

**Idea:** misma URL, distinto resultado; lo único que cambió fue un header.

| Tipo | Cómo viaja | Dónde lo verás |
| --- | --- | --- |
| API key | Una llave fija en un header (por ejemplo `X-API-Key`) | APIs públicas de datos, mapas, clima |
| Basic | Usuario y contraseña codificados en `Authorization: Basic …` | Sistemas internos y antiguos |
| **Bearer token** | Un token temporal en `Authorization: Bearer …` | La mayoría de las APIs modernas |
| OAuth 2.0 | Un flujo para obtener ese token sin compartir tu contraseña ("Iniciar sesión con Google") | Integraciones entre empresas y apps de terceros |

**Regla de oro:** las credenciales van en headers, nunca en la URL ni en el repositorio. Ya viste en el Reto 1 cuánto cuenta una URL.

(Respuesta al final.)

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
- **Parámetro:** dato que ajusta lo que pides. De ruta: `/character/2`. De consulta: `?name=rick`.
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

**Plan B si api.restful-api.dev no responde** (Retos 2 y 3): usa `https://jsonplaceholder.typicode.com/posts` con los mismos métodos. Ojo: esa API simula los cambios pero no los guarda, así que el GET final no mostrará el 404.

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

**1. Sin instalar nada (laptop).** Con cualquier pestaña del Reto 1 abierta, presiona F12, entra a Console y pega esto. Si Chrome te lo pide, escribe antes `allow pasting`.

```js
fetch("https://rickandmortyapi.com/api/character/1")
  .then(r => r.json())
  .then(console.log)
```

**2. En la terminal, con curl.** La opción `-i` muestra el código de estado y los headers de la respuesta, en texto.

```bash
curl -i https://rickandmortyapi.com/api/character/1
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

**Reto 1:** 404, con el body `{"error":"Character not found"}`. El servidor sí contestó, pero ese recurso no existe ("ese platillo no existe").

**Reto 2:** el último GET regresa 404: lo borraste de verdad. (Al crear, esta API contesta 200; muchas otras contestan 201, "creado".)

**Reto 3:** con el PUT, `data` queda en `null`: PUT reemplaza el recurso completo y tú solo mandaste el nombre. El body roto regresa 400, "pediste mal".

**Reto 4:** 415, "no entiendo ese formato". El body era JSON válido, pero la etiqueta decía otra cosa.

**Reto 5:** sin token, 401; con el header `Authorization: Bearer mi-token-123`, 200 con `"authenticated": true`.

**Comprueba lo que aprendiste:**

1. Una API es el contrato para pedirle algo a un sistema. Una integración son dos o más sistemas trabajando juntos usando esos contratos.
2. El de ruta identifica un recurso (`/character/2`). El de consulta filtra o ajusta la respuesta (`?name=rick`).
3. 401: no te identificaste. 403: te identificaste, pero no tienes permiso. 404: eso no existe. En un 4xx el error está en tu petición; en un 5xx, en el servidor.
4. PUT reemplaza el recurso completo. PATCH cambia solo los campos que mandas.
5. En la API tú preguntas cuando quieres. En el webhook dejas tu URL y el otro sistema te avisa cuando pasa algo.
6. Porque la URL queda en el historial, en los registros de los servidores y en cualquier enlace que compartas. Un header no.
7. Es que repetir la misma petición no repita el efecto. Si un pago tarda y lo reintentas, sin idempotencia podrías cobrar dos veces.
