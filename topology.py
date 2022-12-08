#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
import sys
from star_topo_simulation_tests import *

def build_network():
  net = Mininet(topo=None,
                build=False,
                ipBase='10.0.0.0/8')

  info('*** Adding controller\n')
  c0=net.addController(name='c0',
                    controller=Controller,
                    protocol='tcp',
                    port=6633)

  info( '*** Add switches\n')
  s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

  info( '*** Add hosts\n')
  h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
  h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
  h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
  h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
  h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
  h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
  h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)

  info( '*** Add links\n')
  net.addLink(h4, s1)
  net.addLink(h3, s1)
  net.addLink(h2, s1)
  net.addLink(h1, s1)
  net.addLink(s1, h7)
  net.addLink(s1, h6)
  net.addLink(s1, h5)

  info( '*** Starting network\n')
  net.build()
  info( '*** Starting controllers\n')
  for controller in net.controllers:
      controller.start()

  info( '*** Starting switches\n')
  net.get('s1').start([c0])

  info( '*** Post configure switches and hosts\n')



  if len(sys.argv) == 1:
  	print("Runnng default mininet CLI stuff")
    CLI(net)
  elif sys.argv[1] == 'simple':
    print("Running a simple test with no load balancing using 1 client and 1 backend")
    test_simple(net)
  elif sys.argv[1] == 'random':
    print("Running a load balancing test with 3 clients connecting to 3 backend servers via a random load balancing algorithm")
    random_load_balancing(net)
  elif sys.argv[1] == 'round-robin':
    print("Running a load balancing test with 3 clients connecting to 3 backend servers via a round robin load balancing algorithm")
    rr_load_balancing(net)
  net.stop()

# this is the main function
if __name__ == '__main__':
  while (True):
    option = input('Select option: \n \
                    0: add new node \n \
                    1: add new switch \n \
                    2: run speed test between two nodes')
    if (option == 0):
      node_name = input('What will be the name of the node?')
      h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)

  setLogLevel( 'info' )
  build_network()