srv_name = 'member_2'
state = 'stop'


# Get the status server variable srv_name
def status_srv(name):
    print('type=Server,process=' + name + ',*')
#    print(AdminControl.queryNames('type=Server,process=' + name + ',*'))


#status_srv(srv_name)


# "AdminControl.invoke(AdminControl.queryNames('type=Server,process=member_1,*'), 'stop')"

def stop_srv(srv_name,state):
    print('AdminControl.invoke(' + (status_srv(srv_name)+ '', " ' " + state + " ')"))

stop_srv(srv_name, state)