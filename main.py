
from qawafi_server.qawafi_server.bait_analysis import BaitAnalysis



if __name__ =='__main__':

    shatrs = """
    القلب أعلم يا عذول بدائه
    وأحق منك بجفنه وبمائه
    مهلا فإن العذل من أسقامه
    وترفقا فالسمع من أعضائه
    لا تعذل المشتاق في أشواقه
    حتى يكون حشاك في أحشائه
    """
    shatrs = shatrs.split("\n")[1:-1]

    baits = [' # '.join(shatrs[2*i:2*i+2]) for i in range(len(shatrs)//2)]

    analysis = BaitAnalysis()

    output = analysis.analyze(baits, override_tashkeel=True)