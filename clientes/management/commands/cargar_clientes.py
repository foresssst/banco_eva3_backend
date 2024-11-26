import pandas as pd
from django.core.management.base import BaseCommand
from clientes.models import Cliente

class Command(BaseCommand):
    help = 'Carga datos limpios desde el archivo CSV al modelo Cliente, reemplazando los existentes.'

    def handle(self, *args, **kwargs):
        # Ruta del archivo CSV limpio
        csv_path = 'clientes_banco_limpio.csv'

        try:
            # Leer el archivo CSV
            clientes_df = pd.read_csv(csv_path)

            # Eliminar todos los registros existentes en la tabla
            Cliente.objects.all().delete()

            # Iterar sobre el DataFrame y cargar los datos
            for _, row in clientes_df.iterrows():
                try:
                    Cliente.objects.create(
                        cliente_id=row['Cliente_ID'],
                        edad=int(row['Edad']),
                        genero=row['Genero'],
                        saldo=float(row['Saldo']),
                        activo=bool(int(row['Activo'])),
                        nivel_de_satisfaccion=int(row['Nivel_de_Satisfaccion']),
                    )
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error al procesar el cliente {row['Cliente_ID']}: {e}"))

            self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente en el modelo Cliente'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Archivo no encontrado en la ruta especificada: {csv_path}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error inesperado: {e}"))
