# Dockerfile-infra

A Dockerfile to replicate openstack-infra puppet environment 

## Testing an openstack-infra module

Clone a module locally

```
#> git clone https://github.com/openstack-infra/puppet-lodgeit /tmp/
```

Run the docker file

```
#> docker run -i -t --name puppet-infra -v /tmp/pppet-lodgeit:/etc/puppet/modules/lodgeit spredzy:puppet-test /bin/bash
#> puppet apply -e "include ::lodgeit"
```

Edit locally (ie. `/tmp/puppet-lodgeit`), and re-run the `puppet apply` command. Iterate at will.
