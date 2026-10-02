from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import iniciar_sesion


def test_inventory():
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)

    try:
        # Abrimos SauceDemo
        driver.get("https://www.saucedemo.com/")

        # Iniciamos sesión usando la función auxiliar
        iniciar_sesion(driver, wait)

        # Verificamos título de la página
        assert driver.title == "Swag Labs"

        # Verificamos que existan productos
        productos = wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item")
            )
        )

        assert len(productos) > 0

        # Tomamos el primer producto
        primer_producto = productos[0]

        # Obtenemos nombre y precio
        nombre_producto = primer_producto.find_element(
            By.CLASS_NAME,
            "inventory_item_name"
        ).text

        precio_producto = primer_producto.find_element(
            By.CLASS_NAME,
            "inventory_item_price"
        ).text

        # Validamos nombre y precio
        assert nombre_producto == "Sauce Labs Backpack"
        assert precio_producto == "$29.99"

        # Verificamos que el menú esté presente
        menu = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "react-burger-menu-btn")
            )
        )

        assert menu.is_displayed()

        # Verificamos que el filtro esté presente
        filtro = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "product_sort_container")
            )
        )

        assert filtro.is_displayed()

    finally:
        driver.quit()