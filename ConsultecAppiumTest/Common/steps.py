from behave import given, when, then
from Common import functions, config
import pdb


@given("estoy en la pantalla de Login")
def OpenCT(context):
    context.driver = functions.OpenApp(config.host, config.desire_cap)
    pass

@when("hago click en el {element}")
def element_click(context, element):
    type = config.LOCATORS_Login[element]['type']
    text = config.LOCATORS_Login[element]['text']
    e = functions.locate(context, type, text)
    e.click()
    return e


@then("el teclado se habilita")
def keyboard_is_visible(context):
    b = context.driver.is_keyboard_shown()
    return b

@then("puedo introducir texto en el {element}")
def keyboard_works(context, element):
    test = "ABC123abc"
    e = element_click(context, element)
    e.send_keys(test)
    return e.text == test

@then("el {element} esta habilitado")
def is_available(context, element):
    e = element_click(context, element)
    return e.is_enabled()

@when("introduzco '' en el {element}")
def no_introducir_texto(context, element):
    pass

@when("introduzco '{value}' en el {element}")
def introducir_texto(context, value, element):
    e = element_click(context, element)
    e.send_keys(value)
    return

@then("aparece un mensaje de Error diciendo que el login no es exitoso")
def Login_no_exitoso(context):
    print("Login no exitoso")


@then("la sesion inicia exitosamente")
def Login_Exitoso(context):
    print("Login Exitoso!")