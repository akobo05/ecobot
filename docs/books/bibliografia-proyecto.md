# Bibliografía del proyecto — EcoBot (CC431)

Libros y recursos con **perspectiva práctica** alineados al proyecto (Python + PyGame
+ NumPy + OpenCV: filtros reales y matrices homogéneas 3×3), organizados por unidad
del sílabo. Todos los datos fueron **verificados en la web** (autor, edición, año,
ISBN, disponibilidad legal). Donde un dato no se pudo confirmar, se indica.

**Leyenda de enfoque:** **P** = práctico/aplicado · **T** = teórico · **R** = referencia/consulta.

> El curso usa Gonzalez & Woods como base teórica (el equipo ya lo tiene). Esta lista
> añade lo **práctico** que conecta con el código de EcoBot.

---

## Unidad 1 — Fundamentos de procesamiento de imágenes
*(modelos de color, brillo/contraste, histograma y ecualización, filtros espaciales, dominio de frecuencia, transformaciones, ruido)*

- **Programming Computer Vision with Python** — Jan Erik Solem, O'Reilly, 1.ª ed. (2012). ISBN 978-1449316549. — **P** (base T ligera).
  - Para EcoBot: transformaciones geométricas de imágenes (afines/homografías con NumPy), filtros, descriptores. Conecta con las matrices homogéneas del robot.
  - **GRATIS legal** — borrador final CC BY-NC-ND del autor: http://programmingcomputervision.com/downloads/ProgrammingComputerVision_CCdraft.pdf

- **Practical Python and OpenCV (+ Case Studies), 3rd Ed.** — Adrian Rosebrock, PyImageSearch (2016). *ISBN comercial no verificado (eBook autoeditado).* — **P**.
  - Para EcoBot: histogramas + ecualización, thresholding, gradientes/Sobel — casi un mapa 1:1 de las mecánicas de filtros.
  - **De pago.** (No usar copias no oficiales para NotebookLM.)

- **Hands-On Image Processing with Python** — Sandipan Dey, Packt (2018). ISBN 978-1789343731. — **P**.
  - Para EcoBot: ecualización de histograma, filtros espaciales y de frecuencia, ruido (scikit-image / OpenCV / scipy). Útil para el panel de histograma.
  - **De pago.**

- **OpenCV-Python — Documentación oficial / Tutoriales** — OpenCV.org (v4.x). — **P/R**.
  - Para EcoBot: páginas de Histogram Equalization, Image Gradients/Sobel y Otsu thresholding — el código de referencia exacto. https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html
  - **GRATIS legal** (online).

---

## Unidad 2 — Segmentación, compresión y descripción
*(bordes Sobel/Canny, umbral global/local Otsu, regiones, watershed, compresión, descriptores)*

- **Learning OpenCV 4 Computer Vision with Python 3, 3rd Ed.** — Joseph Howse & Joe Minichino, Packt (2020). ISBN 978-1789531619 (impreso) / 978-1789530643 (eBook). — **P**.
  - Para EcoBot: Canny, thresholding, segmentación, contornos/descriptores, NumPy ↔ Surface. El manual práctico OpenCV-Python más actual para "revelar celdas ocultas".
  - **De pago**; el **código de ejemplo es gratis** en GitHub (PacktPublishing).

- *(También aplican aquí "Practical Python and OpenCV" y "Programming Computer Vision with Python" de la Unidad 1.)*

- **Digital Image Processing, 4th Ed.** — Rafael C. Gonzalez & Richard E. Woods, Pearson (2018). ISBN 978-0133356724. — **T/R**. *(Sílabo ítem a — el equipo ya lo tiene.)*
  - Para EcoBot: el "porqué" matemático de ecualización, Sobel/Canny, Otsu, watershed y descriptores. Respaldo académico para el informe.
  - **De pago** (material de apoyo gratis en imageprocessingplace.com).

---

## Unidad 3 — ML / Deep Learning en imágenes
*(CNN, RNN, U-Net, ViT, GANs, difusión)*

> **Unidad menos central para EcoBot** (el juego no entrena redes). Cobertura ligera,
> salvo que se añada una mecánica "inteligente" futura.

- **Deep Learning with Python, 2nd Ed.** — François Chollet, Manning (2021). ISBN 978-1617296864. — **P** (con T clara).
  - Para EcoBot: CNN para visión y secciones de generación, si se añade un módulo inteligente. El más legible (autor de Keras). **De pago.**

- **Deep Learning for Computer Vision with Python** — Adrian Rosebrock, PyImageSearch (2017). *ISBN comercial no verificado (eBook).* — **P** específico de visión.
  - Para EcoBot: CNNs aplicadas a imágenes en Python. **De pago.**

- *(Gonzalez & Woods 4e también introduce CNNs a nivel teórico — sirve de respaldo sin comprar libro nuevo.)*

---

## Unidad 4 — Videojuegos y gráficos 3D  *(núcleo del proyecto)*
*(PyGame, cámara, personaje, colliders, coordenadas homogéneas, transformaciones afines y su concatenación, OpenGL, GLSL, proyecciones, cámara virtual)*

- **Making Games with Python & Pygame** — Al Sweigart (2012). ISBN 9781469901732 (impreso). — **P**.
  - Para EcoBot: game loop, Surface, eventos, sprites, colisiones; 11 juegos completos. Base directa de la arquitectura.
  - **GRATIS legal** (CC): https://inventwithpython.com/pygame/

- **Invent Your Own Computer Games with Python, 4th Ed.** — Al Sweigart, No Starch Press (2017). ISBN 978-1593277956. — **P**.
  - Para EcoBot: estructuras de juego, secuencias y bucles — útil para diseñar la mecánica de "programar instrucciones" (REPETIR, subrutinas).
  - **GRATIS legal** (CC): https://inventwithpython.com/

- **PyGame — Documentación oficial** — pygame.org (v2.6.x). — **P/R**.
  - Para EcoBot: `pygame.Surface` y `pygame.transform` (scale/rotate/flip) — clave para aplicar OpenCV sobre la Surface y para la cámara. https://www.pygame.org/docs/ref/transform.html
  - **GRATIS legal** (online).

- **Mathematics for 3D Game Programming and Computer Graphics, 3rd Ed.** — Eric Lengyel, Cengage (2011). ISBN 978-1435458864. — **R/T aplicada**. *(Sílabo ítem f.)*
  - Para EcoBot: transformaciones afines, **coordenadas homogéneas, concatenación de matrices**, matrices de proyección y cámara virtual — la base directa de las matrices 3×3 del robot y la cámara.
  - **De pago.**

- **Foundations of Game Engine Development, Vol. 1: Mathematics** — Eric Lengyel, Terathon (2016). ISBN 978-0985811747. — **R/T**.
  - Para EcoBot: álgebra lineal y transformaciones para motores; complemento moderno y conciso al anterior. Opcional si ya se tiene el Lengyel 2011. **De pago.**

### Libros de OpenGL/GLSL del sílabo (referencia de menor prioridad — EcoBot es 2D, no usa OpenGL)
- **Computer Graphics Programming in OpenGL with C++** — V. S. Gordon & J. L. Clevenger, Mercury Learning. 1.ª ed. (2018) ISBN 978-1683922216 (existen 2.ª ed. 2020 y 3.ª ed. 2024). **P** (C++/OpenGL). *(Sílabo ítem b.)* De pago.
- **OpenGL Programming Guide ("Red Book"), 8th Ed.** — Shreiner, Sellers, Kessenich, Licea-Kane, Addison-Wesley (2013). ISBN 978-0321773036. **R**. *(Sílabo ítem c.)* De pago.
- **Interactive Computer Graphics, 6th Ed.** — Angel & Shreiner, Pearson (2012). ISBN 978-0132545235. **T/P**. *(Sílabo ítem d.)* De pago.
- **OpenGL 4 Shading Language Cookbook, 3rd Ed.** — David Wolff, Packt (2018). ISBN 978-1789342253. **P** (GLSL). *(Sílabo ítem g; el sílabo cita la ed. 2011, pero la 3.ª de 2018 es la vigente.)* De pago.
- **Graphics Shaders: Theory and Practice, 2nd Ed.** — Bailey & Cunningham, A K Peters/CRC (2011/2012). ISBN 978-1568814346. **T/P** (GLSL). *(Sílabo ítem h.)* De pago.
- **Radiosity and Realistic Image Synthesis** — Cohen & Wallace, Morgan Kaufmann. ISBN 978-0121782702. **T**. *(Sílabo ítem e; año exacto no verificado — original de los 90.)* Poco relevante para EcoBot. De pago.

---

## Los mejores libros (sin importar precio) y a qué Gem alimentan

Selección "calidad por encima de costo", verificada en web. Útil tanto para el equipo
como para configurar las dos Gems de Gemini (Spec-Gem y Reviewer-Gem).

| Libro | Enfoque | Unidad | Spec-Gem | Reviewer-Gem | Disponibilidad |
|---|---|---|---|---|---|
| **Game Programming Patterns** — Robert Nystrom (2014) | P (patrones) | U4 | ✅ (diseña el intérprete: *Command*, *State*, *Game Loop*) | ✅ (verifica patrones) | **Gratis online**: https://gameprogrammingpatterns.com/ |
| **Computer Vision: Algorithms and Applications, 2e** — R. Szeliski (2022). ISBN 978-3-030-34372-9 | P/T moderno | U1–U3 | ✅ | ✅ | **Gratis** (draft del autor): https://szeliski.org/Book/ |
| **Mathematics for 3D Game Programming & CG, 3e** — E. Lengyel (2011) | R/T aplicada | U4 | ✅ (construir matrices 3×3) | ✅ (verificarlas) | De pago *(sílabo ítem f)* |
| **Fundamentals of Computer Graphics, 5e** — Marschner & Shirley (2021). ISBN 978-0367505035 | T/R | U4 | — | ✅ (coordenadas y transformaciones, autoritativo) | De pago |
| **Digital Image Processing, 4e** — Gonzalez & Woods (2018) | T/R | U1–U2 | (fundamento) | ✅ (verificar filtros) | De pago — ya lo tienes |
| **Learning OpenCV 4 ... with Python 3** — Howse & Minichino (2020) | P | U1–U2 | ✅ (implementar filtros) | — | De pago (código gratis en GitHub) |
| **Making Games with Python & Pygame** — Sweigart (2012) | P | U4 | ✅ (esqueleto PyGame) | — | **Gratis CC**: https://inventwithpython.com/pygame/ |
| **Effective Python, 3e** — Brett Slatkin (2024). ISBN 978-0138172183 | P (calidad de código) | — | — | ✅ (estilo Pythonic) | De pago |
| **Fluent Python, 2e** — L. Ramalho (2022) | P (Python profundo) | — | — | ✅ opcional | De pago |
| **Clean Code** — R. C. Martin (2008) | P (calidad de código) | — | — | ✅ opcional | De pago |
| **Documentación PyGame / OpenCV-Python** | P/R | U1–U2, U4 | ✅ | ✅ | Gratis (online) |

> **Resumen por Gem:**
> - **Spec-Gem** (construir): Game Programming Patterns + Sweigart + Howse(OpenCV) + Lengyel + docs PyGame/OpenCV (+ Szeliski opcional).
> - **Reviewer-Gem** (verificar): Gonzalez & Woods + Lengyel + Effective Python + Game Programming Patterns + docs (+ Marschner / Fluent Python / Clean Code opcionales).
> Detalle de configuración en `../../../gemini-gems/`.

---

## Mínimo imprescindible para EcoBot (equipo de 3)

1. **Making Games with Python & Pygame** (Sweigart, gratis) — esqueleto del juego.
2. **Documentación oficial de PyGame** (gratis) — `Surface`/`transform`, integración NumPy/OpenCV.
3. **Documentación oficial de OpenCV-Python** (gratis) — histograma/ecualización, Sobel, Otsu: las mecánicas centrales.
4. **Mathematics for 3D Game Programming and Computer Graphics** (Lengyel, 2011) — coordenadas homogéneas y concatenación (matrices 3×3 del robot/cámara).
5. **Learning OpenCV 4 ... with Python 3** (Howse & Minichino, 2020) *o* **Practical Python and OpenCV** (Rosebrock) — un práctico de OpenCV-Python para bordes/umbral.

## Recursos ingeribles legalmente en NotebookLM (PDF/HTML gratuito)

- **Making Games with Python & Pygame** — Sweigart (CC): https://inventwithpython.com/pygame/
- **Invent Your Own Computer Games with Python, 4e** — Sweigart (CC): https://inventwithpython.com/
- **Programming Computer Vision with Python** — Solem (borrador CC, PDF): http://programmingcomputervision.com/downloads/ProgrammingComputerVision_CCdraft.pdf
- **Documentación PyGame** (HTML): https://www.pygame.org/docs/
- **Documentación OpenCV-Python** (HTML): https://docs.opencv.org/4.x/ (tutoriales de histograma, gradientes/Sobel, thresholding/Otsu)

> ⚠️ **No** cargues en NotebookLM PDFs de libros de pago (Gonzalez & Woods, Lengyel,
> Howse, Chollet, Rosebrock, los de OpenGL). Aunque circulen copias, no es distribución
> legal. Para esos, usa tus propias notas/resúmenes o el material de apoyo oficial
> gratuito.

---

### Notas de verificación
- **No verificable al 100%:** el año exacto de *Radiosity and Realistic Image Synthesis* (Cohen & Wallace) y los ISBN comerciales de los eBooks de Rosebrock (productos digitales de PyImageSearch sin ISBN impreso estándar).
- **Discrepancias con el sílabo (confirmadas):** el *OpenGL Shading Language Cookbook* del sílabo se cita como "4.0 / 2011", pero la edición vigente es la **3.ª (2018)**; *Computer Graphics Programming in OpenGL with C++* tiene ediciones más nuevas (2020, 2024) que la 2018 del sílabo.
