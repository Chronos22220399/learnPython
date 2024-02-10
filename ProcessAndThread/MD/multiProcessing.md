## 多进程（multiProcessing）
### 创建子进程
```commandline
from multiprocessing import Process
import os

# 子进程要执行的代码
def def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    # getpid() 用于获取当前进程的id
    
print('Parent process %s.' % os.getpid())
# 创建子进程
p = Process(target=run_proc, args=('test', ))
print('Child process will start.')
# 开始进程
p.start()
# 将进程合并
p.join()
print('Child process end.')
```
1. #### run_proc中的是要让子进程执行的代码
2. #### Process用于创建子进程，target是需要执行的函数名称，args是函数内所需的参数，函数返回一个进程对象
3. #### start函数用于执行进程
4. #### join函数用于同步进程，将子进程的内容同步到当前进程中去


### 创建进程池
```commandline
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)' %(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.\n' % (name, end-start))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # 限制最多同时跑4个进程，这也是Pool的有意设计
    p = Pool(4)
    print(type(p))
    for i in range(5):
        p.apply_async(long_time_task, args=(i, ))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

```
1. #### long_time_task(name): 需要进程执行的函数
2. #### time.time(): 用于获取当前时间
3. #### sleep(): 暂停程序
4. #### Pool(num): 创建进程池的函数，num表示同一时间最大执行进程数量，返回值是一个进程池对象
5. #### apply_async(): 申请进程的函数，内部参数为待执行函数，以及函数参数组成的元组
6. #### p.close(): 关闭进程池
7. #### p.join(): 同步进程


### 进程间通信
```commandline
# 进程间通信
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码
def write(q):
    print('Process to write: %s.' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random()*10)

# 读数据进程执行的代码
def read(q):
    print('Process to read: %s.' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程传教Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))
    # 启动子进程pw，写入：
    pw.start()
    # 启动子进程pr，读取：
    pr.start()

    # 等待子进程pw接收
    pw.join()
    # pr进程里是死循环，强行关闭
    pr.terminate()
    print('Process end.')
```
1. #### Queue(): 创建并返回一个通信队列
2. #### put(): 将数据压入队列中
3. #### get(): 获取队列中的数据（按照fifo的原则）
4. #### terminate(): 强行终止进程
