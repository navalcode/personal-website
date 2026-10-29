"""Generate two complete static pages; no external packages or runtime scripts."""
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORIGIN = json.loads((ROOT / 'site.json').read_text())['origin']
PROJECTS = [
    ('rumbo-android', 'Rumbo', 'Kotlin · Compose · Room · Retrofit', '40886717961',
     'A complete Android flow, including the moments when the source fails.',
     'Un flujo Android completo, también cuando falla la fuente de datos.',
     'Fictional trips, search, detail, favorites and local bookings. Inspect the REST boundary, read-only ViewModel state, Navigation and cached content during failures.',
     'Escapadas ficticias, búsqueda, detalle, favoritos y reservas locales. Frontera REST, estado de ViewModel de solo lectura, Navigation y caché durante los fallos.',
     '32 JVM tests · 7 emulator tests · optimized release checked', '32 tests JVM · 7 de emulador · release optimizada comprobada'),
    ('bitacora-flutter', 'Bitácora', 'Flutter · Dart · Local persistence · ES/EN', '40887125281',
     'Async work that keeps acknowledged state consistent.', 'Trabajo asíncrono con un estado guardado coherente.',
     'An original field-task board with Android flavors. Follow request generations, failed storage reads, acknowledged writes and English/Spanish resources.',
     'Tablero original de tareas con flavors Android. Generaciones de peticiones, fallos de lectura, escritura confirmada y recursos en español e inglés.',
     '22 controller/widget tests · native persistence journey · Android/web', '22 tests de controlador/widgets · recorrido nativo · Android/web'),
    ('coroutine-lab', 'Coroutine Lab', 'Kotlin · Coroutines · Flow', '40865010719',
     'Who owns the work, and what happens when it fails?', '¿Quién es dueño del trabajo y qué ocurre cuando falla?',
     'Structured concurrency, launch/async, exception propagation and Flow operators. Predict the timeline, then compare the implementation and tests.',
     'Concurrencia estructurada, launch/async, propagación de errores y operadores Flow. Anticipa la secuencia y contrástala con código y tests.',
     '9 JVM tests · build and lint verified', '9 tests JVM · build y lint comprobados'),
    ('compose-effect-lab', 'Compose Effect Lab', 'Compose · Effects · Lifecycle', '40865225369',
     'When should an effect restart, and who releases its resources?', '¿Cuándo reinicia un efecto y quién libera sus recursos?',
     'Effect keys, cleanup and callbacks that stay current without restarting work. Inspect LaunchedEffect, DisposableEffect and rememberUpdatedState.',
     'Claves de efectos, limpieza y callbacks actualizados sin reiniciar trabajo. LaunchedEffect, DisposableEffect y rememberUpdatedState.',
     '4 JVM tests · 4 instrumented tests · verified CI', '4 tests JVM · 4 instrumentados · CI comprobada'),
    ('android-coroutines-tests-mini', 'Coroutines Tests Mini', 'ViewModel · StateFlow · Virtual time', '40865096443',
     'Make cancellation and latest-query behavior observable.', 'Hacer observables la cancelación y la última consulta.',
     'Injectable dispatchers, fakes and virtual time for ViewModel state, replacement of asynchronous work and failure recovery.',
     'Dispatchers inyectables, fakes y tiempo virtual para estado de ViewModel, sustitución de trabajo asíncrono y recuperación.',
     '9 JVM tests · build and lint verified', '9 tests JVM · build y lint comprobados'),
    ('spec-evidence-lab', 'Spec Evidence Lab', 'Python · MCP · Spec-driven development', '40883352632',
     'Connect acceptance criteria to actual test evidence.', 'Conectar aceptación y evidencia de pruebas real.',
     'Original CLI and optional MCP adapter. Trace JUnit to a versioned specification and reject stale proposals. Keep human review and evidence provenance explicit. EN/ES summaries preserve machine statuses and hashes.',
     'CLI original y adaptador MCP opcional. Relaciona JUnit con una especificación versionada y rechaza propuestas obsoletas, conservando revisión humana y límites de procedencia. Resúmenes ES/EN sin cambiar estados o hashes.',
     '40 checker/configuration tests · 5 sample tests · 4 MCP cases', '40 tests del checker/configuración · 5 del ejemplo · 4 casos MCP'),
    ('vehicle-session-lab', 'Vehicle Session Lab', 'Kotlin/JVM · Callbacks · Automotive simulation', '40879403899',
     'A connection can fail independently of its owner.', 'Una conexión puede fallar sin cancelar a su propietario.',
     'A fictional gateway demonstrates bounded reconnection, late callbacks, resource cleanup and per-metric freshness. Host-side simulation, without Android Car or vehicle hardware.',
     'Proveedor ficticio con reconexión acotada, callbacks tardíos, liberación de recursos y antigüedad por métrica. Simulación en el host, sin Android Car o hardware real.',
     '20 JVM tests · executable demo · verified CI', '20 tests JVM · demo ejecutable · CI comprobada'),
    ('gnss-diagnostics-lab', 'GNSS Diagnostics Lab', 'Python · C · ctypes · Synthetic captures', '40879068228',
     'A valid report is not proof of a precise receiver.', 'Un reporte válido no prueba la precisión de un receptor.',
     'Bounded CSV parsing, exact reference pairing, fix gaps and apparent jumps. An original Python/C boundary uses a spherical model and synthetic data, with no device acquisition.',
     'CSV acotado, emparejado exacto, pérdida de fix, huecos y saltos aparentes. Frontera Python/C original, modelo esférico y datos sintéticos, sin adquisición del dispositivo.',
     '25 tests · native build · Linux/macOS CI', '25 tests · build nativo · CI Linux/macOS'),
]

COPY = {
    'en': dict(other='ES', other_file='es.html', skip='Skip to content', work='Projects', method='Approach', profile='GitHub profile',
               eyebrow='Manuel Naval / Mobile engineering', title='Mobile engineering.<br>From state to delivery.',
               intro='I develop and maintain mobile applications, working on architecture, state, integration and testing. The current examples cover Android and Flutter; native iOS is the next extension.',
               cta='Explore the projects', start='Start with Rumbo', note='A self-contained Android example. Follow a feature through its data boundary, presentation state and failure tests.',
               apps='Two complete mobile examples', apps_intro='Original applications with fictional data, explicit failure states and documented validation.',
               android='The behavior behind the interface', android_intro='Focused Android labs for concurrency, effects, ownership and testable state.',
               integrations='Tools and integration boundaries', integrations_intro='AI-assisted engineering, lifecycle ownership and native diagnostics, with their scope made explicit.',
               source='Source', ci='Executed CI', map='Implementation diagram · Rumbo', capture='Actual emulator capture', capture_note='Bitácora · API 37 · English UI', image_alt='Bitácora board with one completed task and five pending tasks',
               approach='AI-assisted engineering,<br>with an explicit contract.', approach_body='I work with reusable context, skills, MCP tools and project terminology. A specification connects the problem to behavior, decisions and verification, so a person or a new agent session can continue with reliable context.',
               approach_link='Read the working SDD example',
               steps=[('Define the boundary','State the user need, constraints and unknowns.'),('Describe acceptance','Include failures, cancellation and recovery.'),('Implement and review','Inspect the code, compare alternatives and keep changes reviewable.'),('Keep the evidence','Run meaningful checks and record what they can establish.')],
               scope_title='Growing across mobile platforms', scope_body='Android and Flutter have runnable examples. Native iOS will grow through a Swift state and concurrency core, then SwiftUI, persistence and platform checks. The roadmap keeps planned work separate from executed validation.', roadmap='Read the mobile roadmap',
               history_title='Earlier work stays in context', history_body='GitHub also contains earlier Android, Flutter, Java and web exercises. Their READMEs explain the scope, preserve original notes and credit shared or upstream work.',
               history_link='Browse the GitHub profile', footer='Manuel Naval · Mobile engineering', language_name='Español', description='Mobile engineering by Manuel Naval. Android, Kotlin, Flutter, architecture, testing and a gradual path to native iOS.'),
    'es': dict(other='EN', other_file='index.html', skip='Saltar al contenido', work='Proyectos', method='Método', profile='Perfil GitHub',
               eyebrow='Manuel Naval / Ingeniería móvil', title='Ingeniería móvil.<br>Del estado a la entrega.',
               intro='Desarrollo y mantengo aplicaciones móviles, trabajando en arquitectura, estado, integración y pruebas. Los ejemplos actuales cubren Android y Flutter; iOS nativo es la siguiente ampliación.',
               cta='Explorar los proyectos', start='Empieza por Rumbo', note='Un ejemplo Android autónomo. Sigue una funcionalidad por su frontera de datos, estado de presentación y pruebas de fallo.',
               apps='Dos ejemplos móviles completos', apps_intro='Aplicaciones originales con datos ficticios, estados de fallo explícitos y validación documentada.',
               android='El comportamiento tras la interfaz', android_intro='Laboratorios Android centrados en concurrencia, efectos, propiedad de recursos y estado testeable.',
               integrations='Herramientas y fronteras de integración', integrations_intro='Ingeniería asistida por IA, propiedad del ciclo de vida y diagnóstico nativo, con su alcance explícito.',
               source='Código', ci='CI ejecutada', map='Esquema de implementación · Rumbo', capture='Captura real del emulador', capture_note='Bitácora · API 37 · Interfaz inglesa', image_alt='Tablero de Bitácora con una tarea completada y cinco pendientes',
               approach='Ingeniería asistida por IA,<br>con un contrato explícito.', approach_body='Trabajo con contexto reutilizable, skills, herramientas MCP y terminología de proyecto. La especificación conecta el problema con comportamiento, decisiones y comprobación para que otra persona o sesión de un agente pueda continuar con contexto fiable.',
               approach_link='Ver el ejemplo SDD ejecutable',
               steps=[('Definir los límites','Necesidad del usuario, restricciones e incógnitas.'),('Describir la aceptación','Incluir fallos, cancelación y recuperación.'),('Implementar y revisar','Leer el código, comparar alternativas y preparar cambios revisables.'),('Conservar la evidencia','Ejecutar comprobaciones útiles y registrar qué permiten concluir.')],
               scope_title='Ampliación entre plataformas móviles', scope_body='Android y Flutter tienen ejemplos ejecutables. iOS nativo crecerá con un núcleo Swift de estado y concurrencia, seguido de SwiftUI, persistencia y comprobaciones de plataforma. La hoja de ruta distingue el trabajo previsto de la validación ejecutada.', roadmap='Ver la hoja de ruta móvil',
               history_title='El trabajo anterior conserva su contexto', history_body='GitHub también conserva ejercicios anteriores de Android, Flutter, Java y web. Sus README explican el alcance, mantienen las notas originales y atribuyen el trabajo compartido o de terceros.',
               history_link='Explorar el perfil GitHub', footer='Manuel Naval · Ingeniería móvil', language_name='English', description='Ingeniería móvil de Manuel Naval. Android, Kotlin, Flutter, arquitectura, pruebas y ampliación gradual a iOS nativo.'),
}


def render(language):
    c = COPY[language]
    es = language == 'es'
    filename = 'es.html' if es else 'index.html'
    profile = 'https://github.com/navalcode' + ('/navalcode/blob/main/README.es.md' if es else '')
    page_title = 'Manuel Naval · Ingeniería móvil' if es else 'Manuel Naval · Mobile engineering'
    canonical = ''
    if ORIGIN:
        origin = ORIGIN.rstrip('/') + '/'
        canonical = f'<link rel="canonical" href="{escape(origin + (filename if es else ""))}"><link rel="alternate" hreflang="en" href="{escape(origin)}"><link rel="alternate" hreflang="es" href="{escape(origin + "es.html")}">'

    def card(project, index, featured=False):
        slug, title, stack, run, q_en, q_es, body_en, body_es, check_en, check_es = project
        repo = 'https://github.com/navalcode/' + slug
        visual = ''
        if featured and index == 0:
            visual = f'<div class="feature-visual"><div class="flow-map" aria-label="{escape(c["map"])}">' + ''.join(f'<div class="flow-step"><small>{n:02d}</small><strong>{label}</strong></div>' for n,label in enumerate(['Retrofit / DTO','Repository / Room','ViewModel / Flow','Compose / Navigation'],1)) + f'</div><span class="visual-label">{escape(c["map"])}</span></div>'
        elif featured:
            visual = f'<div class="feature-visual phone-stage"><a class="phone" href="assets/bitacora-board.png" aria-label="{escape(c["capture"])}"><img src="assets/bitacora-board.png" width="1344" height="2992" alt="{escape(c["image_alt"])}"></a><div class="capture-label"><strong>{escape(c["capture"])}</strong>{escape(c["capture_note"])}</div></div>'
        content = f'<span class="index">{index + 1:02d} / {escape(q_es if es else q_en)}</span>' if not featured else ''
        content += f'<h3>{escape(title)}</h3><div class="stack">' + ''.join(f'<span class="tag">{escape(tag)}</span>' for tag in stack.split(' · ')) + f'</div><p>{escape(body_es if es else body_en)}</p><p class="evidence">{escape(check_es if es else check_en)}</p><div class="links"><a href="{repo}">{escape(c["source"])}<span aria-hidden="true"> ↗</span><span class="sr-only"> · {escape(title)}</span></a><a href="{repo}/actions/runs/{run}">{escape(c["ci"])}<span class="sr-only"> · {escape(title)}</span></a></div>'
        return f'<article class="feature">{visual}<div class="feature-body">{content}</div></article>' if featured else f'<article class="card">{content}</article>'

    def section(number, title, intro, projects, start, featured=False):
        return f'<section class="section"'+(' id="projects"' if start==0 else '')+f'><div class="section-head"><div><span class="section-number">{number}</span><h2>{escape(title)}</h2></div><p>{escape(intro)}</p></div><div class="'+('featured' if featured else 'cards')+'">'+''.join(card(p,start+i,featured) for i,p in enumerate(projects))+'</div></section>'

    return f'''<!doctype html>
<html lang="{language}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(page_title)}</title><meta name="description" content="{escape(c['description'])}"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; img-src 'self'; base-uri 'none'; form-action 'none'"><meta name="referrer" content="strict-origin-when-cross-origin"><meta property="og:title" content="{escape(page_title)}"><meta property="og:description" content="{escape(c['description'])}"><meta property="og:type" content="website"><link rel="stylesheet" href="styles.css"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml">{canonical}</head>
<body><a class="skip" href="#main">{escape(c['skip'])}</a><header class="site-header"><nav class="wrap nav" aria-label="{'Principal' if es else 'Main'}"><a class="wordmark" href="{filename}">navalcode<span>.</span></a><div class="nav-links"><a href="#projects">{escape(c['work'])}</a><a href="#approach">{escape(c['method'])}</a><a href="{profile}">GitHub ↗</a><a class="language" href="{c['other_file']}" lang="{'en' if es else 'es'}" hreflang="{'en' if es else 'es'}" aria-label="{c['language_name']}">{c['other']}</a></div></nav></header>
<main id="main" class="wrap" tabindex="-1"><section class="hero"><div><p class="eyebrow">{escape(c['eyebrow'])}</p><h1>{c['title']}</h1><p class="intro">{escape(c['intro'])}</p><div class="actions"><a class="button" href="#projects">{escape(c['cta'])} ↓</a><a class="text-link" href="{profile}">{escape(c['profile'])} ↗</a></div></div><aside class="hero-note"><strong>{escape(c['start'])}</strong>{escape(c['note'])}</aside></section>
{section('01',c['apps'],c['apps_intro'],PROJECTS[:2],0,True)}
{section('02',c['android'],c['android_intro'],PROJECTS[2:5],2)}
{section('03',c['integrations'],c['integrations_intro'],PROJECTS[5:],5)}
<section class="section approach" id="approach"><div><span class="section-number">04</span><h2>{c['approach']}</h2><p>{escape(c['approach_body'])}</p><div class="links"><a href="https://github.com/navalcode/spec-evidence-lab">{escape(c['approach_link'])} ↗</a></div></div><ol class="steps">{''.join(f'<li><div><strong>{escape(title)}</strong><span>{escape(body)}</span></div></li>' for title,body in c['steps'])}</ol></section>
<section class="section"><div class="scope"><div><h3>{escape(c['scope_title'])}</h3><p>{escape(c['scope_body'])}</p><div class="links"><a href="https://github.com/navalcode/navalcode/blob/main/MOBILE_ROADMAP{'.es' if es else ''}.md">{escape(c['roadmap'])} ↗</a></div></div><div><h3>{escape(c['history_title'])}</h3><p>{escape(c['history_body'])}</p><div class="links"><a href="{profile}">{escape(c['history_link'])} ↗</a></div></div></div></section></main>
<footer class="footer"><div class="wrap"><p>{escape(c['footer'])}</p><p><a href="https://github.com/navalcode">GitHub</a> · <a href="{c['other_file']}" lang="{'en' if es else 'es'}">{c['language_name']}</a></p></div></footer></body></html>
'''


if __name__ == '__main__':
    for language, filename in [('en', 'index.html'), ('es', 'es.html')]:
        (ROOT / 'docs' / filename).write_text(render(language))
    print('Generated English and Spanish static pages.')
