API_KEY = '0126da41500b4bcdf6e343fcb9487bfe'
import requests
def obtener_clima(ciudad, API_KEY, unidades='metric', idioma='es'):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units={unidades}&lang={idioma}'
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        pais = datos['sys']['country']
        sensacion_termica = datos['main']['feels_like']
        descripcion = datos['weather'][0]['description']
        temperatura = datos['main']['temp']
        humedad = datos['main']['humidity']
        viento = datos['wind']['speed']
        texto = (f'\nClima en {ciudad}, {pais}.\n'
                f'=============================\n'
                f'Temperatura: {temperatura}°C\n'
                f'Sensación térmica: {sensacion_termica}°C\n'
                f'Descripción: {descripcion}\n'
                f'Humedad: {humedad}%\n'
                f'Viento: {viento} m/s\n')
        return texto
    else:
        return f'Error al obtener datos del clima para {ciudad}.'

ciudad = 'Zafra'
print(obtener_clima(ciudad, API_KEY))