# dockerstats
Script for pulling stats from Docker using the Docker Python Client (click here for more info https://docker-py.readthedocs.io/en/stable/)

Notes:
1. Make sure the Docker Python Client is installed, using 'pip install docker'.
2. This script is designed to run on each docker node from a monitoring tool and therefore uses client = docker.from_env() for info and client = docker.APIClient(base_url='unix://var/run/docker.sock') for stats. This can easily be changed to the host and port if run externally if the Docker http client is enabled.

Usage: 
./dockerstats.py list=LISTTYPE type=DATATYPE attribute=ATTRIBUTE <br>
  (Required) list should be one of the following: images, services, nodes, containers, networks, volumes, client, swarm <br>
  (Required) type should be one of the following: info, stats <br>
  (Required) attribute is the attribute to return data for. If 'all', then returns all attributes. <br>
    
Examples: <br>
  ./dockerstats.py list=containers type=stats attribute=all <br><br>
  ./dockerstats.py list=containers type=info attribute=containers.Config.Image,containers.Config.Hostname,containers.Config.Labels.com.docker.swarm.node.id,containers.Config.Labels.com.docker.swarm.service.id,containers.Config.Labels.com.docker.swarm.task.name,containers.Config.Labels.com.docker.swarm.service.name,containers.Config.Labels.com.docker.swarm.task.id <br><br>
  ./dockerstats.py list=containers type=stats attribute=containers.stats.name,containers.stats.id,containers.stats.memory_stats.usage,containers.stats.memory_stats.limit,containers.stats.memory_stats.max_usage,containers.stats.cpu_stats.cpu_usage.total_usage,containers.stats.networks.eth2.tx_bytes,containers.stats.networks.eth2.rx_bytes,containers.stats.networks.eth1.tx_bytes,containers.stats.networks.eth1.rx_bytes,containers.stats.cpu_stats.system_cpu_usage <br><br>
