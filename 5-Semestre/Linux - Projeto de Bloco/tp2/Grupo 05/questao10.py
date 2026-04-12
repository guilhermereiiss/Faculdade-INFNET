import asyncio
import random

async def produtor(fila):
    while True:
        batimento = random.randint(40, 180)
        await fila.put(batimento)  
        print(f"Produzido: {batimento}")
        await asyncio.sleep(0.5)

async def consumidor(fila):
    while True:
        batimento = await fila.get()  

        if batimento > 120:
            print(f"ALERTA: Batimento em {batimento}!")
        else:
            print(f"Normal: {batimento}")

        fila.task_done()


async def main():
    fila = asyncio.Queue(maxsize=10)

    tarefa_produtor = asyncio.create_task(produtor(fila))
    tarefa_consumidor = asyncio.create_task(consumidor(fila))

    await asyncio.sleep(10)

    tarefa_produtor.cancel()
    tarefa_consumidor.cancel()

    print("Encerrando sistema...")

asyncio.run(main())