nec_bm = 0
def nec_cb(nec, a, c, r):
	global nec_bm
	nec_bm=c
	print(a, c, r,nec_bm)   # Address, Command, Repeat


def necbm():
        global nec_bm
        global tempNec
        tempNec = nec_bm
        nec_bm = 0
        return tempNec
