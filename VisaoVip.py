import sys
import requests
from bs4 import BeautifulSoup
import locale
from googletrans import Translator

#url = "https://visaovip.com/produto/notebook/notebook-gamer-dell-g5-15-5530-intel-core-i7-13650hx-pantalla-full-hd-15-6-16gb-de-ram-1tb-ssd-geforce-rtx4060-8gb-dark-shadow-gris-ingles/42846"
#nombre_archivo = "PresupuestoVisaoVip.html"
#aumento = 1.30  # % que se desea aumentar

locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

print(sys.argv)

if len(sys.argv) != 4:
    print("Uso: script.py <url> <porcentaje_de_aumento> <numero>")
    sys.exit(1)

url = sys.argv[1]
aumento = float(sys.argv[2]) / 100 + 1
numero = sys.argv[3]

nombre_archivo = "VisaoVip-"+numero+".html"

def traducir(texto, idioma_origen='pt', idioma_destino='es'):
    try:
        translator = Translator()
        traduccion = translator.translate(texto, src=idioma_origen, dest=idioma_destino)
        return traduccion.text
    except Exception as e:
        print(f"Error al traducir texto: {e}")
        return texto

page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')

    # Título
    h1_titulo =  soup.find('h1', class_='h1-titulo').text.strip() if soup.find('h1', class_='h1-titulo') else "Título no encontrado"

    h1_titulo = traducir(h1_titulo)

    # Precio con aumento
    span_precio = soup.find_all('span', class_='produto-moeda-outros')[1].text.strip().replace("G$", "").replace(".", "").replace(",", ".") if len(soup.find_all('span', class_='produto-moeda-outros')) > 1 else "0"
    precio_numero = float(span_precio)
    precio_aumentado = precio_numero * aumento
    #precio_formateado = "Precio Contado Gs. {:.0f}".format(precio_aumentado)
    #precio_formateado = "{:.,0f}".format(precio_aumentado)
    #precio_formateado = "{:.0f}".format(precio_aumentado)
    precio_formateado = "{:,.0f}".format(precio_aumentado).replace(",", ".").replace(",", ".")
    # Imágenes
    imagenes_src = ["https://visaovip.com" + img['src'] for img in soup.find_all('img', class_='img-galeria')]



    # Asegurarse de tener exactamente 3 imágenes
    if len(imagenes_src) < 3:
        imagenes_src.extend(["" for _ in range(3 - len(imagenes_src))])

    # Características (Títulos y Valores)
    titulos_y_valores = []
    for bloque in soup.find_all('div', class_='p-grid'):
        titulo = bloque.find('label', class_='produto-titulo').text.strip() if bloque.find('label',
                                                                                           class_='produto-titulo') else ""
        valor = bloque.find('span', class_='produto-valor').text.strip() if bloque.find('span',
                                                                                        class_='produto-valor') else ""
        titulos_y_valores.append([titulo, valor])



    # Crear el contenido HTML
    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="ISO-8859-1">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Información del Producto</title>
    </head>
    <body>
        <h1>{h1_titulo}</h1>

        <div style="display:flex;flex-direction:column;justify-content:center">           
            <div style="display:flex;flex-direction:row;justify-content:center">
                <img src='{imagenes_src[0]}' alt='Imagen Grande' width='640'  >                
            </div>
            <div style="display:flex;flex-direction:row;justify-content:center">
                <div><img src='{imagenes_src[1]}' alt='Imagen Pequeña' width='200'  ></div>
                <div><img src='{imagenes_src[2]}' alt='Imagen Pequeña' width='200'  ></div>
            </div>
        </div>
        <div style="display:flex;flex-direction:column;justify-content:center">
            <h2>Características</h2>
            <table border="1" style="border-collapse:collapse">
                <tr>
                    <th>Título</th>
                    <th>Valor</th>
                </tr>
                {''.join([f"<tr><td>{traducir(titulo)}</td><td>{traducir(valor)}</td></tr>" for titulo, valor in titulos_y_valores if titulo and valor])}
            </table>
        </div>
        <div style="margin-top:40px">
            <b>Precio Contado Gs. {precio_formateado}</b>
        </div>
    </body>
    </html>
    """

    # Guardar el contenido HTML en un archivo
    with open("files/"+nombre_archivo, "w", encoding="ISO-8859-1") as html_file:
        html_file.write(html_content)

else:
    print("Error al realizar la petición:", page.status_code)
