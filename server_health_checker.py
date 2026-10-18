servers = [
    {
        "name": "web01",
        "is_reachable": True,
        "status": "running",
        "cpu": 45
    },
    {
        "name": "web02",
        "is_reachable": True,
        "status": "running",
        "cpu": 85
    },
    {
        "name": "db01",
        "is_reachable": False,
        "status": "unknown",
        "cpu": None
    },
    {
        "name": "app01",
        "is_reachable": True,
        "status": "running",
        "cpu": 95
    }
]

def check_server_status(is_reachable):
    if is_reachable is True:
        return 'reachable'
    elif is_reachable is False:
        return 'unreachable'
    else:
        return 'unknown'

def check_cpu(cpu):
    if cpu >= 90:
        return 'critical'
    elif cpu >= 70:
        return 'warning'
    else:
        return 'normal'
critical_server= 0
for server in servers:
    print('Server:',server['name'])
    reachability = check_server_status(server['is_reachable'])

    print('Reachability:',reachability)

    if reachability == 'reachable':
        print('CPU:',check_cpu(server['cpu']))
        server_cpu = check_cpu(server['cpu'])
    else:
        print('not checked') 
    
    if server_cpu == 'critical':
        critical_server+=1
    print ('Number of critical servers:',critical_server)
    print('---'*40)
