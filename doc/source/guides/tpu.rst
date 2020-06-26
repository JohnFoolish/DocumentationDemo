.. _guide_to_running_on_tpu_using_google_cloud_platform:

Guide to Running on TPU using Google Cloud Platform
===================================================

.. _about_tpu:

About TPU
---------

Google’s Tensor Processing Unit, or TPU, can be used to accelerate
Tensorflow neural network computations behind the scenes. The TPU was
announced last year and recently followed up with a detailed study of
its performance and architecture. In short, they found that the TPU
delivered 15–30X higher performance and 30–80X higher
performance-per-watt than contemporary CPUs and GPUs. These advantages
help many of Google’s services run state-of-the-art neural networks at
scale and at an affordable cost. In this guide, we will walk you through
running any process that involves Tensorflow computation on a Google
Cloud Virtual Machine that leverages TPU processing power. You can read
more about the TPU
`here <https://cloud.google.com/blog/products/gcp/an-in-depth-look-at-googles-first-tensor-processing-unit-tpu>`__.

.. _how_to_get_started_with_google_cloud:

How to get started with Google Cloud
------------------------------------

Using the Google Cloud Platform services is very easy. Here are the
instructions

#. Go to `cloud.google.com <cloud.google.com>`__
#. Login with a gmail address.
#. Click on "console" - you should be directed to a dashboard.

.. _create_a_project:

Create a Project
----------------

Steps to create a project:

#. Click on the "Select A Project" option.
#. Select "New Project" and follow instructions (it may take few minutes
   for this project to show up on your dashboard).
#. Click the ≡ symbol in the top left corner and select "billing". This
   will allow you to link your project to a payment method. This is
   where you will want to add your google cloud credits.

.. _creating_a_google_cloud_storage_bucket:

Creating a Google Cloud Storage Bucket
--------------------------------------

**Note:** the following instructions are based on `this quickstart
tutorial <https://cloud.google.com/tpu/docs/quickstart>`__

In this step, we will create a Cloud Storage bucket, which will serve as
your interface to move data in and out of your Cloud VM:

#. Sign into your google account, select your project and ensure billing
   is enabled for the project.
#. Go to the `Cloud Storage Page on the GCP
   Console <https://console.cloud.google.com/storage/browser>`__
#. Create a new bucket with:

   -  a unique name of your choosing
   -  Default storage class: ``Regional``
   -  Location: ``us-central1``

#. If may take a few minutes for your bucket to show up.
#. Select [your bucket name]

   -  if starting from the dashboard, do Resources > Cloud Storage >
      [your bucket's name]

#. Select "Upload Folder" and upload the folder that contains "emade".
   This process may take few minutes. **DO NOT BEGIN THE NEXT STEP UNTIL
   THIS IS COMPLETELY FINISHED.**

   -  If the files are too large to upload all at once, set up git-lfs
      by running the following 2 commands in a Cloud Shell

      -  ``curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash``
      -  ``sudo apt-get install git-lfs``

   -  Now clone from github and copy to an empty bucket using
      ``gsutil -m cp -r [git_folder] [bucket_link]``
   -  Consider reading this
      `guide <https://cloud.google.com/solutions/transferring-big-data-sets-to-gcp>`__
      for more information on uploading large datasets to google cloud
   -  It may also be useful to `install
      gsutil <https://cloud.google.com/storage/docs/gsutil_install#deb>`__
      on your personal device to upload files
   -  **NOTE: For deep learning subteam working on CGP-CNN, please use
      the vip_shell.sh file in CGP-CNN GitHub repository. Relevant
      documentation is contained in the README. It will install and
      configure Git-LFS, download EMADE, and install all relevant pip
      dependencies. You may continue onto the next TPU step after script
      concludes.**

.. _tpu_initialization_and_connecting_to_the_cloud_vm:

TPU Initialization and Connecting to the Cloud VM
-------------------------------------------------

For this part, we will be using the cloud shell and Cloud TPU
Provisioning Utility (``ctpu``). This guide uses ``ctpu`` as a simple
tool for setting up and managing your Cloud TPU. The guide
runs ``ctpu`` from a Cloud Shell. The ``ctpu`` tool is pre-installed in
your Cloud Shell. Follow these steps to set up your TPU:

1. Open a `Cloud
Shell <https://console.cloud.google.com/?cloudshell=true>`__ window.

2. Type the following into your Cloud Shell, to check
your ``ctpu`` configuration do the following.

``ctpu print-config``

You should see a message like this:

.. code-block:: none

   2018/04/29 05:23:03 WARNING: Setting zone to "us-central1-b" 
   ctpu configuration: 
          name: [your TPU's name] 
          project: [your-project-name] 
          zone: us-central1-b 
   If you would like to change the configuration for a single command invocation, please use the command line flags.


3. You can see a list of ctpu commands by typing ``ctpu`` in the Cloud
Shell

4. Run the command ``cptu up`` to set up a Compute Engine virtual
machine (VM) and a Cloud TPU with associated services.
The ``--tpu-size`` parameter is an optional parameter that you can use
to specify the size of your Cloud TPU configuration, a single Cloud TPU
device or slices from a Cloud TPU Pod *(alpha)*.

.. code-block:: none

   ctpu will use the following configuration: 

       Name: [your TPU's name]
       Zone: [your project's zone]
       GCP Project: [your project's name]
       TensorFlow Version: 1.11
       VM:
           Machine Type: [your machine type]
           Disk Size: [your disk size]
           Preemptible: [true or false]
       Cloud TPU:
           Size: [your TPU size]
           Preemptible: [true or false]

   OK to create your Cloud TPU resources with the above configuration? [Yn]: 

5. Press y to create your Cloud TPU resources. **This process will take
a few minutes** the first time you connect to the TPU - every subsequent
time should be almost instantaneous. To learn more about what ctpu
up does, check out `this
link <https://cloud.google.com/tpu/docs/quickstart>`__

6. Verify your computing engine VM. When the ``ctpu up`` command has
finished executing, verify that your shell prompt has changed
from ``username@project`` to ``username@tpuname``. This change shows
that you are now logged into your Compute Engine VM.

-  WARNING: The TPU can use minor computing resources when idle. To
   avoid loosing credits see "Cleaning Up Cloud Resources"

.. _emade_on_your_virtual_machine:

EMADE on Your Virtual Machine
-----------------------------

Here are the instructions to get the EMADE code onto your virtual
machine (**note:** this process is not specific to EMADE, and can be
used for any codebases).

#. Download emade from your GCP Bucket using the following command that
   performs a parallel multi-threaded/multi-processing copy:
   ``gsutil -m cp -r [bucket_link] .`` You can find your [bucket_link]
   by clicking on your bucket, selecting the overview tab and copying
   the "Link for gsutil". This command copies the contents of your
   entire bucket to the current directory on your Cloud VM. Click here
   to learn more on `gsutil
   cp <https://cloud.google.com/storage/docs/gsutil/commands/cp>`__. If
   you want to only copy a certain directory, then append the directory
   path to the end of your link.
#. Python3 can be accessed with the command "python3".
#. Several packages should already be on your virtual machine - however,
   not all packages come installed.

   -  Run your code and see if it works.
   -  In the event of a missing package, simply "pip3 install" it.
   -  When we did it, we were missing pandas, scoop and psutil, but your
      code may be missing different dependencies,

.. _code_changes_to_run_tensorflow_with_tpu_support:

Code Changes to Run Tensorflow With TPU Support
-----------------------------------------------

As of now, your code is running on a Cloud VM that has access to TPUs,
but is not actually leveraging TPU power. Below are the steps necessary
to run your tensorflow code with TPU support:

In the file where your tensorflow session is instantiated:

1. Add the following import statements:

.. code-block:: python

   import os 
   from tensorflow.contrib import tpu 
   from tensorflow.contrib.cluster_resolver import TPUClusterResolver

2. Directly before instantiating your session, add:

.. code-block:: python

   tpu_grpc_url = TPUClusterResolver(project="<your-project-name>", zone="us-central1-b", tpu_names=[os.environ['TPU_NAME']]).get_master

3. Instantiate your session with the target set to ``tpu_grpc_url``. For
instance, instantiate it like:

.. code-block:: python
   
   with tf.Session(tpu_grpc_url) as sess:
      # ...

4. Congrats - If you run your code now, you will be using the power of
TPUs to run your tensorflow code.

.. _connecting_to_google_cloud_vm_from_local_machine:

Connecting to Google Cloud VM from Local Machine
------------------------------------------------

Everything done till now has been on the google cloud shell. If you want
to run it from your own system, here are the steps (taken from `this git
repo <https://github.com/tensorflow/tpu/tree/master/tools/ctpu>`__):

#. Download cptu onto your local machine

   -  Linux:
         .. code-block:: bash

            wget https://dl.google.com/cloud_tpu/ctpu/latest/linux/ctpu
            chmod a+X ctpu
   -  Mac:
         .. code-block:: bash

            curl -O https://dl.google.com/cloud_tpu/ctpu/latest/darwin/ctpu
            chmod a+x ctpu

   -  Windows: No support as of 11/12/2018.

#. While you can use ctpu in your local directory (by prefixing all
   commands with ./; example: ./ctpu print-config), Google recommends
   installing it somewhere on your $PATH. (example: cp ctpu ~/bin/ to
   install for just yourself, or sudo cp ctpu /usr/bin/ for all users of
   your machine.)
#. Configure gcloud credentials: If you have never used gcloud before,
   you will need to configure it. Run gcloud auth login to allocate
   credentials for gcloud to use when operating on your behalf.
#. Configure ctpu credentials: ctpu uses the "application default"
   credentials set up by the Google SDK. In order to allocate your
   application default credentials, run: gcloud auth application-default
   login.
#. Now your local machine shell should be able to support the same ctpu
   commands as the cloud shell.

.. _cleaning_up_google_cloud_resources:

Cleaning up Google Cloud Resources
----------------------------------

To avoid incurring charges to your GCP account for the resources used in
this quickstart

1. If still connected, disconnect from the Compute Engine VM:

``(vm)$ exit``

2. Run the following command to delete your Compute Engine VM and your
Cloud TPU:

``$ ctpu delete``

3. Run ``ctpu status`` to make sure you have no instances allocated to
avoid unnecessary charges for TPU usage. The deletion might take several
minutes. A response like the one below indicates there are no more
allocated instances:

.. code-block:: bash

   2018/04/28 16:16:23 WARNING: Setting zone to "us-central1-b" 
   No instances currently exist.
           Compute Engine VM:     --
           Cloud TPU:             -- 

4. When you no longer need the Cloud Storage bucket you created during
this tutorial, use the ``gsutil`` command to delete it.
Replace ``YOUR-BUCKET-NAME`` with the name of your Cloud Storage bucket:

``$ gsutil rm -r gs://YOUR-BUCKET-NAME``

This is not necessary every time, as you can keep your bucket alive at a
very low cost. This will save time in future uses as you will not have
to upload emade again. See the Cloud Storage pricing guide for free
storage limits and other pricing information.

However, **IT IS HIGHLY RECOMMENDED TO DELETE YOUR VM AND TPU AS THEY
ARE MORE PRICEY**.

.. _common_problems_and_their_solutions:

Common Problems and Their Solutions
-----------------------------------

**SSH Error 255 and Permission Denied (Publickey)**

1. Manually create a VM using the google cloud console (Compute
Engine>VM Instances>Create)

-  Make sure the name is the same as your username, or the TPU you
   create later won't use this VM
-  Give the VM sufficient disk space ~250GB should work
-  Under "Firewall" allow HTTP/HTTPS traffic. This is the main issue
   causing the problem

2. Use the command ``ctpu up`` to initialize the CTPU, it should run on
the VM you just made.

3. Manually creating a VM means there are less packages preinstalled, so
you may want to install git and pip with the following commands

.. code-block:: bash

   sudo apt-get install git
   sudo apt-get install python3-setuptools
   sudo easy_install3 pip

**KeyError TPU_NAME**

1. The environment variable is not initialized so you must export it
with the following command: ``export TPU_NAME=``

2. Your VM is also likely to be missing some package dependencies, so
run the following commands:

.. code-block:: bash

   sudo pip install --upgrade google-api-python-client
   sudo pip install --upgrade oauth2client

**psutil Import Errors** (**Note:** only seen after SSH Error 255 fix)

Python3-dev is not set up, so you must install it with the command

``sudo apt-get install python3-dev``

**cv2 Import Errors**

There are several dependencies that could cause this, so here are a few
things to try:

1. Older versions of opencv-python have less dependencies, so you can
try reverting to version 3.3.0.9

-  There are other distros with less dependencies, like
   opencv-python-headless which may help

2. If you can't get around installing extra libraries, then you will
have to install whatever the error says you are missing

-  For example ``ImportError: libgthread-2.2.so.0 ...`` means you need
   to run the command ``sudo apt-get install libglib2.0-0``
