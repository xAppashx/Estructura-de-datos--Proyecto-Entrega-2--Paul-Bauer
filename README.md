# Estructura-de-datos--Proyecto-Entrega-2--Paul-Bauer
Segunda entrega de mi proyecto para el curso de Estructura de Datos. Inventario con estrucuta de arbol B+

La meta con esa entrega es comparar 2 estructuras de datos. 
En la primera iteracion de mi proyecto, hize un manejador de inventario usando como estructura de datos una lista encadenada.
Para esa intrega, hare un codigo cual me hace exactamente lo mismo que el manejador de inventario original, solo que esa ves, usando un arbol como estructura de datos.


Llegue a hacer varias iteraciones para un mismo codigo.
Mi primer paso para ese proyecto, fue "crear" la estructura de arbol B+.
Realmente, busque un codigo en internet cual implementaba esa estructura de dato, y lo re-escribi para que contenga mis variables y que lo pueda adaptar a mi necesidad.
Una ves re-escrito, lo corri para ver si funccionaba. Ese codigo es el CodigoTreeV1, la primera version del arbol que implemente.

El echo que simplemente corria no lo hacia terminado. Entonces segui dessarollando ese codigo, asta lleguar al CodigoTreeV2, la segunda version, simplemente la primera, pero mas desarrollada. 
Esa version lleva nodos conteniendo todos los datos que quiero salvar en esos. En el codigo original que encontre en internet, y en el CodigoTreeV1, cada nodo lleva asta 2 variables.
En el CodigoTreeV2, los nodos tienen 5 variables.
Pero por hacer muchas modificaciones, termine destruyendo la estructura del arbol. Todos los nodos estaban salvados en el root. No tenia ningun sentido.
Al darme cuenta de ese error, simplemente deje esa iteracion del codigo como estaba. No tenia sentido seguir en ese.

Entonces cree el CodigoTreeV3, sin basarme ni en el CodigoTreeV1 ni en el CodigoTreeV2. Volvi a empezar basandome en el codigo que encontre originalmente en internet.
Lo cree de una ves con nodos cuales contienen 5 variables. Solo que esa ves, si verifique que estaba realmente creando un arbol. 

La ultima version del CodigoTree es la version 4. Esa version es ya la completa cual uso para mi proyecto. Es muy similar al CodigoTreeV3, solo que ya completada y funccionando con el Main.
Hablando del Main, no subi todas las iteraciones de ese codigo que realise, por 2 razones. Primero: Es muy similar al Main de la primera entrega de mi proyecto. A final de cuenta, esos 2 proyectos hacen lo mismo.
La segunda razon es porque modifique poquisimo ese codigo. Lo construi como necesitaba, y lo monte muy rapido. No sentia que publicar como estaba el codigo en cada momento en el cual tomaba un descando era muy necesario ni valioso.

Despues vino el TreeFacturas. Ese codigo lleva la misma estructuras que el CodigoTreeV4. Es tambien un arbol, con el proposito de almazenar facturas y no los elementos en el inventario. Realmente es basicamente lo mismo que el CodigoTreeV4 en su estructura. Lo cree en poquisimo tiempo.

Ya esos 3 codigos creados, tengo mi inventario implementando un B+ tree creado. Pero dejarlo asi hubiera sido tomar el camino simple. 
Tenia otras cosas en mente, y quize realizarlas. 
Como mencione anteriormente, quize comparar las diferencias de tiempos que se tomaba una lista encadenada con un arbol en devolver un nodo cuando le damos el codigo de ese. 
Para esa realisación, cree 2 nuevos codigos. InventarioListTimingTest, cual es la lista encadenada que cree para la primera entrega de ese proyecto. Y esta el CodigoTreeTimingTest.
Lo que hacen esos codigos son ingresar 10 000 nodos en sus estructuras de datos correspondientes, y devolver cuanto tiempo se toman para devolver cada nodo de forma individual. Las comparaciones en los resultados estan dados por la imagen llamada "GraficaComparacionesTiempos".

Notamos que con la estrucutra de arbol, los tiempos tomados son ridiculamente mas rapido que con la lista encadenanda. 
Aunque sabia que las estructuras de arboles eran mas adecuados para grandes cantidades de datos (o nodos), tengo que admitir que estoy bastante satisfecho del echo que lo pude averiguar por mi cuenta y sacar mis propias conclusiones.
