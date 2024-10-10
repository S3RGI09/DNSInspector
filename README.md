# DNS Inspector

**DNS Inspector** es un script de Python que recopila información de DNS para un dominio específico. Este programa te permite obtener diversos tipos de registros DNS, facilitando la auditoría y análisis de la configuración de DNS de un dominio.

## Funciones

- Recopila Registros DNS: Obtiene diferentes tipos de registros, incluyendo:
  - Registros A (dirección IPv4)
  - Registros AAAA (dirección IPv6)
  - Registros CNAME (nombre canónico)
  - Registros MX (intercambio de correo)
  - Registros NS (servidores de nombres)

## Requisitos

- Python 3.x
- La biblioteca `dnspython` debe estar instalada. Puedes instalarla con:
  pip install dnspython

## Cómo Usar

1. **Descarga el script**: Clona o descarga este repositorio en tu máquina.
2. **Ejecuta el script**:
   ```
   python dnsinspector.py
   ```
3. **Introduce el dominio**: Cuando se te solicite, ingresa el dominio del cual deseas recopilar información de DNS (por ejemplo, `example.com`).

## Ejemplo de Salida

Al ejecutar el script, recibirás un informe similar al siguiente:
```
Introduce el dominio para recopilar información de DNS (ejemplo.com): example.com  
Dirección IP de example.com: 93.184.216.34

Información de DNS recopilada:  
A registros: ['93.184.216.34']  
AAAA registros: []  
CNAME registros: []  
MX registros: []  
NS registros: ['a.iana-servers.net.', 'b.iana-servers.net.']
```
## Notas

- Este script debe usarse solo en tu propia máquina o en sistemas para los cuales tienes permiso explícito para escanear.
- Asegúrate de tener permisos adecuados para acceder a la información de DNS del dominio que deseas investigar.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, no dudes en abrir un issue o enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
