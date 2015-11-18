from spidertool import sniffertask
nmaptask=sniffertask.snifferTask(0)
def taskinit():
    nmaptask.set_deal_num(5)
def taskadd(array):
    nmaptask.add_work(array)
