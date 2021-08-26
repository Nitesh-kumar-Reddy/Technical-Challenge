# Terraform code to deploy three-tier architecture on azure

Challenge -1 

1. One virtual network tied in three subnets.
2. Each subnet will have one virtual machine.
3. First virtual machine -> allow inbound traffic from internet only.
4. Second virtual machine -> entertain traffic from first virtual machine only and can reply the same virtual machine again.
5. App can connect to database and database can connect to app but database cannot connect to web.

For the solution, we have created and used five modules:
1. resourcegroup - creating resourcegroup
2. networking - creating azure virtual network and required subnets
3. securitygroup - creating network security group, setting desired security rules and associating them to subnets
4. compute - creating availability sets, network interfaces and virtual machines
5. database - creating database server and database

Challenge-2

To get the entire JSON, the code can be run as:

python metadata.py

Challenge-3

To test the python function written to achieve this, run

python testgetValue.py
