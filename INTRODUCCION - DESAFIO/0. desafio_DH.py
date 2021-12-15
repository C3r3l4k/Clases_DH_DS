{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "884c025b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "161.46341463414635"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cantidad_verano = 126\n",
    "precio_verano = 200\n",
    "cantidad_invierno = 79\n",
    "precio_invierno = 100\n",
    "\n",
    "ventas_verano = cantidad_verano * precio_verano\n",
    "ventas_invierno = cantidad_invierno * precio_invierno\n",
    "total_producto = cantidad_verano + cantidad_invierno\n",
    "\n",
    "media = (ventas_verano + ventas_invierno)/total_producto\n",
    "media"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "d2dc2aa1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "230.9733750889916"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sueldos_empleados = [2536, 2137, 2448, 2121,2622] #sueldos buenos aires\n",
    "empleados_buenos_aires = 5 #empleados en baires\n",
    "\n",
    "empleados_cordoba = 6 #empleados en cordoba\n",
    "sueldo_promedio_cordoba = 2550 #sueldo promedio en cordoba\n",
    "desvio_estandar_cordoba = 250 #desvio estandar cordoba\n",
    "\n",
    "sueldo_promedio_buenos_aires = sum(sueldos_empleados)/empleados_buenos_aires\n",
    "\n",
    "sueldo_empleados_desvio = []\n",
    "\n",
    "for i in sueldos_empleados: # empezamos el calculo de la varianza\n",
    "    i = round(i - sueldo_promedio_buenos_aires,2) # valor sueldo - sueldo promedio\n",
    "    a = i ** 2 # diferencia al cuadrado\n",
    "    sueldo_empleados_desvio.append(a)\n",
    " \n",
    "varianza = sum(sueldo_empleados_desvio) / (empleados_buenos_aires - 1) #formula varianza\n",
    "\n",
    "desvio_estandar = varianza ** .5 # raiz cuadrada de la varianza\n",
    "    \n",
    "desvio_estandar"
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
