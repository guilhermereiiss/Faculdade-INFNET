import random
import time
import os
import argparse
import multiprocessing as mp
import asyncio
from datetime import datetime
import threading

def monte_carlo_chunk(n):
    hits = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x*x + y*y <= 1:
            hits += 1
    return hits

def run_serial(total_samples):
    start = time.time()
    hits = monte_carlo_chunk(total_samples)
    pi = 4 * hits / total_samples
    return pi, time.time() - start

def log_writer(msg):
    with open("log.txt", "a") as f:
        f.write(msg + "\n")

def worker_task(n):
    pid = os.getpid()
    hits = monte_carlo_chunk(n)
    log_writer(f"{datetime.now()} | PID {pid} finalizou chunk")
    return hits

async def monitor_task(i):
    while True:
        await asyncio.sleep(1)
        print(f"[monitor {i}] ativo...")

async def run_monitors():
    tasks = [asyncio.create_task(monitor_task(i)) for i in range(20)]
    await asyncio.gather(*tasks)

def run_parallel(total_samples, workers, n_tasks):
    start = time.time()
    chunk_size = total_samples // n_tasks
    pool = mp.Pool(processes=workers)
    tasks = [chunk_size for _ in range(n_tasks)]
    results = pool.map(worker_task, tasks)
    pool.close()
    pool.join()
    total_hits = sum(results)
    pi = 4 * total_hits / total_samples
    return pi, time.time() - start

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=1000000)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--tasks", type=int, default=8)
    args = parser.parse_args()

    print("SERIAL: ")
    pi_s, t_s = run_serial(args.samples)
    print(pi_s, t_s)

    print("PARALELO: ")
    threading.Thread(target=lambda: asyncio.run(run_monitors()), daemon=True).start()
    pi_p, t_p = run_parallel(args.samples, args.workers, args.tasks)
    print(pi_p, t_p)

    print("Speedup:", t_s / t_p)