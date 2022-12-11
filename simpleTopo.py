def simpleTest(net):
    net.get("h1").cmdPrint("python3 /home/mininet/CSCD58-LAN-Speed-Tester/ReceiverHost.py &")

    net.get("h2").cmdPrint("python3 /home/mininet/CSCD58-LAN-Speed-Tester/SenderHost.py")