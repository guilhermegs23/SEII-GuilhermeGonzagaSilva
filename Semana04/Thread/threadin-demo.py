# Guilherme Gonzaga Silva 
# 11621EMT021 

import time
# import threading
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f'SLeeping {seconds} second(s)...')
    time.sleep(seconds)
    # print('Done Sleeping...')
#    return 'Done Sleeping...'
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_something, 1)
#     f2 = executor.submit(do_something, 1)
#     print(f1.result())
#     print(f2.result())
#     results = [executor.submit(do_something, 1) for _ in range(10)]
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

#     for result in results:
#         print(result)
    
#     results = [executor.submit(do_something, sec) for sec in secs]

#     for f in concurrent.futures.as_completed(results):
#         print(f.result())


# do_something()
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')