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
# ALGO IMPORTANTE QUE DEBEMOS ACLARAR CON RESPECTO A "a" ES QUE ES LA CANTIDAD DE SUBPROBLEMAS EN LOS QUE SE
# DIVIDE EL ALGORITMO, MAS NO ES LA CANTIDAD DE NODOS QUE TIENE DICHO ALGORITMO.
# Entonces sabiendo eso, en el merge sort lo que hacemos es dividir en 2 partes cada nodo, lo que significa
# que "a" sería igual a 2. 


# AHORA VAMOS A TRATAR DE HACER ALGUNAS ACLARACIONES RELACIONADAS A LA ECUACIÓN: O(1) if n <= n0:
# Esto significa que si el tamaño de n0, el cual hemos definido en nuestro algoritmo solamente requiere de una
# operación para ser resuelto, entonces podríamos decir de el tiempo big O del algoritmo es de O(1).
# Debemos recordar que n es igual al numero total de elementos en la lista del algoritmo, mientras que n0 sería
# la cantidad de elementos en los cuales nosotros hemos decidido que sea el punto de inflexión de dicho algoritmo.
# Entonces por mera lógica, si hemos decidido que el algoritmo analize 3 como n0 del total de 5 como n, obviamente
# va a tomar 1 solo proceso, lo cual se traduce en O(1).


# en el algoritmo T(n) = O(1) si n < n0 o sino aT(n/b) + C(n) + D(n):
# si el algoritmo no es recursivo entonces se maneja con la segunda parte de la formula. ahora bien
# cuando usamos dicha ecuación, analizamos D(n), que es el tiempo que tarda en dividirse el algoritmo, es decir, 
# el tiempo que toma la operación que este manipulando la recursividad, en el merge sort sería de O(1), ya que no hay
# ninguna operación, sino que solamente se divide y C(n) que es el tiempo u operación que tarda para combinarsen los
# subproblemas, el cual, en merge sort sería la comparación mediante "<" y ">" en los bucles while, lo cual es de 
# big O O(n), debido a que estamos practicamente pasando por cada uno de los elementos.
# Ahora habiendo analizado ambos casos, donde se divide y se combinan de nuevo los subproblemas, podemos tomar el 
# peor de los casos, el cual es al combinarsen de nuevo los subproblemas, es decir O(n).

# Ya sabiendo esto, simplemente contamos en cuantas partes se divide el problema principal y reemplazamos los 
# valores en "a" y "b", que al parecer serían proporcionales, ya que la cantidad en la que se divide el problema
# principal es 2, y la cantidad de subproblemas resultantes sería igualemente de 2.
# Por ello es que la ecuación del algoritmos de recursividad merge sort es T(n) = 2T(n/2) + C(n). (según el analisis
# debería haber sido D(n) pero creo que es debido a que se toma C(n) como una constante general del algoritmo.)


# ALGUNAS ACLARACIONES POR LA INTELIGENCIA ARTIFICIAL RELACIONADO A RELACION DE RECURRENCIA Y COMPLEJIDAD DE TIEMPO:
"""La ecuación T(n) = 2T(n/2) + C(n) es una relación de recurrencia que describe cómo el algoritmo Merge Sort 
divide el problema en subproblemas y combina las soluciones1. En esta ecuación, T(n) es el tiempo total requerido 
para ordenar una lista de n elementos, 2T(n/2) representa las dos llamadas recursivas al algoritmo para ordenar las 
dos mitades de la lista, y C(n) representa el tiempo requerido para combinar las dos listas ordenadas en una sola 
lista1.

Por otro lado, n log n es la complejidad de tiempo del algoritmo Merge Sort. Esta es una medida de cuánto crece el 
tiempo de ejecución del algoritmo a medida que aumenta el tamaño de la entrada2. En otras palabras, si tienes una 
lista de n elementos, el algoritmo Merge Sort puede ordenarla en un tiempo proporcional a n log n2.

La razón por la que ves ambas formas es porque están describiendo diferentes aspectos del algoritmo. La relación 
de recurrencia describe cómo se comporta el algoritmo, mientras que la complejidad de tiempo describe cuánto tiempo 
tarda el algoritmo en ejecutarse en términos del tamaño de la entrada12."""



# AHORA VAMOS A ANALIZAR LA ECUACION MAESTRA EN ALGORITMOS RECURSIVOS:
# las reglas nos dicen lo siguiente:
"""Caso 1: Si f(n) es O(n^c), donde c < log_b(a), entonces la complejidad temporal del algoritmo 
es Θ(n^(log_b(a))).

Caso 2: Si f(n) es Θ(n^c log^k(n)), donde c = log_b(a) y k ≥ 0, entonces la complejidad temporal del algoritmo 
es Θ(n^c log^(n)).

Caso 3: Si f(n) es Ω(n^c), donde c > log_b(a), y si se cumple que af(n/b) ≤ kf(n) para alguna 
constante k < 1 y suficientemente grande n, entonces la complejidad temporal del algoritmo es Θ(f(n))."""

# Vamos a tomar como ejemplo el algoritmo recursivo merge sort el cual es: T(n) = 2T(n/2) + c(n)
# donde: a = 2, b = 2 y f(n) = O(n), ya que es la constante de la función big o
# Ahora procedemos a resolver log_b(a) de la parte de la ecuación c < log_b(a):
# log_2(2) = 1.
# Ahora seguimos con f(n) = O(n), es decir n está elevado a la 1
# Luego hacemos la comparación: log_2(2) = 1 = O(n) = 1, es decir que aplica para el segundo caso, que nos propone
# que los valores de n^c = donde c = log_b(a), el cual nos arroja una ecuacion: Θ(n^c log^(n)).