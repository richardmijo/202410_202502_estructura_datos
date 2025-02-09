# Implementación de Árbol Binario para Evaluación de Expresiones Aritméticas

## Descripción
Este proyecto implementa un **Árbol Binario de Expresión** para evaluar expresiones aritméticas escritas en **notación postfija** (notación polaca inversa). El árbol se construye a partir de una cadena que representa la expresión en postfijo y permite evaluar su resultado.

Se incluyen métodos para:
- **Construcción del árbol binario** a partir de la expresión postfija.
- **Recorridos del árbol** en inorden, preorden y postorden.
- **Evaluación del árbol** para calcular el resultado de la expresión.

## Funcionamiento del Código

### 1. Construcción del Árbol de Expresión
El árbol se construye utilizando una pila (**stack**). Se recorre la expresión postfija y:
- Si el carácter es un número, se crea un nodo hoja y se apila.
- Si el carácter es un operador (`+`, `-`, `*`, `/`), se extraen dos nodos de la pila, se asignan como hijos izquierdo y derecho, y el operador se vuelve el nodo raíz de esa subexpresión.
- Al finalizar, el último nodo en la pila será la raíz del árbol.

### 2. Recorridos del Árbol
Se implementan los siguientes métodos de recorrido:
- **Inorden (izquierda - raíz - derecha):** Representa la expresión de forma natural.
- **Preorden (raíz - izquierda - derecha):** Se usa para reconstrucción de la expresión.
- **Postorden (izquierda - derecha - raíz):** Útil para evaluar expresiones en postfijo.

### 3. Evaluación del Árbol
La evaluación recorre el árbol de manera recursiva:
- Si el nodo es un número, se devuelve su valor.
- Si es un operador, se evalúan los subárboles izquierdo y derecho y se aplica la operación correspondiente.

## Código de Ejemplo

```python
from expression_tree import ExpressionTree

postfix_expression = "23*54*+9-"  # Representa (2*3) + (5*4) - 9
exp_tree = ExpressionTree(postfix_expression)

print("Recorrido Inorden:")
exp_tree.inorder(exp_tree.root)
print("\nRecorrido Preorden:")
exp_tree.preorder(exp_tree.root)
print("\nRecorrido Postorden:")
exp_tree.postorder(exp_tree.root)

print("\nResultado de la Evaluación:", exp_tree.evaluate(exp_tree.root))
