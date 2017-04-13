#!/usr/bin/python

import docker
import sys

def printdata(thekey,thekeyname,thevalue,filterattribute):
  if(type(thevalue) is dict):
    for key,value in dict.items(thevalue):
      printdata(key,thekeyname+"."+str(key),value,filterattribute)
  elif(type(thevalue) is list):
    for key in thevalue:
      printdata(key,thekeyname,key,filterattribute)
  else:
    if(filterattribute[0]=="all"):
      print str(thekeyname)+"="+str(thevalue)
    else:
      for attr in filterattribute:
        if(thekeyname.endswith(attr)):
          print str(thekeyname)+"="+str(thevalue)
  return

def getdockerinfo(listtype,datatype,filterattribute):
  count=0
  if(datatype=="info"):
    client = docker.from_env()
    if(listtype in("images", "services", "nodes", "containers", "networks", "volumes")):
      for lt in getattr(client,listtype).list():
        count=count+1
        for key,value in dict.items(lt.attrs):
          printdata(key,str(count)+"."+listtype+"."+str(key),value,filterattribute)

    elif(listtype in ("client", "swarm")):
      for key,value in dict.items(getattr(getattr(client,listtype),attrlist[listtype]) if listtype == "swarm" else getattr(client,attrlist[listtype])()):
        printdata(key,str(count)+"."+listtype+"."+str(key),value,filterattribute)

  elif(datatype=="stats"):
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    if(listtype == "containers"):
      for lt in client.containers(quiet=False, all=False, trunc=False, latest=False, since=None, before=None, limit=-1, size=False, filters=None):
        statdata=client.stats(container=lt["Id"],decode=True,stream=False)
        count=count+1
        for key in statdata:
          printdata(key,str(count)+"."+listtype+"."+datatype+"."+str(key),statdata[key],filterattribute)

  return

attrlist = {"client":"info", "swarm":"attrs"}

if(len(sys.argv) != 4):
  print "Incorrect number of args exiting"
  print "  Usage: ./dockerpy.py list=<LISTTYPE> type=<DATATYPE> attribute=<ATTRIBUTE>"
  print "    (Required) list should be one of the following: images, services, nodes, containers, networks, volumes, client, swarm"
  print "    (Required) type should be one of the following: info, stats"
  print "    (Required) attribute is the attribute to return data for. If 'all', then returns all attributes."

  sys.exit()

for arg in sys.argv:
  if(arg.startswith("list=")):
    listtype = arg.replace("list=","")
  elif(arg.startswith("type=")):
    datatype = arg.replace("type=","")
  elif(arg.startswith("attribute=")):
    filterattribute = arg.replace("attribute=","").split(",")
getdockerinfo(listtype,datatype,filterattribute)

sys.exit()

