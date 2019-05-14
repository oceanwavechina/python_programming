weeklycard

cd /Users/liuyanan/kuwo_work/sshfs_space/remote

sshfs t78:/home/liuyanan/new_ming/Ice/weeklycard_compile .

/bin/cp -rf /Users/liuyanan/kuwo_work/mining/Ice/weeklycard/branches/weeklycard20171205/* .




scp WeeklyCardServer fengqinyuan@60.28.210.114:/home/fengqinyuan/project/ice/WeeklyCard/bin




icegridadmin114 -e 'server stop WeeklyCardServer-1'
icegridadmin114 -e 'server start WeeklyCardServer-1'
icegridadmin114 -e 'server state WeeklyCardServer-1'





source /home/fengqinyuan/project/ice/virtualenv/ice-env/bin/activate
cd /home/fengqinyuan/project/ice/pyclient


source /home/fengqinyuan/project/ice/virtualenv/py27env/bin/activate
cd /home/fengqinyuan/project/ice/pyclient




import httplib2   
h = httplib2.Http(".cache")   
resp, content = h.request("http://zhiboserver.kuwo.cn/proxy.p?src=WEB&cmd=getroomguardianlist&rid=676118&r=0.5673788534857693&_=1528105320917", "GET")  

