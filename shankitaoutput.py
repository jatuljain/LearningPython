output = '''Sep 5 16:13:21 :124004:  <6414> <DBUG> |authmgr|  RX (sock) message of type 1, len 1040

Sep 5 16:13:21 :124004:  <6414> <DBUG> |authmgr|  aal_authenticate aal 0x38b3070 username Varsha

Sep 5 16:13:21 :124546:  <6414> <DBUG> |authmgr|  aal_authenticate user:Varsha vpnflags:0.

Sep 5 16:13:21 :124547:  <6414> <DBUG> |authmgr|  aal_authenticate server_group:TACACS.

Sep 5 16:13:21 :124004:  <6414> <DBUG> |authmgr|  Select server for method=Management, user=Varsha, essid=<>, server-group=TACACS, last_srv <>

Sep 5 16:13:21 :124004:  <6414> <DBUG> |authmgr|   server=MgmtTac, ena=1, ins=1 (1)

Sep 5 16:13:21 :124038:  <6414> <INFO> |authmgr|  Selected server MgmtTac for method=Management; user=Varsha,  essid=<>, domain=<>, server-group=TACACS

Sep 5 16:13:21 :124004:  <6414> <DBUG> |authmgr|  aal_authenticate (1142)(INC) : os_auths 1, s MgmtTac type 5 inservice 1 markedD 0 sg_name TACACS

Sep 5 16:13:21 :124004:  <6414> <DBUG> |authmgr|  aal_authenticate (1145)(INC) : os_reqs 1, s MgmtTac type 5 inservice 1 markedD 0

Sep 5 16:13:21 :122020:  <6414> <DBUG> |authmgr| |aaa| [authen.c:85] tac_authen_pap_send: user 'Varsha'(mgmt user), tty 'tty0', rem_addr '195.168.1.251', encrypt: yes

Sep 5 16:13:21 :122026:  <6414> <INFO> |authmgr| |aaa|  tac_connect_try_once  276 source-interface  ANY selected for outgoing requests to TACACS-server  195.168.1.250

Sep 5 16:13:21 :122020:  <6414> <DBUG> |authmgr| |aaa| [authen.c:196] tac_authen_pap_send: written message of size 52

Sep 5 16:13:22 :122020:  <6414> <DBUG> |authmgr| |aaa| [authen.c:824] TACACS server MgmtTac-195.168.1.250-12544 response on port 65

Sep 5 16:13:22 :122020:  <6414> <DBUG> |authmgr| |aaa| [authen.c:521] tac_authen_pap_read: authentication ok

Sep 5 16:13:22 :122020:  <6414> <DBUG> |authmgr| |aaa| [authen.c:298] tac_author_pap_send: user 'Varsha'(mgmt user), tty 'tty0', rem_addr '195.168.1.251', encrypt: yes

Sep 5 16:13:22 :122026:  <6414> <INFO> |authmgr| |aaa|  tac_connect_try_once  276 source-interface  ANY selected for outgoing requests to TACACS-server  195.168.1.250

Sep 5 16:13:22 :122020:  <6414> <DBUG> |authmgr| |aaa| [authen.c:410] tac_author_pap_send: written message of size 73

Sep 5 16:13:22 :122020:  <6414> <DBUG> |authmgr| |aaa| [authen.c:824] TACACS server MgmtTac-195.168.1.250-12544 response on port 65

Sep 5 16:13:22 :122020:  <6414> <DBUG> |authmgr| |aaa| [authen.c:643] Total 1 args in author response

Sep 5 16:13:22 :122020:  <6414> <DBUG> |authmgr| |aaa| [authen.c:666] tac_author_pap_read: authorization ok

Sep 5 16:13:22 :122020:  <6414> <DBUG> |authmgr| |aaa| [authen.c:673] tac_author_pap_read: Aruba-Admin-Role: root

Sep 5 16:13:22 :122020:  <6414> <DBUG> |authmgr| |aaa| [authen.c:686] tac_author_pap_read: Aruba-Admin-Role AVP created

Sep 5 16:13:22 :124066:  <6414> <INFO> |authmgr|  Administrative User result=Authentication Successful(0), method=Management, username=Varsha IP=195.168.1.251 auth server=MgmtTac

Sep 5 16:13:22 :124003:  <6414> <INFO> |authmgr|  Authentication result=Authentication Successful(0), method=Management, server=MgmtTac, user=195.168.1.251

Sep 5 16:13:22 :124004:  <6414> <DBUG> |authmgr|  server_cbh (163)(DEC) : os_reqs 0, s MgmtTac type 5 inservice 1 markedD 0

Sep 5 16:13:22 :124607:  <6414> <DBUG> |authmgr|  server_cbh(): response=0 from Auth server 'MgmtTac for client:9 proto:1 eap-type:0'.

Sep 5 16:13:22 :124004:  <6414> <DBUG> |authmgr|  server_cbh (546)(DEC) : os_auths 0, s MgmtTac type 5 inservice 1 markedD 0 sg_name TACACS

Sep 5 16:13:22 :124025:  <6414> <NOTI> |authmgr|  Administrative user 'Varsha' authenticated successfully  (role=root, privileged=0)

Sep 5 16:13:22 :199801:  <29545> <INFO> |sshd|  Accepted password for Varsha from 195.168.1.251 port 50279 ssh2

 '''

# print(output)

released = {
		"iphone" : 2007,
		"iphone 3G" : 2008,
		"iphone 3GS" : 2009,
		"iphone 4" : 2010,
		"iphone 4S" : 2011,
		"iphone 5" : 2012
	}

newrelease = {
		"iphone 3G" : 2008,
		"iphone 3GS" : 2009,
		"iphone 4" : 2010,
		"iphone 4S" : 2011,
		"iphone 5" : 2012
	}


print (released)
print(len(released))
print(newrelease)
print(len(newrelease))
