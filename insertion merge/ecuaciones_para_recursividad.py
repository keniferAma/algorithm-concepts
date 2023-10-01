"""T(n) = 2T(n/2) + n: Esta es una ecuación de recurrencia específica para el algoritmo Merge Sort. 
Aquí, ‘n’ es el tamaño del problema (por ejemplo, el número de elementos en la lista que estamos ordenando), 
‘2’ es el número de subproblemas en los que dividimos el problema original (en Merge Sort, siempre dividimos 
la lista en dos mitades), y ‘n/2’ es el tamaño de cada subproblema. El término ‘+ n’ representa el tiempo que 
toma combinar las soluciones de los subproblemas en la solución del problema original.
OJO, TENER EN CUENTA QUE ESTA ECUACION APLICA PARA ALGORITMOS QUE DE VERDAD SE DIVIDAN EN 2 PARTES PARA TRATAR
DE RESOLVERLO, POR EJEMPLO EN EL CASO DE UN ALGORITMO FACTORIAL NO APLICARÍA LA MISMA ECUACIÓN, SINO QUE POR EL
CONTRARIO SERÍA DE TIPO T(n) = T(n-1) + O(1), ESTE 1 REPRESENTA EL TIEMPOR QUE REPRESENTA EN CADA NIVEL DE EJECUCIÓN
DE NUESTRO ALGORITMO DE RECURSION. POR EJEMPLO EN UN CASO HIPOTETICO DE FACTORIAL 3, TENDRÍAMOS APROXIMADAMENTE
4 NIVELES EN EL STUCK, LO QUE SIGNIFICA QUE HAY 4 EJECUCIONES DE N MULTIPLICADO POR SU LLAMADO RECURSIVO.
Y DICHA OPERACION ES IGUAL A O(1) YA QUE ES UNA SIMPLE MULTIPLICACION DE 2 NUMEROS.

T(n) = aT(n/b) + D(n) + C(n): Esta es una ecuación de recurrencia más general que puede aplicarse a cualquier 
algoritmo de divide y vencerás, no solo a Merge Sort. Aquí, ‘a’ es el número de subproblemas en los que dividimos 
el problema original, ‘n/b’ es el tamaño de cada subproblema, ‘D(n)’ es el tiempo que toma dividir el problema en 
subproblemas, y ‘C(n)’ es el tiempo que toma combinar las soluciones de los subproblemas en la solución del 
problema original."""



# Ahora vamos a tratar de poner en contexto de como usar estas ecuaciones con algoritmos reales. 
# En el caso del algoritmo merge sort resuelto mediante recursividad, usando la ecuación: T(n) = 2T(n/2) + n,
# podemos darnos cuenta cual es el valor de la constante n y para ello debemos dibujar las respectivas 
# ramificaciones que va a llevar dicho algoritmo. Por ejemplo en el primer nivel vamos a tener n que es el arreglo
# original, luego ese arreglo lo vamos a dividir entre 2 (precisamente eso es lo que hacemos en algoritmos recursivos) 
# y tendremos 2 ramas cada una con un valor de n/2, de aquí vamos a ramificar en 4 ramas, es decir n/4. 
# De esta manera podemos encontrar un patrón especifico de cada nivel o nodo del arbol, el cual, en nuestro caso 
# es de valor "n", es decir que nuestro algoritmo recursivo tiene una constante de n, ya que n/2 + n/2, que 
# teniamos en el primer nodo nos da como resultado n. Y n/4 + n/4 + n/4 + n/4 que tenemos en el segundo nivel o 
# segundo nodo es igual también a 1, en nuestro caso es igual a n, lo cual nos indica que ya tenemos un patrón 
# especifico de la constante n, el cual es de n; es decir, es constante en cada uno de los niveles de la recurrencia 
# con respecto a su base que es "n". (OJO, ESTAMOS HABLANDO DE N DIRECTAMENTE, ES DECIR, DE LA ÚLTIMA PARTE DE NUESTRO 
# ALGORITMO) 

# Ahora bien, cuando tenemos este tipo de algoritmos, donde dividimos por 2 cada nodo, siempre se aplica log n 
# (con su base por supuesto de 2, el cual fue el valor por que estmas dividiendo cada nodo) y luego contamos 
# la cantidad de nodos que tuvo nuestro arbol, es decir que nuestra ecuación final sería n * log n teniendo 
# como la primera n la multiplicación de n * la cantidad de nodos que contiene el arbol en cada una de su 
# recursividad


# Algo para tener en cuenta: cn, es decir la constante de n está relacionada con la manera como se divide y 
# posteriormente se unen de nuevo las recursividades, o cuanto se demora en entrar y salir cada funcion 
# en el stack o pila, esto va determinado por la operación que une dicha constante con las recursividades.

# una ecucacion muy usada para analisis de este tipo de algoritmo de merge sort es: T(n) = aT(n/b) + D(n) + C(n)
# donde: aT = a la cantidad de subprocesos en los cuales se divide el problema, n/b = en cuantas partes se divide
# el problema por cada ramificación, D(n) = al tiempo que se utiliza en dividir cada ramificación, 
# y por último C(n) = al tiempo que tarda en unir o combinar o conquistar de nuevo cada nodo o subproceso. 