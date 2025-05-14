from selenium import webdriver


def before_all(context):
    print("before_all")

    PATH = "/Users/olia/work/webdrivers/chromedriver"

    # Configuración del driver de Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Iniciar la ventana del navegador maximizada

    # Inicializar el driver de Chrome
    context.driver = webdriver.Chrome(PATH, options=options)


def before_scenario(context, scenario_name):
    print("before_scenario")


def after_scenario(context, scenario_name):
    pass
    print("after scenario")


def after_all(context):
    context.driver.quit()
