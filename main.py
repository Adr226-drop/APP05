import flet as ft

def calcular_imc(txtPeso,txtAltura,lblIMC,page):
    try:
        peso=float(txtPeso.value)
        altura=float(txtAltura.value)
        imc=peso/(altura**2)
        lblIMC.value=f"Tu IMC es: {imc:.2f}"
        page.update()
        
        #funcion para cerrar cuadro de dialogo
        def cerrar_dialogo():
            page.dialog.open=False
            page.update()
        
        #validar condiciones del IMC
            if imc<18.5:
                dialog=ft.AlertDialog(
                    title=ft.Text("Resultado de IMC"),
                    content=ft.Text("actualmente estas bajo de peso"),
                    actions=[ft.TextButton("OK", on_click=cerrar_dialogo)],
                )
            elif imc >= 18.5 and imc<24.9:
                dialog=ft.AlertDialog(
                    title="peso normal",
                    content="Tu imc indica que tienes un peso normal"
                    actions=[
                        ft.TextButton(text="cerrar" on_click=cerrar dialogo)
                        
                        


    except ValueError:



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
            c],alignment="CENTER"),
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



