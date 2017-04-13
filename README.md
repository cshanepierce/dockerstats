# dockerstats
Scripts for pulling stats from Docker using the Docker Python Client 

Usage: ./dockerpy.py list=LISTTYPE type=DATATYPE attribute=ATTRIBUTE <br>
  (Required) list should be one of the following: images, services, nodes, containers, networks, volumes, client, swarm <br>
  (Required) type should be one of the following: info, stats <br>
  (Required) attribute is the attribute to return data for. If 'all', then returns all attributes. <br>
    
Example:
  ./dockerpy.py list=containers type=stats attribute=all <br>
  ./dockerpy.py list=containers type=info attribute=containers.Config.Image,containers.Config.Hostname,containers.Config.Labels.com.docker.swarm.node.id,containers.Config.Labels.com.docker.swarm.service.id,containers.Config.Labels.com.docker.swarm.task.name,containers.Config.Labels.com.docker.swarm.service.name,containers.Config.Labels.com.docker.swarm.task.id <br>
  ./dockerpy.py list=containers type=stats attribute=containers.stats.name,containers.stats.id,containers.stats.memory_stats.usage,containers.stats.memory_stats.limit,containers.stats.memory_stats.max_usage,containers.stats.cpu_stats.cpu_usage.total_usage,containers.stats.networks.eth2.tx_bytes,containers.stats.networks.eth2.rx_bytes,containers.stats.networks.eth1.tx_bytes,containers.stats.networks.eth1.rx_bytes,containers.stats.cpu_stats.system_cpu_usage <br>
