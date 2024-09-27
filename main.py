import flet as ft


def main(page: ft.Page):
    page.title = "calculadora de IMC"
    page.bgcolor="purple"
    
    txtPeso=ft.TextField(label="ingresa tu peso")
    txtAltura=ft.TextField(label="ingresa tu altura")
    lblIMC=ft.Text("Tu IMC es:")
    
    img=ft.Image(scr="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
                width=200,
                height=200
                
                )
    btnCalcular=ft.ElevatedButton(text="Calcular")
    btnLimpiar=ft.ElevatedButton(text="Limpiar")
    
    
    page.add(
        ft.column(
            controls=[txtPeso,
                      txtAltura,
                      lblIMC
                      ],alignment="CENTER"),
        ft.Row(
            controls=[
                ing
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                    btnCalcular,
                    btnLimpiar
            ],alignment="CENTER")
    )
    

ft.app(target=main,view=ft.AppView.WEB_BROWSER)
