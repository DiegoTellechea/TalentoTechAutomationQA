#  Pre-Entrega - Automation Testing con Selenium

Proyecto de pre-entrega del curso de QA Automation, donde pongo en práctica los conocimientos aprendidos hasta la Clase 8 utilizando Python, Selenium WebDriver y Pytest.

El sitio utilizado para realizar las pruebas es **SauceDemo**, una aplicación web creada especialmente para practicar automatización y testing.

---

##  Objetivo del proyecto

El objetivo es automatizar algunos flujos básicos de navegación e interacción dentro de SauceDemo y realizar validaciones sobre los elementos de la página.

En este proyecto se automatizaron principalmente:

- Login de usuario.
- Verificación del catálogo de productos.
- Verificación de elementos de la interfaz.
- Agregado de un producto al carrito.
- Verificación del contador del carrito.
- Verificación del producto dentro del carrito.

Además, se buscó mantener el código organizado y reutilizable mediante funciones auxiliares.

---

##  Tecnologías utilizadas

- **Python**
- **Selenium WebDriver**
- **Pytest**
- **Git**
- **GitHub**
- **Chrome / ChromeDriver**

---

##  Estructura del proyecto

```text
Preentrega/
│
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_cart.py
│
├── utils/
│   └── helpers.py
│
├── reports/
│   └── reporte.html
│
├── pytest.ini
├── README.md
└── requirements.txt