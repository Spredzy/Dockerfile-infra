# Dockerfile-infra

A Dockerfile to replicate openstack-infra puppet environment 

## Installation

One needs to build all three docker images

```
#(base/) > docker built -t spredzy:infra-base .
#(sshd/) > docker build -t spredzy:infra-sshd .
#(infra/) > docker build -t spredzy:infra-infra .
```

The last image will contain systemd, a running ssh server and all the files present in an instance of infra when spawned.

Note: The presence of systemd is necessary in order to be able to start services else a user will face `Failed to get D-Bus connection: No connection to service manager.`

## Testing an openstack-infra module

Clone a module locally

```
#> git clone https://github.com/openstack-infra/puppet-lodgeit /tmp/
```

Run the docker file

```
#> docker run --privileged -d --name puppet-infra -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v ~/.ssh/id_rsa.pub:/root/.ssh/authorized_keys -v /tmp/puppet-lodgeit:/etc/puppet/modules/lodgeit -v /tmp/site.pp:/var/tmp/site.pp spredzy:infra-infra
#> ssh root@$(docker inspect --format='{{.NetworkSettings.IPAddress}}' puppet-infra)
#> puppet apply /var/tmp/site.pp
```

Edit locally (ie. `/tmp/puppet-lodgeit`), and re-run the `puppet apply` command. Iterate at will.
