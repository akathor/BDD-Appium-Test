Feature: Inicializacion del Login
	Scenario Outline: El <element> esta habilitado
		Given estoy en la pantalla de Login
		Then el <element> esta habilitado

		Examples:
		|    element     |
		|  Boton Entrar  |
		| Campo Username |
		| Campo Password |