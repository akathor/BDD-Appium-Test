Feature: Funcionalidad del teclado en el Login

    Scenario Outline: El teclado es accesible cuando hago tap en <campo>

        Given estoy en la pantalla de Login
        when hago click en el <campo>
        then el teclado se habilita
        and puedo introducir texto en el <campo>

        Examples:
            |    campo     |
            |Campo Username|
            |Campo Password|