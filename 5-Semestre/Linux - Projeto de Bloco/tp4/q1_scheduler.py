
import time
import random
from typing import Optional

class MinHeap:
    def __init__(self):
        self._data: list = []

    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    def _swap(self, i: int, j: int) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _sift_up(self, i: int) -> None:
        while i > 0:
            p = self._parent(i)
            if self._data[i] < self._data[p]:
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i: int) -> None:
        n = len(self._data)
        while True:
            smallest = i
            l, r = self._left(i), self._right(i)
            if l < n and self._data[l] < self._data[smallest]:
                smallest = l
            if r < n and self._data[r] < self._data[smallest]:
                smallest = r
            if smallest == i:
                break
            self._swap(i, smallest)
            i = smallest

    def push(self, item) -> None:
        self._data.append(item)
        self._sift_up(len(self._data) - 1)

    def pop(self) -> object:
        if self.is_empty():
            raise IndexError("Heap vazia")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        if self._data:
            self._sift_down(0)
        return item

    def peek(self) -> object:
        if self.is_empty():
            raise IndexError("Heap vazia")
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"MinHeap({self._data})"

_PID_COUNTER = 0

class Process:

    def __init__(self, name: str, priority: int, burst_ms: int,
                 wait_cycles: int = 0):
        global _PID_COUNTER
        _PID_COUNTER += 1
        self.pid = _PID_COUNTER
        self.name = name
        self.priority = priority
        self.burst_total = burst_ms
        self.burst_rem = burst_ms
        self.state = "Nova"
        self.wait_cycles = wait_cycles  
        self.wait_cycles_init = wait_cycles
        self.cpu_count = 0              
        self.total_wait = 0              
        self.history: list[str] = []     

    def __lt__(self, other: "Process") -> bool:
        return self.priority < other.priority

    def __eq__(self, other: "Process") -> bool:
        return self.pid == other.pid

    def set_state(self, new_state: str) -> None:
        self.state = new_state
        self.history.append(new_state)

    def __repr__(self) -> str:
        return (f"Process(pid={self.pid}, name={self.name!r}, "
                f"priority={self.priority}, burst_rem={self.burst_rem}ms, "
                f"state={self.state!r})")

class Scheduler:
    def __init__(self, quantum: int = 30, speed: float = 0.03):
        self.quantum = quantum
        self.speed = speed           
        self.ready_queue: MinHeap = MinHeap()
        self.waiting_queue: MinHeap = MinHeap()
        self.new_queue: list[Process] = []
        self.finished: list[Process] = []
        self.current: Optional[Process] = None
        self.clock = 0               
        self.log_rows: list[dict] = []

    def add_process(self, p: Process) -> None:
        self.new_queue.append(p)

    def run(self) -> None:
        print("\n" + "="*72)
        print("  SIMULAÇÃO DO ESCALONADOR ROUND-ROBIN")
        print(f"  Quantum = {self.quantum} ms")
        print("="*72)

        for p in self.new_queue:
            p.set_state("Pronta")
            self.ready_queue.push(p)
            self._log(p, "Nova -> Pronta")

        while not self.ready_queue.is_empty() or \
              not self.waiting_queue.is_empty() or \
              self.current is not None:

            self._resume_waiting()

            if self.ready_queue.is_empty():
                self.clock += self.quantum
                time.sleep(self.speed * self.quantum)
                continue

            proc = self.ready_queue.pop()
            self._execute(proc)

        print("\n" + "="*72)
        print("  TODOS OS PROCESSOS TERMINADOS")
        print("="*72)
        self._print_table()
        self._print_summary()

    def _execute(self, proc: Process) -> None:
        """Executa o processo por até um quantum."""
        proc.set_state("Executando")
        proc.cpu_count += 1
        time_slice = min(self.quantum, proc.burst_rem)

        print(f"\n[Clock {self.clock:>5}ms] >> Executando  PID {proc.pid:>2} "
              f"'{proc.name}' | prioridade={proc.priority} | "
              f"burst_rem={proc.burst_rem}ms -> usando {time_slice}ms")

        self._log(proc, f"Pronta -> Executando (fatia={time_slice}ms)")
        time.sleep(self.speed * time_slice)

        self.clock += time_slice
        proc.burst_rem -= time_slice

        if proc.burst_rem <= 0:
            proc.set_state("Terminada")
            self.finished.append(proc)
            print(f"           OK PID {proc.pid:>2} '{proc.name}' TERMINADO "
                  f"(usou CPU {proc.cpu_count}x)")
            self._log(proc, "Executando -> Terminada")
        else:
            if proc.wait_cycles > 0 and proc.cpu_count % 2 == 0:
                proc.wait_cycles = proc.wait_cycles_init
                proc.set_state("Suspensa")
                self.waiting_queue.push(proc)
                print(f"           || PID {proc.pid:>2} '{proc.name}' -> "
                      f"SUSPENSA (aguarda {proc.wait_cycles} ciclos)")
                self._log(proc, f"Executando -> Suspensa (wait={proc.wait_cycles})")
            else:
                proc.set_state("Pronta")
                self.ready_queue.push(proc)
                print(f"           -> PID {proc.pid:>2} '{proc.name}' -> "
                      f"PRONTA (burst_rem={proc.burst_rem}ms)")
                self._log(proc, "Executando -> Pronta (preempção)")

    def _resume_waiting(self) -> None:
        """Decrementa contadores de espera e move processos para Pronta."""
        to_resume = []
        temp: list[Process] = []

        while not self.waiting_queue.is_empty():
            p = self.waiting_queue.pop()
            p.wait_cycles -= 1
            if p.wait_cycles <= 0:
                to_resume.append(p)
            else:
                temp.append(p)

        for p in temp:
            self.waiting_queue.push(p)

        for p in to_resume:
            p.set_state("Pronta")
            self.ready_queue.push(p)
            print(f"[Clock {self.clock:>5}ms]  ^ PID {p.pid:>2} '{p.name}' "
                  f"saiu de SUSPENSA -> PRONTA")
            self._log(p, "Suspensa -> Pronta")

    def _log(self, proc: Process, transition: str) -> None:
        self.log_rows.append({
            "Clock": self.clock,
            "PID": proc.pid,
            "Nome": proc.name,
            "Prioridade": proc.priority,
            "Transição": transition,
            "Burst Rem.": proc.burst_rem,
            "CPU#": proc.cpu_count,
        })

    def _print_table(self) -> None:
        print("\n" + "-"*90)
        print(f"{'Clock':>7} | {'PID':>3} | {'Nome':<14} | {'Prior':>5} | "
              f"{'Transição':<38} | {'BRem':>5} | {'CPU#':>4}")
        print("-"*90)
        for r in self.log_rows:
            print(f"{r['Clock']:>7} | {r['PID']:>3} | {r['Nome']:<14} | "
                  f"{r['Prioridade']:>5} | {r['Transição']:<38} | "
                  f"{r['Burst Rem.']:>5} | {r['CPU#']:>4}")
        print("-"*90)

    def _print_summary(self) -> None:
        print("\n-- RESUMO FINAL ------------------------------------------")
        print(f"{'PID':>4} | {'Nome':<14} | {'Prioridade':>10} | "
              f"{'Burst Total':>11} | {'Uso CPU':>7}")
        print("-"*60)
        for p in sorted(self.finished, key=lambda x: x.pid):
            print(f"{p.pid:>4} | {p.name:<14} | {p.priority:>10} | "
                  f"{p.burst_total:>11} | {p.cpu_count:>7}x")
        print("-"*60)
        print(f"Clock total: {self.clock} ms | Processos terminados: {len(self.finished)}")

def main():
    random.seed(42)

    process_specs = [
        ("Sistema",   1, 150, 0),
        ("Kernel",    2, 120, 0),
        ("Rede",      3, 180, 2),
        ("Disco",     4,  90, 1),
        ("Audio",     5, 100, 0),
        ("Video",     6, 160, 2),
        ("Browser",   7, 130, 1),
        ("Editor",    8,  70, 0),
        ("Banco DB",  9, 140, 2),
        ("Email",    10, 110, 1),
    ]

    scheduler = Scheduler(quantum=30, speed=0.02)

    for name, pri, burst, wait in process_specs:
        p = Process(name=name, priority=pri, burst_ms=burst, wait_cycles=wait)
        scheduler.add_process(p)

    scheduler.run()

if __name__ == "__main__":
    main()
