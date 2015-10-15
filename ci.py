#!/bin/python

import jinja2
import os
import re

def _extract_role(node):
  """Return the site.pp content of a specific node"""
  manifest = ''
  in_manifest = False

  with open('site.pp', 'r') as site_pp:
    for line in site_pp:
      if in_manifest == True and re.search('^}', line):
        break
      if in_manifest == True:
        manifest += line
      if re.search("node '%s" % node, line):
        in_manifest = True

  return manifest.strip()

def _generate_docker_compose(node, tmp_path):
  """Generate the docker-compose.yml file"""
  templateLoader = jinja2.FileSystemLoader( searchpath="/" )
  templateEnv = jinja2.Environment( loader=templateLoader )
  TEMPLATE_FILE = "/home/spredzy/Projects/docker/infra-ci/deploy/docker-compose.yml.tmpl"
  template = templateEnv.get_template( TEMPLATE_FILE )
  composeVars = { "node" : node.replace('.', ''), "tmp_path" : tmp_path }
  with open("%s/docker-compose.yml" % tmp_path, 'w') as docker_compose:
    docker_compose.write(template.render( composeVars ))

def _setup_folder(node):
  """Setup the foder to test the manifest.

  This includes :
    * create the site.pp
    * generate the docker-compose.yml
  """
  node_manifest = _extract_role(node)
  folder_name = node.replace('.', '_')
  tmp_path = "/tmp/%s" % folder_name
  if not os.path.exists(tmp_path):
    os.makedirs(tmp_path)
  with open("%s/site.pp" % tmp_path, 'w') as site_pp:
    site_pp.write(node_manifest)
  _generate_docker_compose(node, tmp_path)
  

def process():

  # TODO(spredzy): Get those lists from a yaml configuration file
  nodes = ['paste.openstack.org', 'wiki.openstack.org']
  platforms = ['precise', 'trusty', 'wheezy', 'jessie', 'centos7']

  for node in nodes:
    _setup_folder(node)

if __name__ == "__main__":
  process()
