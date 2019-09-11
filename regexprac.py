import re

output = '''Sep 5 10:52:00 :124004:  <6127> <DBUG> |authmgr|  cmdtype=10, len=98, cmd='USER:Varsha@195.168.1.251 NODE:"/mm/mynode" COMMAND:<show vlan> -- command executed successfully '

Sep 5 10:52:00 :124004:  <6127> <DBUG> |authmgr|  user=Varsha, line=195.168.1.251, node=/mm/mynode, cmd='show vlan'

Sep 5 10:52:00 :124004:  <6127> <DBUG> |authmgr|  aal_authenticate aal 0x42f92b0 username Varsha

Sep 5 10:52:00 :124546:  <6127> <DBUG> |authmgr|  aal_authenticate user:Varsha vpnflags:0.

Sep 5 10:52:00 :124547:  <6127> <DBUG> |authmgr|  aal_authenticate server_group:TACACS.

Sep 5 10:52:00 :124004:  <6127> <DBUG> |authmgr|  Select server for method=tacacs-accounting, user=Varsha, essid=<>, server-group=TACACS, last_srv <>

Sep 5 10:52:00 :124004:  <6127> <DBUG> |authmgr|   server=MgmtTac, ena=1, ins=1 (1)

Sep 5 10:52:00 :124038:  <6127> <INFO> |authmgr|  Selected server MgmtTac for method=tacacs-accounting; user=Varsha,  essid=<>, domain=<>, server-group=TACACS

Sep 5 10:52:00 :124004:  <6127> <DBUG> |authmgr|  aal_authenticate (1142)(INC) : os_auths 21, s MgmtTac type 5 inservice 1 markedD 0 sg_name TACACS

Sep 5 10:52:00 :124004:  <6127> <DBUG> |authmgr|  aal_authenticate (1145)(INC) : os_reqs 1, s MgmtTac type 5 inservice 1 markedD 0

Sep 5 10:52:00 :122020:  <6127> <DBUG> |authmgr| |aaa| [acct.c:92] tac_account_send: user 'Varsha', tty '195.168.1.251', encrypt: yes, type: START

Sep 5 10:52:00 :122020:  <6127> <DBUG> |authmgr| |aaa| [acct.c:166] tac_account_send: send attribute 'start_time=1567680720' of len 21

Sep 5 10:52:00 :122020:  <6127> <DBUG> |authmgr| |aaa| [acct.c:166] tac_account_send: send attribute 'task_id=44340' of len 13

Sep 5 10:52:00 :122020:  <6127> <DBUG> |authmgr| |aaa| [acct.c:166] tac_account_send: send attribute 'service=system' of len 14

Sep 5 10:52:00 :122020:  <6127> <DBUG> |authmgr| |aaa| [acct.c:166] tac_account_send: send attribute 'protocol=ip' of len 11

Sep 5 10:52:00 :122020:  <6127> <DBUG> |authmgr| |aaa| [acct.c:166] tac_account_send: send attribute 'cmd=show vlan' of len 13

Sep 5 10:52:00 :122020:  <6127> <DBUG> |authmgr| |aaa| [acct.c:166] tac_account_send: send attribute 'cmd=show vlan1' of len 13

Sep 5 10:52:00 :122020:  <6127> <DBUG> |authmgr| |aaa| [acct.c:166] tac_account_send: send attribute 'cmd=delete vlan' of len 13

Sep 5 10:52:00 :122026:  <6127> <INFO> |authmgr| |aaa|  tac_connect_try_once  276 source-interface  ANY selected for outgoing requests to TACACS-server  195.168.1.250

Sep 5 10:52:00 :122020:  <6127> <DBUG> |authmgr| |aaa| [authen.c:824] TACACS server MgmtTac-195.168.1.250-12544 response on port 65

Sep 5 10:52:00 :122020:  <6127> <DBUG> |authmgr| |aaa| [acct.c:316] tac_account_read: accounted ok

Sep 5 10:52:00 :124067:  <6127> <DBUG> |authmgr|  TACACS+ Accounting Successful: result=Authentication Successful(0), method=tacacs-accounting, username=Varsha source=195.168.1.251 auth server=MgmtTac

Sep 5 10:52:00 :124003:  <6127> <INFO> |authmgr|  Authentication result=Authentication Successful(0), method=tacacs-accounting, server=MgmtTac, user=Varsha

Sep 5 10:52:00 :124004:  <6127> <DBUG> |authmgr|  server_cbh (163)(DEC) : os_reqs 0, s MgmtTac type 5 inservice 1 markedD 0

Sep 5 10:52:00 :124607:  <6127> <DBUG> |authmgr|  server_cbh(): response=0 from Auth server 'MgmtTac for client:16 proto:6 eap-type:0'.

'''

# print(output)


cmd = re.findall("send attribute 'cmd=(.*)'", output)
print("All the commands used: " , cmd)

# server = re.findall("aal_authenticate server_group:(.*).\n", output)
# print("server group :" , server)
servergroup = re.search("aal_authenticate server_group:(.*).\n", output)
print("server group :", servergroup.group(1))


methoduser = re.search('Select server for method=(.*), user=(.*), essid', output)
print("method : ", methoduser.group(1))
print("user : ", methoduser.group(2))
