class Node:
    def __init__(self, value):  # Constructor para crear un nodo del árbol
        self.value = value  # Valor del nodo (puede ser un número u operador)
        self.left = None  # Puntero al hijo izquierdo
        self.right = None  # Puntero al hijo derecho

class ExpressionTree:
    def __init__(self, postfix_expression):  # Constructor que recibe una expresión en notación postfija
        self.root = self.build_tree(postfix_expression)  # Construye el árbol a partir de la expresión

    def build_tree(self, postfix_expression):  # Método para construir el árbol desde la expresión postfija
        stack = []  # Pila para almacenar los nodos
        operators = set(['+', '-', '*', '/'])  # Conjunto de operadores válidos
        
        for char in postfix_expression:  # Recorremos cada carácter de la expresión postfija
            if char not in operators:  # Si es un operando (número)
                stack.append(Node(char))  # Se crea un nodo y se apila
            else:  # Si es un operador
                node = Node(char)  # Se crea un nodo con el operador
                node.right = stack.pop()  # Se extrae el último nodo (operando derecho)
                node.left = stack.pop()  # Se extrae el penúltimo nodo (operando izquierdo)
                stack.append(node)  # Se apila el nodo operador con sus hijos

        return stack.pop()  # Devuelve la raíz del árbol construido
    
    def inorder(self, node):  # Método para recorrido inorden (izquierda, raíz, derecha)
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')  # Imprime el valor del nodo
            self.inorder(node.right)
    
    def preorder(self, node):  # Método para recorrido preorden (raíz, izquierda, derecha)
        if node:
            print(node.value, end=' ')  # Imprime el valor del nodo
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self, node):  # Método para recorrido postorden (izquierda, derecha, raíz)
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=' ')  # Imprime el valor del nodo
    
    def evaluate(self, node):  # Método para evaluar la expresión contenida en el árbol
        if node is None:
            return 0  # Retorna 0 si el nodo es nulo
        
        if node.left is None and node.right is None:  # Si es un nodo hoja (número)
            return int(node.value)  # Retorna el valor numérico del nodo
        
        left_value = self.evaluate(node.left)  # Evalúa el subárbol izquierdo
        right_value = self.evaluate(node.right)  # Evalúa el subárbol derecho
        
        # Realiza la operación correspondiente según el operador del nodo
        if node.value == '+':
            return left_value + right_value
        elif node.value == '-':
            return left_value - right_value
        elif node.value == '*':
            return left_value * right_value
        elif node.value == '/':
            return left_value / right_value

# Ejemplo de uso
postfix_expression = "23*54*+9-"  # Representa la expresión: (2*3) + (5*4) - 9
exp_tree = ExpressionTree(postfix_expression)  # Crea un árbol con la expresión postfija

print("Recorrido Inorden:")
exp_tree.inorder(exp_tree.root)  # Muestra el recorrido inorden
print("\nRecorrido Preorden:")
exp_tree.preorder(exp_tree.root)  # Muestra el recorrido preorden
print("\nRecorrido Postorden:")
exp_tree.postorder(exp_tree.root)  # Muestra el recorrido postorden

print("\nResultado de la Evaluación:", exp_tree.evaluate(exp_tree.root))  # Evalúa la expresión
