# asyncio

# youtube yury selivanov, pydata

# Historie
# 1. python 2.5: coroutines with yield
# 2. python 3.3: coroutines with yield from
# 3. python 3.5: async/await

# @types.coroutine
# __await__
# __aenter__
# __aexit__
# __aiter__
# __anext__

# Wichtige Funktionen
# asyncio.get_event_loop()
# loop.create_task()
# loop.run_until_complete() and loop_run_forever()
# asyncio.gather()
# loop.run_in_executor()
# loop.close()

# Debugging durch
# Environmentvariable: PYTHONASYNCIODEBUG=1
# or loop.set_debug()
# or logging




import asyncio
#import await


print ("Beispiel loop create task (nach 0.5 sek: hellp, nach 1 sek: world")
async def say(what, when):
    await asyncio.sleep(when)
    print(what)

# Variante 1 - run forever
# loop = asyncio.get_event_loop()
# loop.create_task(say('hello', 0.5))
# loop.create_task(say('world',1))
# loop.run_forever()

loop = asyncio.get_event_loop()
loop.set_debug('enabled')
t1 = loop.create_task(say('hello',0.5))
t2 = loop.create_task(say('world',1))
try:
    loop.run_until_complete( asyncio.gather(t1,t2))
finally:
    loop.close()

# ...........................................................................
print ("loop.run_in_executor")

def compute_pi(digits):
    # implementation
    return result

loop2 = asyncio.get_event_loop()

#pool = concurrent.futures.ProcessPoolExecutor()
#await loop2.run_in_executor(pool, compute_pi(10), 20000)

# .........................................................................



