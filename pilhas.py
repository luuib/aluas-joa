class Stack:
    def __init__(self):
        self.items = []

    def isEmpyt(self):
        return self.items == []
    
    def push(self, items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
pilha = Stack()

pilha.push('A')
pilha.push('B')
pilha.push('C')
pilha.push('D')
pilha.push('E')
pilha.push('F')
print(pilha.items)
print(pilha.peek())
print(pilha.items)
pilha.pop()
print(pilha.items)
