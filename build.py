#!/usr/bin/env python

# Prerequisites (OSX)
# pip install pyyaml

import yaml
from string import Template
import os, sys
import urllib
import shutil

TARGET_DIR = "target"

def clean( ):
	# Clean first
	if os.path.exists(TARGET_DIR):
		shutil.rmtree(TARGET_DIR)
	os.mkdir(TARGET_DIR)

def createDiscoveryToken( numberOfMachines ):
	url = "https://discovery.etcd.io/new?size=" + str(numberOfMachines);
	discoveryToken = urllib.urlopen(url).read()
	print "Discovery token: " + discoveryToken
	return discoveryToken

def createCloudConfig( configuration, template, discoveryToken, numberOfMachines ):
	ip = configuration["ip"];
	hostname = configuration["hostname"]
	cloudConfig = Template(template).safe_substitute(
		PRIVATE_IPV4=ip, 
		PUBLIC_IPV4=ip,
		HOSTNAME=hostname,
		DISCOVERY_TOKEN=discoveryToken,
		NUMBER_OF_MACHINES=numberOfMachines
	);
	hostDirectory = TARGET_DIR + '/' + hostname
	os.mkdir(hostDirectory)
	with open(hostDirectory + '/cloud-config.yaml','w') as f:
		f.write(cloudConfig)
	shutil.copy('templates/install.sh', hostDirectory + '/install.sh')


def build():
	with open("configuration.yaml", 'r') as machinesStream, open("templates/cloud-config.yaml") as templateStream:
		configurations = yaml.load(machinesStream)	
		template = templateStream.read()

		# Generate a discovery token
		numberOfMachines = len(configurations['cluster'])
		discoveryToken = createDiscoveryToken(numberOfMachines)

		for configuration in configurations['cluster']:
			createCloudConfig( configuration, template, discoveryToken, numberOfMachines )

clean()
build()
