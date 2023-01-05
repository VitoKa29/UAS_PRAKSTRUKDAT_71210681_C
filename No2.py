class Node:
    def __init__(self,data,priority) -> None:
        self._data = data
        self._priority = priority
        self._next = None
        self._prev = None

class PQSTugas:
    def __init__(self) -> None:
        self._data = []
        self._size = 0

    def isEmpty(self) -> bool:
    #isi kode anda
        return len(self._data) == 0

    def printAll(self):
    #isi kode anda
        print("=== Prioritas : Tugas ===")
        a=0
        b=1
        for i in self._data:
            print(f"[{i[b]}] : {i[a]}")
            a+=1
            b+=1

    def _addHead(self, newNode) -> None:
    #isi kode anda
        pass

    def _addTail(self, newNode) -> None:
    #isi kode anda
        pass

    def _addMiddle(self, newNode) -> None:
    #isi kode anda
        pass

    def add(self, data, priority) -> None:
        #isi kode anda
        if self.isEmpty():
            self._data.append((data, priority))
        
        
    def remove(self) -> None:
    #isi kode anda
        self._data.pop(0)

    def removePriority(self, priority) -> None:
    #isi kode anda
        bantu = 0
        while self._data[bantu][1] != priority:
            bantu+=1
        self._data.pop[bantu]

if __name__ == "__main__":
    tugasKu = PQSTugas()
    tugasKu.add("StrukDat",1)
    # tugasKu.add("Menyapu", 5)
    # tugasKu.add("Cuci Baju", 4)
    # tugasKu.add("Beli Alat Tulis", 3)
    # tugasKu.add("Cuci Sepatu", 4)
    tugasKu.printAll()
    # tugasKu.remove()
    # tugasKu.printAll()
    # tugasKu.removePriority(2)
    # tugasKu.removePriority(4)
    # tugasKu.printAll()