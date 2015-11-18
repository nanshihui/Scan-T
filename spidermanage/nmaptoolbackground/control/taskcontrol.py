from spidertool import sniffertask
nmaptask=sniffertask.snifferTask(1)
def taskinit():
    nmaptask.set_deal_num(5)
def taskadd(array):
    nmaptask.add_work(array)
