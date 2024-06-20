import streamlit as st
import math

st.title('Cotizador Mercari')

'''
### ¡Bienvenido al cotizador de Mercari México!

Aqui podrás cotizar tus pedidos de Mercari. Las cotizaciones ya incluirán la comisión por proxy.

Asegurate de que el precio de tu producto ya incluya el envío.

'''


p_yenes = st.text_input('Escribe el precio en yenes:')
p_yenes = p_yenes.replace(',', '')

yen_a_peso_paypal = 1/8.1332


try: 
    p_yenes = float(p_yenes)
    if st.button('Cotizar'):
        if p_yenes <= 2000:
             coti = (p_yenes + 300)*yen_a_peso_paypal
        elif p_yenes <= 10000:
             coti = (p_yenes + 500)*yen_a_peso_paypal
        elif p_yenes <= 50000:
             coti = (p_yenes + 1000)*yen_a_peso_paypal
        elif p_yenes <= 100000:
             coti = (p_yenes + 2500)*yen_a_peso_paypal
        else:
            coti = (p_yenes)*1.10*yen_a_peso_paypal
        total = str(math.ceil(coti))
        st.write('El precio a pagar es ', total, 'pesos.')
except (ValueError, TypeError, IndexError):
    st.write ('Debes ingresar solo un número')





### okay let's try now