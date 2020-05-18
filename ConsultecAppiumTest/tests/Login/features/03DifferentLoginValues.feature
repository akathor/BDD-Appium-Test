Feature: Introducir valores invalidos no permite el Login

	Scenario Outline: Hacer click en Entrar con Usuario = <usrvalue> y Password = <pwdvalue>
		Given estoy en la pantalla de login
        when hago click en el Campo Username
        and introduzco '<usrvalue>' en el Campo Username
        and hago click en el Campo Password
        and introduzco '<pwdvalue>' en el Campo Password
		and hago click en el Boton Entrar
		then aparece un mensaje de Error diciendo que el login no es exitoso

        Examples:
        |usrvalue|pwdvalue|
        |||
        ||clave|
        |usuario||
        |User58|clave|
        |usuario|Consultec|

    Scenario: La sesion inicia exitosamente con un usuario y password validos
        Given estoy en la pantalla de login
        when hago click en el Campo Username
        and introduzco 'usuario' en el Campo Username
        and hago click en el Campo Password
        and introduzco 'clave' en el Campo Password
		and hago click en el Boton Entrar
		Then la sesion inicia exitosamente