.. _running_on_the_cloud:

Running on the Cloud
====================

.. _running_on_google_cloud:

Running on Google Cloud
-----------------------

To run on Google Cloud, make a single virtual machine (VM) using
Google's precompiled deep-learning image that they developed to be
optimized for their processors with Intel. Access the platform via the
"SSH" button on the VM control panel. Do not install anaconda, but
rather install all needed packages using pip3, taking care not to
reinstall a non-optimized version of tensorflow, keras, numpy or scipy.
Also start a local mySQL server. Run EMADE as a local run within a
"screen" daemon as described below. Start workers on a separate deamon.

.. _making_an_aws_educate_account:

Making an AWS Educate Account
-----------------------------

You can apply for an AWS Educate account
`here <https://www.awseducate.com/registration?refid=Qe5oPnjlwk6UyeRP88DLWK8GIxfK5Ipt>`_,
and you should receive a preliminary $100 credit immediately.

.. _about_aws:

About AWS
---------

Amazon Web Services (AWS) is a massively scalable service. Therefore, there are lots of ways you could use AWS to run EMADE; you could choose to run EMADE with centralized storage for very large datasets on the S3 service  or as a containerized docker service, for example. However, because an individual Linux instance on the Amazon Elastic Compute Cloud (EC2) is cost-effective, relatively standard across current industry practices as a *nix system, and scalable to include up to 16 GPUs and local storage on an SSD, this guide will proceed with a machine instance running Amazon Linux. This service is called EC2 in Amazon’s nomenclature. This offers the added advantage that you can create an image of your base instance—software installation and data included—and have it to share with your teammates. Contact Scott Heston for access to a pre-configured machine image or follow `this guide <https://datanextsolutions.com/blog/aws-how-to-copy-ec2-instances-to-another-account/>`_ to clone your own image.

.. _operating_system:

Operating System
----------------

Amazon Linux offers optimization for AWS, and uses the yum package
manager. By using Amazon Linux instead of a standard distribution like
Ubuntu, you can avoid installing specific drivers like is necessary on a
VM-Ware host, for example.

.. _accessing_an_aws_node_via_ssh:

Accessing an AWS Node Via SSH
-----------------------------

SSH is used to access your node, and the corresponding push/pull tool to
exchange files is SCP. You can read more about these tools by typing man
ssh or man scp on a \*nix system. On windows, you must install an SSH
client, like PuTTY. Note that you will need to use the -i flag with both
ssh and scp to provide your local key—which you must download from the
AWS console—for access to AWS. The user for an Amazon Linux instance is
always ec2-user. For example:

``scp -r -i CERTIFICATE.pem LOCALDIRTOPUSH ec2-user@REMOTEURLFROMAWSCONSOLE:PATHTOPUSHTO``

Again, this command will only work on Windows after installing PuTTY,
but comes preinstalled on Linux or macOS.

.. _emade_installation:

EMADE Installation
------------------

EMADE should be installed through anaconda or miniconda if you intend to eventually implement any primitive that needs a GPU to train efficiently. This is because one instance of Python cannot have tensorflow compiled for CUDA and tensorflow compiled for CPU execution. (This will give a libcuda.so not found error.) For example, a premade image might include one conda environment called gpu and another called noGPU, so that you can only pay for GPU access when you need it. 

.. _database_initialization_collaborating_with_several_aws_accounts:

Database Initialization // Collaborating with Several AWS Accounts
------------------------------------------------------------------

Because our lab is structured into sub-teams, it is likely that you will want to set up a DB that everyone can access via their instances or personal computers. You can do this by creating a free-tier database through AWS’s relational database service (RBS) and configuring the security parameters appropriately; EMADE can connect to a mySQL RDS service, but the containing security group must include the IP addresses of every user. A good way to test for a connection is to try to login using MySQL Workbench, which is a free GUI for managing SQL DBs and is also useful in reading results from EMADE.
Note that the -w flag fed into launchGTMOEP.py will run only workers. Two masters should never run at the same time on the same DB.  

.. _necessary_packages:

Necessary Packages
------------------

Following the standard install instructions within the README.md file of
the Git repository should be sufficient to install EMADE with the
additional prerequisite of a C compiler:

``sudo yum install gcc``

Additionally, note that conda is designed to never be run as a
superuser; i.e. never type “sudo conda”.

.. _file_manipulation:

File Manipulation
-----------------

The read/write time from a local SSH to Amazon Linux instances on the
school network is excellent. It takes about 10 minutes to push 7 GB to
an EC2 instance, depending on network congestion. Cloning the Git
repository is also very fast. You may need to resize your instance’s
drive if your dataset is more than a trivial size. You can do this by
changing the volume under elastic block store that is listed as your
instances’ mounted drive on the AWS console. You will then need to
either restart the instance or issue a modification command
`here <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modify-volume.html?icmpid=docs_ec2_console>`_.

.. _changing_instance_resources:

Changing Instance Resources
---------------------------

See a list of EC2 instance types `here <https://aws.amazon.com/ec2/instance-types/>`_. Note that the free tier with only 1 GiB of RAM is equivalent to a low-end raspberry pi; it won’t load EMADE into memory. You need at least 2 GiB to start running trivial feature-data problems for validation purposes. 

.. _daemonizing_processes_with_screen:

Daemonizing Processes with Screen
---------------------------------

If you run an instance of EMADE through an SSH instance, it may time out
and requires the client to maintain a connection. Use the Linux command
screen to daemonize an EMADE run. “screen” will start a session. “screen
-r” restores the same terminal session to a later SSH instance.

FAQ
---

**Why is “sudo yum install” not installing where I can see the files?**
By executing yum as super user, you are repointing your HOME
environmental to the root user folder. Without root access, you cannot
read from or write to this folder. You can become root by running the
“sudo su” command, but you must be careful to not override engineering
safeguards as superuser. Note that during some installations (e.g.
mysql, miniconda) it may be helpful to force installation into your home
folder instead of the root user folder.

**How do I get AWS credit?**

If you apply with your .edu account
`here <https://aws.amazon.com/grants/>`__, you’ll be approved for an
instant $100. Beyond that, OIT recommends undergraduates apply for
additional education grants. Consult
`here <https://support.cc.gatech.edu/facilities/research-clusters>`__
Emory’s IT department also recommends AWS education grants.

**Are there other Amazon services I could use besides EC2?**

AWS has been around since 2004, and has grown to include a massive
amount of services. You can research different ways to store your data:
S3 and EFS offer different advantages. It is unlikely that you would
need another DB service besides a MySQL database. It may be worth
researching how EMADE could be run on an Elastic Beanstock, Docker
container, or maybe even incorporating Amazon lambda functions only for
functions that need to run on a GPU.
