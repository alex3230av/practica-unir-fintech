# Repo para EIEC - DevOps - UNIR

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.

---

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Ejecución

```
python3 main.py <filename> <dup> [order]
```

- filename: **ruta** al fichero que contiene la lista de palabras, una por línea
- dup: **yes|no**, yes para eliminar palabras duplicadas, no para mantener la lista
- order (opcional): **asc|desc**, orden ascendente (por defecto) o descendente

### Con Makefile

```
make run          # Ejecuta dentro de un contenedor Docker
make run-local    # Ejecuta en local con python3, sin Docker
make run-local FILE=palabras.txt DUP=no ORDER=desc
```

Por defecto se usa `FILE=palabras.txt`, `DUP=yes` y `ORDER=asc`.

## Ejecución de prueba

Contenido de `palabras.txt`:

```
pera
manzana
zanahoria
banana
kiwi
manzana
uva
fresa
banana
naranja
```

Orden ascendente eliminando duplicados:

```
$ python3 main.py palabras.txt yes asc
Words will be read from file palabras.txt
['banana', 'fresa', 'kiwi', 'manzana', 'naranja', 'pera', 'uva', 'zanahoria']
```

Orden descendente manteniendo duplicados:

```
$ python3 main.py palabras.txt no desc
Words will be read from file palabras.txt
['zanahoria', 'uva', 'pera', 'naranja', 'manzana', 'manzana', 'kiwi', 'fresa', 'banana', 'banana']
```

Sin argumentos:

```
$ python3 main.py
The file must be provided as the first argument
The second argument indicates whether duplicates should be removed (yes|no)
The optional third argument indicates the sort order (asc|desc)
```
