############################
Hosting Documentation Online
############################

In all of the searching to determine the best online hosting services
for static site generators, we reached the conclusion that the two 
front runners were `Readthedocs <https://readthedocs.org/>`_ and
 `Netlify <https://matplotlib.org/sampledoc/index.html>`_. Both of 
them interfaced with Sphinx so that they could automatically generate
the html documentation from the restructured text alone, and both of
them interfaced with GitHub/GitLab/Bitbucket so that the websites 
would automatically be updated whenever the source repo was pushed
to. Additionally, both services were free to use and let the user
customize the domain name to a degree. In our time working with both
Netlify and Readthedocs, we found that Readthedocs was considerably
easier to set-up, collaborate on, and integrate with GitHub. 

Comparisons between Hosting Options
-----------------------------------
The biggest downside to Netlify was the fact that their free service
only allowed for one person to be the editor/maintainer. For our team 
of three, this meant that only one person was able to access the 
hosting account in order to make changes or adjust the settings. 
Meanwhile, Readthedocs was extremely easy to add team members to 
collaborate with, and it took our team all of 10 minutes to get
everyone set up with their own account. Additionally, Readthedocs is 
Sphinx's official choice of website hosting, and while Sphinx is the 
only real static site generator it uses (in contrast to the wide 
range availible at Netlify), we did not run into any issues in 
generating the html from our source documentation. Readthedocs' UI is
also very easy to use to view the documentation on different branches
whereas Netlify ran into quite a few issues. It is our 
recommendation that if you are trying to host your documentation on a
website, Readthedocs is the better option, however Netlify will also 
work with some extra effort. 

Private GitHub Addendum
-----------------------
Currently, hosting documentation on a service such as Netlify or 
Readthedocs is easiest when using a public git repo. Sadly, 
Enterprise GitHub does not count as a public git repo. In our 
attempts to set up the online hosting from a Enterprise GitHub, we
encountered many problems along the way. We found a few websites 
where people had configured it to work, but doing so took a lot of
extra hoops and techinical experience. We were not able to make this 
work for the documentation demo.

Setting up with Readthedocs
###########################
To set up your public documentation, follow the below steps:

# Create a Readthedocs account at https://Readthedocs.org, linking
  this to your GitHub account makes later steps easier.
# Go to import a repository, and then you can past the link to the 
  Git repo into the Repository URL area.
# Add a GitHub incoming webhook in the integrations tab
# Add the webhook url (listed in the integrations tab) to the 
  Webhook tab of your git repo.
# Now, your website should automatically be updated whenever you 
  push to the remote repo.
# You can add collaborators by including their names in the 
  maintainer tab.
# You can deploy many different branches by navigating to the 
  Versions tab and then making the branches you want published 
  public and active. 

Setting up with Netlify
#######################  
To host your documentation with Netlify, follow the below steps:

# Create a Netlify account at https://app.netlify.com
# Set the GitHub directory as the Repository under build settings
# Include the following for your build command::
      sphinx-build -b html [source dir] [output dir] 
	  
  where the source dir is the path from your root directory to your
  Sphinx **conf.py** file, and output dir is the path that you will
  have the output html files under.
# Set your Publish directory as the output directory from the 
  previous step.  
# If you want to publish multiple branches, then you can edit the 
  Contexts section. Production branch should be set to your main
  branch, and then you can select other branches you want to include.
  This step caused us multple issues in contrast to Readthedocs, as 
  Netlify is not as set up for building with Sphinx.
# Without a paid subscription, you are unable to add additional 
  collaborators.  






