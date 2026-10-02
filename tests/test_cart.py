from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#importamos la funcion auxiliar de iniciar sesion
from utils.helpers import iniciar_sesion


def test_cart():
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        # funcion auxiliar para login
        iniciar_sesion(driver, wait)

        # Agregar Sauce Labs Backpack al carrito
        boton_agregar = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        )

        boton_agregar.click()

        # Verificar contador
        contador = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            )
        )

        assert contador.text == "1"

        # Ir al carrito
        carrito = wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        )

        carrito.click()

        # Verificar que estamos en el carrito
        assert "/cart.html" in driver.current_url

        # Verificar producto
        producto = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )

        assert producto.text == "Sauce Labs Backpack"

    finally:
        driver.quit()