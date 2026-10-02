from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def iniciar_sesion(driver, wait):
    usuario = wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )

    password = wait.until(
        EC.presence_of_element_located((By.ID, "password"))
    )

    boton_login = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )

    usuario.send_keys("standard_user")
    password.send_keys("secret_sauce")

    boton_login.click()