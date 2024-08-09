from typing import Deque, Any, Interador
from collections import deque

class Queue:
    """ Uma classe representado uma fila """

    def __int__(self, maxlen=None) ->None:
        self.__items: Deque[Any] = deque(maxlen=maxlen)

    def enqueue(self, *items:Any) ->None:
        """Enqueue (enfileirar) é o mesmo que apped"""
        for item in items:
            self.__items.apped(item)

    def dequeue(self) -> Any:
        """dequeue (desenfileirar) é o mesmo que popleft"""
        if not self:
            raise IndexError('pop from empyt queue')
        return self.__items.popleft()
    
    def __repr__(self) -> str:
        return str(self.__items)
    
    def __bool__(self) -> bool:
        return bool(self.__items)
    
    def __len__(self) -> int:
        return len(self.__items)
    
    def __iter__(self) -> Interador:
        return self.__items.__iter__()
    
    def __getitem__(self, index: int) -> Any:
        return self.__items[index]
    
if __name__ == "__main__":
    fila = Queue()

fila.enqueue('A','B','C','D')

print(fila.__repr__())
print(fila.__getitem__(2))
print(fila.__bool__())
print(fila.__iter__())

fila.enqueue('d','e','f','g')

print(fila)
print('Item com indice 1:',fila[1], end='\n\n')

for item in fila:
    print('Iteração:', item)
    