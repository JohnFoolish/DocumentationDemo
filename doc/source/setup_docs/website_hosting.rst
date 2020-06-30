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

Setting up with Readthedocs
###########################


Setting up with Netlify
#######################  