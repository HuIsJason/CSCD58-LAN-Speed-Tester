def simpleTest(net):
    mininet.get("h1").sendCmd("python3 /home/mininet/CSCD58-LAN-Speed-Tester/ReceiverHost.py &")

    mininet.get("h2").cmd("python3 /home/mininet/CSCD58-LAN-Speed-Tester/SenderHost.py")