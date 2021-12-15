{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4cf9b3c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Escribí una función que reciba un número y lo compare con el 17. Si el número es menor, la función tiene que devolver la diferencia entre ese número y 17; si es mayor, la función debe devolver el doble del valor absoluto de la diferencia.\n",
    "\n",
    "def difference(numero):\n",
    "  \n",
    "  if numero < 17:\n",
    "    return 17 - numero\n",
    "  elif numero > 17:\n",
    "    return 2 * abs(17 - numero)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cd9b0894",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Escribí una función que reciba un número y devuelva True si el número se encuentra entre 100 y 1000 (incluidos), y False en caso contrario.\n",
    "\n",
    "def near_thousand(numero):\n",
    "    return 100 <= numero <= 1000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d876c591",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Escribí una función que calcule la suma de tres números dados, y si los tres números son iguales, que devuelva el triple de su suma.\n",
    "\n",
    "def suma_tres(a,b,c):\n",
    "  \n",
    "  suma = a + b + c\n",
    "  \n",
    "  if a == b == c:\n",
    "    return suma * 3\n",
    "  else:\n",
    "    return suma"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "01b4a826",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Escribí una función que reciba una lista de números enteros y devuelva la cantidad de veces que aparece el número 4 en ella. \n",
    "\n",
    "def cuenta_cuatro(numero):\n",
    "  lista = list(numero)\n",
    "  a = lista.count(4)\n",
    "  return a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d3e96999",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Escribí una función que reciba un número y un listado de números (en ese orden) y devuelva True si el número pertenece a la lista. Si el número no se encuentra presente, la función debe incluirlo al final de la lista y devolverla.\n",
    "def check(n, lista):\n",
    "  n = n\n",
    "  lista = list(lista)\n",
    "  if lista.count(n) == 1:\n",
    "    return True\n",
    "  else:\n",
    "    lista.append(n)\n",
    "    return lista\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4c37cf5c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Escribí una función que reciba una lista y concatene los elementos de la lista en un único string.\n",
    "\n",
    "def concat_string(lista):\n",
    "  lista = \"\".join(lista)\n",
    "  return lista"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9a688713",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Escribí una función que reciba una lista de números y devuelva los pares de esa lista. Si alguno de los números es el 248, la lista no debería incluirlo.\n",
    "\n",
    "def stop_248(lista):\n",
    "  pares = []\n",
    "  for n in lista:\n",
    "    if n % 2 == 0 and n != 248:\n",
    "      pares.append(n)\n",
    "  return pares"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f198ecea",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Escribí una función que tome una lista y devuelva True si hay dos números iguales, y False si son todos distintos\n",
    "def repetidos(lista):\n",
    "    indice_c = -1\n",
    "    for elemento in lista:\n",
    "        indice_c = -1\n",
    "        indice = lista.index(elemento)\n",
    "        for comparacion in lista:\n",
    "            indice_c += 1\n",
    "            if indice_c == indice:\n",
    "                continue \n",
    "            elif elemento == comparacion: \n",
    "                return True\n",
    "    return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "40c55dce",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Escribí una función que reciba un número y devuelva True si es número primo, y False en caso contrario.\n",
    "def primos(num):\n",
    "    if num == 1 or num == 0:\n",
    "        return False\n",
    "    elif num == 2:\n",
    "        return True\n",
    "    elif num > 2:\n",
    "        for divisor in range (2,num):\n",
    "            if num % divisor == 0:\n",
    "                return False\n",
    "            elif num % divisor != 0 and divisor == num-1:\n",
    "                return True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "30797979",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Escribí una función que reciba una lista y devuelva otra lista eliminando los valores repetidos.\n",
    "def unicos(lista):\n",
    "  nueva_lista = []\n",
    "  \n",
    "  for i in lista:\n",
    "    if i not in nueva_lista:\n",
    "      nueva_lista.append(i)\n",
    "  return nueva_lista"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fec13b88",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Escribí una función que reciba una lista y devuelva otra lista con los valores únicos de forma ordenada.\n",
    "def lista_de_unicos(lista):\n",
    "  return list(sorted(set(lista)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "dff954af",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Escribí una función que devuelva una lista con todos los cuadrados de los números entre 1 y 30 (incluidos).\n",
    "def cuadrados():\n",
    "  return [i**2 for i in range(1,31)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "af4ae4d8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Escribí una función que, dado un número, devuelva una lista con los los números impares comprendidos entre 0 y ese número (sin incluirlo). Como condición, la función se debe construir con una lista por comprensión.\n",
    "def impares(numero):\n",
    "  return [ x for x in range(numero) if x%2 !=0]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
