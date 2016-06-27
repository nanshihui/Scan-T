# import gevent,multiprocessing
# import multiprocessing.Pool
# class Poc_Base(object):
#     gevent_num = 100            # 协程数
#     process_num = 4             # 进程数
#     count = [0] * process_num   # 每个进程，单独计数
#     progress = 100              # 进度提醒的单位
#
#     def verify(self):
#         pass
#     def verify_count(self):
#         self.count[progress_number] += 1
#         if self.count[progress_number] % progress == 0:
#             save()                                                # 数据存储
#             print "progress %d " % (self.count[progress_number])       # 进度提醒
#         if self.verify():            print "success"
#     # 协程调度函数，分配任务到协程
#     def run_in_gevent(url_list):                    # url_list 每个进程分配到一定量的url
#         pool = Pool(self.gevent_num)
#         for target in url_list:
#             pool.add(gevent.spawn(self.verify_count, url))
#         pool.join()    # 进程调度函数，分配任务到各个进程
#     def run():
#         url_each_process = len(url_list)/process_num
#         for process_number in range(process_num):
#             multiprocessing.Process(target=run_in_gevent, args=(url_list[*:*],)).start()
#         multiprocessing.join()
#
# if __name__ == "__main__":
#     # temp=Portscantool()
#     # temp.do_scan(ip='172.20.13.11', port='80')