"""Lo que dicen las páginas que no son la portada: rubros, nosotros, contacto, privacidad y el 404.

Cada página es una lista de bloques que `generar_paginas.py` pasa a HTML y a Markdown (la versión para agentes).
En el texto valen **negrita** y [enlaces](/ruta). Lo que se dice acá tiene que ser cierto hoy: si algo no lo hace el
sistema, no va.
"""

SITIO = "https://vueltito.legios.com.ar"
WHATSAPP = "5493492665908"
TELEFONO = "+54 9 3492 66-5908"
ACTUALIZADO = "2026-11-17"

# Lo que trae cualquier sistema hecho sobre la base de Vueltito, sea del rubro que sea.
BASE = [
    ("Copia de seguridad diaria", "Revisada, de los últimos 60 días, y una guardada fuera del lugar."),
    ("Se actualiza solo", "Prueba la versión nueva aparte; si algo no anda, no toca nada."),
    ("Ayuda a distancia, segura", "Por una conexión privada y cifrada, sin abrir nada en el router."),
    ("Los datos son tuyos", "Todo queda en tu computadora, no en un sistema ajeno."),
    ("En cualquier computadora", "Anda en Windows, Mac o Linux, con la que ya tenés."),
    ("Factura electrónica de ARCA", "Con su CAE y su QR, si la necesitás."),
]

PASOS = [
    ("Miramos cómo trabajan", "Qué hacen todos los días, qué anotan, qué sistema o planilla usan hoy."),
    ("Armamos tu versión", "Sobre la base de Vueltito, con lo que tu rubro necesita, y la instalamos al lado de lo que ya usás."),
    ("Y quedamos cerca", "Actualizaciones y copias solas, ayuda a distancia y lo nuevo que vaya haciendo falta."),
]

RUBROS = {
    "arquitectos": {
        "nombre": "Estudios de arquitectura",
        "corto": "Arquitectos",
        "titulo": "Sistema de gestión a medida para estudios de arquitectura",
        "h1": ("Un sistema a medida", "para tu estudio de arquitectura."),
        "descripcion": "Sistema de gestión a medida para estudios de arquitectura en Argentina: obras, clientes, "
                       "presupuestos, horas, proveedores y cobros en un solo lugar, armado según cómo trabaja tu estudio.",
        "bajada": "Obras, clientes, presupuestos y cobros en un solo lugar, en vez de repartidos entre planillas, "
                  "carpetas y el WhatsApp. Armado según cómo trabaja tu estudio.",
        "mensaje": "Hola, quiero un sistema a medida para mi estudio de arquitectura.",
        "ejemplos": [
            ("Obras y clientes", "Cada obra con su cliente, su etapa y todo lo que se habló, a mano cuando llama."),
            ("Presupuestos y avances", "Presupuestos por rubro y el avance de cada obra, para saber qué se certificó y qué falta cobrar."),
            ("Horas por proyecto", "Quién trabajó en qué y cuánto, para saber qué obras dejan y cuáles no."),
            ("Proveedores y compras", "Lo que se compró para cada obra y a quién, con sus facturas."),
            ("Cobros y honorarios", "Quién debe, cuánto y desde cuándo, y la factura electrónica cuando se cobra."),
        ],
        "fotos": ["Pantalla de obras de un estudio", "Presupuesto de una obra", "Horas por proyecto"],
        "preguntas": [
            ("¿Reemplaza al programa de dibujo?", "No. Los planos se siguen haciendo con el programa de siempre; "
             "Vueltito ordena lo que pasa alrededor: obras, clientes, presupuestos, horas y cobros."),
            ("¿Se puede usar desde la obra?", "Lo vemos según el estudio. La base de Vueltito tiene una app para el "
             "celular, y lo que haga falta en la obra se suma a tu versión."),
            ("¿Tenemos que dejar las planillas de golpe?", "No. Se instala al lado y conviven hasta que estén cómodos; "
             "cuando se puede, traemos lo que ya tienen cargado."),
        ],
    },
    "laboratorios": {
        "nombre": "Laboratorios",
        "corto": "Laboratorios",
        "titulo": "Sistema de gestión a medida para laboratorios",
        "h1": ("Un sistema a medida", "para tu laboratorio."),
        "descripcion": "Sistema de gestión a medida para laboratorios en Argentina: pacientes u órdenes, muestras, "
                       "resultados, insumos con vencimiento, obras sociales y cobros, armado según cómo trabaja tu laboratorio.",
        "bajada": "Órdenes, muestras, resultados, insumos y cobros en un solo lugar, armado según cómo trabaja tu "
                  "laboratorio y no al revés.",
        "mensaje": "Hola, quiero un sistema a medida para mi laboratorio.",
        "ejemplos": [
            ("Órdenes y muestras", "Cada orden con su paciente o cliente, sus análisis y en qué paso está la muestra."),
            ("Resultados", "Cargar los resultados y entregarlos ordenados, sin buscar en carpetas."),
            ("Insumos y vencimientos", "Qué reactivos e insumos quedan, cuándo vencen y qué hay que pedir."),
            ("Obras sociales y cobros", "Lo que se factura a cada obra social o cliente y lo que falta cobrar."),
            ("Cómo va el laboratorio", "Cuántas órdenes entran, de qué tipo y cuánto deja cada mes."),
        ],
        "fotos": ["Órdenes del día de un laboratorio", "Carga de resultados", "Insumos con vencimiento"],
        "preguntas": [
            ("¿Dónde quedan los datos de los pacientes?", "En la computadora del laboratorio, no en un sistema ajeno. "
             "La copia diaria se revisa y una queda guardada fuera del lugar."),
            ("¿Se conecta con nuestros equipos?", "Depende del equipo. Lo vemos al mirar cómo trabajan, y si se "
             "puede, se suma a tu versión."),
            ("¿Tenemos que dejar el sistema que usamos?", "No de golpe. Se instala al lado y conviven hasta que "
             "estén cómodos."),
        ],
    },
    "medicos": {
        "nombre": "Consultorios médicos",
        "corto": "Médicos",
        "titulo": "Sistema de gestión a medida para consultorios médicos",
        "h1": ("Un sistema a medida", "para tu consultorio."),
        "descripcion": "Sistema de gestión a medida para consultorios y centros médicos en Argentina: turnos, "
                       "pacientes, obras sociales, cobros y recordatorios, armado según cómo trabaja tu consultorio.",
        "bajada": "Turnos, pacientes, obras sociales y cobros en un solo lugar, armado según cómo atiende tu "
                  "consultorio.",
        "mensaje": "Hola, quiero un sistema a medida para mi consultorio.",
        "ejemplos": [
            ("Turnos", "La agenda de cada profesional, con los turnos del día a la vista."),
            ("Pacientes", "Los datos de cada paciente y sus visitas, a mano cuando llega."),
            ("Recordatorios por WhatsApp", "El aviso del turno sale por WhatsApp, para que falten menos."),
            ("Obras sociales y cobros", "Qué se cobra particular, qué va a cada obra social y qué falta cobrar."),
            ("Cómo va el consultorio", "Cuántas consultas, de qué tipo y cuánto deja cada mes."),
        ],
        "fotos": ["Agenda de turnos de un consultorio", "Ficha de un paciente", "Cobros por obra social"],
        "preguntas": [
            ("¿Dónde quedan los datos de los pacientes?", "En la computadora del consultorio, no en un sistema "
             "ajeno. La copia diaria se revisa y una queda guardada fuera del lugar."),
            ("¿Sirve para varios profesionales?", "Sí: cada uno con su agenda, y lo que el consultorio necesite "
             "se suma a su versión."),
            ("¿Tenemos que dejar la agenda que usamos?", "No de golpe. Se instala al lado y conviven hasta que "
             "estén cómodos."),
        ],
    },
}


def wa(mensaje):
    from urllib.parse import quote
    return f"https://wa.me/{WHATSAPP}?text={quote(mensaje)}"


def pagina_rubro(clave, r):
    return {
        "ruta": f"/rubros/{clave}",
        "archivo": f"rubros/{clave}",
        "titulo": f"{r['titulo']} · Vueltito",
        "descripcion": r["descripcion"],
        "etiqueta": f"Sistema a medida · {r['nombre']}",
        "h1": r["h1"],
        "bajada": r["bajada"],
        "cta": r["mensaje"],
        "migas": [("Rubros", "/rubros/"), (r["corto"], f"/rubros/{clave}")],
        "servicio": {"nombre": r["titulo"], "publico": r["nombre"]},
        "bloques": [
            ("h2", "Lo que se puede resolver", "Cada uno trabaja distinto. Esto es lo que suele hacer falta; tu versión lleva lo tuyo."),
            ("tarjetas", [(t, d, None) for t, d in r["ejemplos"]]),
            ("fotos", clave, r["fotos"]),
            ("h2", "Lo que trae siempre", "La base de Vueltito, la misma que usan los comercios todos los días."),
            ("tarjetas", [(t, d, None) for t, d in BASE]),
            ("h2", "Cómo empezamos", None),
            ("pasos", PASOS),
            ("h2", "Preguntas", None),
            ("faq", r["preguntas"]),
            ("h2", "Otros rubros", None),
            ("p", "Hacemos sistemas a medida para cualquier rubro: [comercios](/), "
                  + ", ".join(f"[{o['nombre'].lower()}](/rubros/{k})" for k, o in RUBROS.items() if k != clave)
                  + " y los que nos traigan. Mirá [todos los rubros](/rubros/)."),
        ],
    }


PAGINAS = [
    {
        "ruta": "/rubros/",
        "archivo": "rubros/index",
        "titulo": "Sistemas de gestión a medida para cualquier rubro · Vueltito",
        "descripcion": "Vueltito hace sistemas de gestión a medida para cualquier rubro en Argentina: comercios, "
                       "estudios de arquitectura, laboratorios, consultorios médicos y más. Cada uno con su propia versión.",
        "etiqueta": "Para cualquier rubro",
        "h1": ("Un sistema a medida,", "sea cual sea tu rubro."),
        "bajada": "Vueltito nació en el mostrador de un comercio, y la misma base sirve para cualquier trabajo: "
                  "cada uno tiene su propia versión, con lo que su rubro necesita.",
        "cta": "Hola, quiero un sistema a medida para mi negocio.",
        "migas": [("Rubros", "/rubros/")],
        "servicio": {"nombre": "Sistemas de gestión a medida para cualquier rubro", "publico": "Comercios, profesionales y empresas"},
        "bloques": [
            ("tarjetas", [("Comercios", "Almacenes, autoservicios, fiambrerías y comercios de todos los rubros: caja, precios, facturas con una foto y fiado.", "/")]
                         + [(r["nombre"], r["bajada"], f"/rubros/{k}") for k, r in RUBROS.items()]
                         + [("¿Tu rubro no está?", "Contanos qué hacés y cómo trabajás. Si lo hacés todos los días, se puede armar.", "/contact")]),
            ("h2", "Lo que trae siempre", "La base de Vueltito, la misma para todos los rubros."),
            ("tarjetas", [(t, d, None) for t, d in BASE]),
            ("h2", "Cómo empezamos", None),
            ("pasos", PASOS),
        ],
    },
    *[pagina_rubro(k, r) for k, r in RUBROS.items()],
    {
        "ruta": "/about",
        "archivo": "about",
        "titulo": "Sobre nosotros · Vueltito",
        "descripcion": "Quiénes hacemos Vueltito, el sistema de gestión a medida de Legios para comercios y "
                       "cualquier rubro en Argentina, y cómo trabajamos.",
        "etiqueta": "Sobre nosotros",
        "h1": ("Hacemos sistemas", "sin vueltas."),
        "bajada": "Vueltito es un producto de [Legios](https://legios.com.ar), hecho en Argentina.",
        "cta": "Hola, quiero saber más de Vueltito.",
        "migas": [("Sobre nosotros", "/about")],
        "bloques": [
            ("h2", "Cómo nació", None),
            ("p", "Vueltito nació para un comercio de barrio: que la caja, los precios, las facturas de los "
                  "proveedores y el fiado dejaran de estar repartidos entre la calculadora y la libreta, y quedaran "
                  "en un solo lugar, con palabras, con letra grande y sin vueltas."),
            ("h2", "Cómo trabajamos", None),
            ("p", "Vueltito no es un sistema enlatado. Hay una **base común**, con la caja, los precios, la factura "
                  "electrónica de ARCA, las copias de seguridad y las actualizaciones, y cada cliente tiene **su "
                  "propia versión** con lo que su trabajo necesita. Cuando mejoramos la base, la mejora le llega a "
                  "todos; lo particular de cada uno queda en su versión."),
            ("p", "Cada cliente recibe el sistema instalado en su computadora, con Windows, Mac o Linux, y una "
                  "licencia mensual, anual o sin vencimiento. Los datos quedan en su computadora: son suyos."),
            ("h2", "Para quién", None),
            ("p", "Empezamos con comercios y hoy hacemos sistemas para cualquier rubro: "
                  + ", ".join(f"[{r['nombre'].lower()}](/rubros/{k})" for k, r in RUBROS.items())
                  + " y los que nos traigan. Mirá [todos los rubros](/rubros/)."),
            ("h2", "Hablemos", None),
            ("p", f"Escribinos por [WhatsApp al {TELEFONO}](https://wa.me/{WHATSAPP}) o mirá la página de "
                  "[contacto](/contact)."),
        ],
    },
    {
        "ruta": "/contact",
        "archivo": "contact",
        "titulo": "Contacto · Vueltito",
        "descripcion": f"Cómo contactar a Vueltito para un sistema de gestión a medida: WhatsApp {TELEFONO}. "
                       "Contanos qué hacés y qué sistema usás hoy.",
        "etiqueta": "Contacto",
        "h1": ("Contanos qué hacés", "y te mostramos cómo quedaría."),
        "bajada": f"La forma más rápida es por WhatsApp, al {TELEFONO}.",
        "cta": "Hola, quiero ver Vueltito andando en mi negocio.",
        "migas": [("Contacto", "/contact")],
        "bloques": [
            ("h2", "Qué contarnos", None),
            ("ul", [
                "**Qué hacés:** el rubro y cómo es un día normal de trabajo.",
                "**Qué usás hoy:** otro sistema, planillas, una libreta o nada.",
                "**Qué te complica:** lo que más tiempo te lleva o lo que más se pierde.",
                "**Con qué trabajás:** la computadora, la impresora, el lector de códigos o lo que ya tengas.",
            ]),
            ("p", "Con eso te mostramos cómo quedaría tu versión y te pasamos el precio. La licencia puede ser "
                  "mensual, anual o sin vencimiento."),
            ("h2", "Cómo seguimos", None),
            ("pasos", PASOS),
            ("h2", "Dónde estamos", None),
            ("p", "Somos [Legios](https://legios.com.ar), de Argentina. La instalación, las actualizaciones y la "
                  "ayuda se hacen a distancia, así que trabajamos con clientes de todo el país."),
        ],
    },
    {
        "ruta": "/privacy",
        "archivo": "privacy",
        "titulo": "Privacidad · Vueltito",
        "descripcion": "Qué datos usa el sitio de Vueltito y el sistema, dónde quedan y cómo pedir que los "
                       "corrijamos o borremos.",
        "etiqueta": "Privacidad",
        "h1": ("Tus datos,", "en tu computadora."),
        "bajada": f"Qué datos usa este sitio y el sistema, y qué podés pedirnos. Actualizado el {ACTUALIZADO}.",
        "cta": "Hola, tengo una consulta sobre mis datos.",
        "migas": [("Privacidad", "/privacy")],
        "bloques": [
            ("h2", "Quién es responsable", None),
            ("p", f"Vueltito es un producto de [Legios](https://legios.com.ar), de Argentina. Para cualquier "
                  f"consulta sobre tus datos, escribinos por [WhatsApp al {TELEFONO}](https://wa.me/{WHATSAPP})."),
            ("h2", "En este sitio", None),
            ("ul", [
                "**No usamos analítica ni cookies de seguimiento.**",
                "Tu navegador guarda sólo si elegiste el modo claro u oscuro, y no nos llega.",
                "Las letras se cargan de Google Fonts, que recibe tu dirección IP para entregarlas.",
                "El sitio se sirve con GitHub Pages y Cloudflare, que registran datos técnicos (como la IP y el "
                "navegador) para entregarlo y protegerlo.",
                "Los botones de contacto abren WhatsApp. Lo que nos escribas lo usamos sólo para responderte y "
                "mostrarte el sistema, y WhatsApp lo trata además según sus propias políticas.",
            ]),
            ("h2", "En el sistema", None),
            ("ul", [
                "Los datos de tu negocio quedan **en tu computadora**. Son tuyos.",
                "Una copia de seguridad se guarda fuera del lugar para poder recuperarla si se rompe la computadora.",
                "Si usás la lectura de facturas con una foto, la foto se envía por internet a un servicio de "
                "inteligencia artificial que la lee.",
                "Si usás la factura electrónica, los datos de cada factura se envían a ARCA, como pide la ley.",
                "La ayuda a distancia usa una conexión privada y cifrada.",
            ]),
            ("h2", "Tus derechos", None),
            ("p", "Podés pedirnos ver, corregir o borrar tus datos personales cuando quieras, escribiéndonos por "
                  "WhatsApp. Lo hacemos según la Ley 25.326 de Protección de los Datos Personales. La Agencia de "
                  "Acceso a la Información Pública, como órgano de control de esa ley, atiende las denuncias y "
                  "reclamos de quienes vean afectados sus derechos."),
        ],
    },
]

PAGINA_404 = {
    "archivo": "404",
    "titulo": "No encontramos esa página · Vueltito",
    "descripcion": "La página que buscás no existe.",
    "etiqueta": "Error 404",
    "h1": ("Esta página", "no existe."),
    "bajada": "Puede que el enlace esté mal escrito o que la hayamos movido.",
    "cta": "Hola, llegué a una página que no existe en el sitio de Vueltito.",
    "bloques": [
        ("ul", [
            "[La portada](/): qué es Vueltito y qué hace.",
            "[Rubros](/rubros/): sistemas a medida para cada rubro.",
            "[Contacto](/contact): cómo hablar con nosotros.",
            "[Mapa del sitio](/sitemap.xml) y [resumen para asistentes de IA](/llms.txt).",
        ]),
    ],
}
