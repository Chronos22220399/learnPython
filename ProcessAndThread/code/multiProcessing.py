# from multiprocessing import Process
# import os
#
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     # 创建进程  run_proc：进程的执行函数
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     # 执行进程的函数
#     p.start()
#     # 同步进程, 这样能将子进程的结果输出出来
#     p.join()
#     print('Child process end.')


# # 进程池
# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print('Run task %s (%s)' %(name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.\n' % (name, end-start))
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     # 限制最多同时跑4个进程，这也是Pool的有意设计
#     p = Pool(4)
#     print(type(p))
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i, ))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')


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
    print(q.qsize())


# 读数据进程执行的代码
def read(q):
    print('Process to read: %s.' % os.getpid())
    while True:
        value = q.get()
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程传教Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))
    # 启动子进程pw，写入：
    pw.start()
    # 启动子进程pr，读取：
   # pr.start()

    # 等待子进程pw接收
    pw.join()
    # pr进程里是死循环，强行关闭
    #pr.terminate()
    print('Process end.')
