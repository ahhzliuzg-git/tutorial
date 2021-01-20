#turn urls into iteration by calss 2020-12-12
# https://www.runoob.com/python3/python3-iterator-generator.html
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017496031185408

def yieldpage(n):
    counter=1
    a=1
    while True: 
        if counter>n:

            return  'http://search.ccgp.gov.cn/bxsearch?searchtype=2&page_index='+'{}'.format(a)+'&bidSort=0&buyerName=&projectId=&pinMu=0&bidType=0&dbselect=bidx&kw=&start_time=2019%3A02%3A13&end_time=2019%3A08%3A14&timeType=5&displayZone=&zoneId=&pppStatus=0&agentName='
        yield 'http://search.ccgp.gov.cn/bxsearch?searchtype=2&page_index='+'{}'.format(a)+'&bidSort=0&buyerName=&projectId=&pinMu=0&bidType=0&dbselect=bidx&kw=&start_time=2019%3A02%3A13&end_time=2019%3A08%3A14&timeType=5&displayZone=&zoneId=&pppStatus=0&agentName='
        counter=counter+1
        a=a+1
   
