import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from app.data.paciente import Paciente

# opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")

# carga del driver
driver_path = "../driver/chromedriver"
driver = webdriver.Chrome(driver_path, chrome_options=options)

# urls
consulta_url = "https://sacatepequez.mspas.gob.gt/sigsa3/sigsa3consulta.aspx"
sigsa_url = "https://sacatepequez.mspas.gob.gt/Login.aspx?ReturnUrl=%2fdefault.aspx"
sigsa3_url = "https://sacatepequez.mspas.gob.gt/Sigsa3/default.aspx"


def cargar_pagina(user: str, password: str, responsable: str, mes: str):
    try:

        # inicializar navegador
        driver.get(sigsa_url)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "Login1_UserName"))
        ).send_keys(user)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "Login1_Password"))
        ).send_keys(password)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "Login1_LoginButton"))
        ).click()

        driver.get(sigsa3_url)

        # filtro de personal
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.NAME, "ctl00$MainContent$TxtMes"))
        ).send_keys(mes)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.NAME, "ctl00$MainContent$TxtAno"))
        ).send_keys("2021")
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.NAME, "ctl00$MainContent$Chktodo"))
        ).click()
        time.sleep(1)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_cmb_Responsable"))
        ).send_keys(responsable)
        time.sleep(1)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_lnkFiltrar"))
        ).click()
        time.sleep(1)

        # editar registros del personal
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.ID, "ctl00_MainContent_GrdResul_ctl02_lnkEditar")
            )
        ).click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_lnkAgregar"))
        ).click()
        time.sleep(1)
    except TimeoutException as e:
        print(e)


def buscar_paciente(dia: int, paciente: Paciente):
    try:
        # input dia
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_TxtDia"))
        ).send_keys(dia)
        # boton buscar persona
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_lnkBuscarP"))
        ).click()
        time.sleep(1)

        # inputs nombres
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_TxtNombre1"))
        ).send_keys(paciente.primer_nombre)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_TxtNombre2"))
        ).send_keys(paciente.segundo_nombre)

        # inputs apellidos
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_TxtApellido1"))
        ).send_keys(paciente.primer_apellido)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_TxtApellido2"))
        ).send_keys(paciente.segundo_apellido)

        # boton filtrar
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_lnkFiltrarP"))
        ).click()
        time.sleep(2)
        # primer resultado dxgvDataRow_PlasticBlue
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "dxgvDataRow_PlasticBlue"))
        ).click()

        # guarda los nombres de los encontrados
        f = open("registros/ingresados.txt", "a")
        f.write("\n" + f"Dia: {dia}, paciente: {paciente}")
        f.close()
        time.sleep(2)

    except TimeoutException as e:
        # sale si no encuentra personas
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.ID, "ctl00_MainContent_btnCancelarSeleccion")
            )
        ).click()
        # guarda los nombres de los no encontrados
        f = open("registros/no-ingresados.txt", "a")
        f.write("\n" + f"Dia: {dia}, paciente: {paciente}")
        f.close()
        print(f"Persona no encontrada: {paciente}", e)
        # recargar pagina para evitar errores
        driver.get(consulta_url)
        time.sleep(1)


def ingresar_paciente(cie: str, ingresar: bool):
    try:
        # select tipo consulta ID ctl00_MainContent_cmbConsulta
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_cmbConsulta"))
        ).send_keys("2")
        time.sleep(1)
        # boton agregar motivo de consulta ID ctl00_MainContent_lnkNuevoD
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_lnkNuevoD"))
        ).click()
        time.sleep(1)

        # input cie 10 set keys ID ctl00_MainContent_TxtIdCie
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_TxtIdCie"))
        ).send_keys(cie)
        # boton filtrar motivo ID ctl00_MainContent_lnkFiltrarD
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_lnkFiltrarD"))
        ).click()
        time.sleep(2)

        # motivo encontrado classname dxgvDataRow_PlasticBlue
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//table[@id='ctl00_MainContent_GrdBuscaD']/tbody/tr[1]")
            )
        ).click()
        time.sleep(2)

        # boton agregar medicamento ID ctl00_MainContent_lnkNuevoM
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_MainContent_lnkNuevoM"))
        ).click()
        time.sleep(1)

        # checkbox no aplica ID ctl00_MainContent_Chk_noaplica
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "ctl00_MainContent_Chk_noaplica"))
        ).click()
        time.sleep(1)
        if ingresar:
            """ GUARDAR """
            # aboton guardar ID ctl00_MainContent_LnkGrabarC
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(
                (By.ID, 'ctl00_MainContent_LnkGrabarC'))).click()
            time.sleep(2) 

        # recargar pagina para evitar errores
        driver.get(consulta_url)
        time.sleep(1)

    except TimeoutException as e:
        print(e)
