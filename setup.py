#!/usr/bin/env python

# Prerequisites (OSX)
# pip install pyyaml

import yaml
from string import Template
import os, sys
import urllib
import shutil

MACHINES_DIR = "machines.d"

def clean( ):
	# Clean first
	if os.path.exists(MACHINES_DIR):
		shutil.rmtree(MACHINES_DIR)
	os.mkdir(MACHINES_DIR)

def createDiscoveryToken( numberOfMachines ):
	url = "https://discovery.etcd.io/new?size=" + str(numberOfMachines);
	discoveryToken = urllib.urlopen(url).read()
	print "Discovery token: " + discoveryToken
	return discoveryToken

def createCloudConfig( configuration, template, discoveryToken, numberOfMachines ):
	ip = configuration["ip"];
	hostname = configuration["hostname"]
	cloudConfig = Template(template).safe_substitute(
		private_ipv4=ip, 
		public_ipv4=ip,
		hostname=hostname,
		discoveryToken=discoveryToken,
		numberOfMachines=numberOfMachines
	);
	with open(MACHINES_DIR + '/' + hostname + '.yaml','w') as f:
		f.write(cloudConfig)

clean()
with open("configuration.yaml", 'r') as machinesStream, open("cloud-config-template.yaml") as templateStream:
	configurations = yaml.load(machinesStream)	
	template = templateStream.read()

	# Generate a discovery token
	numberOfMachines = len(configurations['cluster'])
	discoveryToken = createDiscoveryToken(numberOfMachines)

	for configuration in configurations['cluster']:
		createCloudConfig( configuration, template, discoveryToken, numberOfMachines )
