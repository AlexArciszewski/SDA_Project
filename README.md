* [General info](#generalinfo)
  <details>
   <summary>Click here to see general information about <b>Project</b>!</summary>
   <b>Covid-19 report application</b> is a simple application that allows counting active cases of SARS-Cov-2 infection and then         presents the results as a simple graph of the number of infections as a function of time. 
   </details>
* [Technologies](#technologies)
   <details>
   <summary>Click here to see information about <b>Project Technology</b>!</summary>
   <b>Covid-19 report application</b> The application was developed in the Django framework(Python). HTML was used to create the         templates.
    
<ul>
<li>asgiref   	3.7.2 </li> 
<li>Django     4.2.2 </li> 
<li>packaging  23.1  </li> 
<li>Pillow      9.5.0</li> 
<li>pip        23.1.2</li> 
<li>plotly     5.15.0</li> 
<li>setuptools 60.2.0</li> 
<li>sqlparse    0.4.4</li> 
<li>tenacity    8.2.2</li> 
<li>tzdata     2023.3</li> 
<li>wheel      0.37.1</li> 
</ul>

   </details>

* [Setup](#setup)  
  <details>
  <summary>Click here to see the setup <b>Project</b>!</summary>
  <b>For the application to work properly, it is necessary to download it from the repository. The repository can be found at the     following link: https://github.com/AlexArciszewski/SDA_Project.</b> After downloading the application, start the server and       that's   it.
  The application consists of 5 tabs.
  <li>1. http://127.0.0.1:8000/covid_app/  </li> 
   There is a front page with the possibility to redirect to the  
   The page for adding users. 
  <li>2. http://127.0.0.1:8000/users/create/</li> 
    This is the page where it is possible to add users.     
  <li>3. http://127.0.0.1:8000/users/edit/x/</li> 
    The page where it is possible to edit a users.
    In the x, insert the number of the user which, you want to edit. 
  <li>4. http://127.0.0.1:8000/users/delete/x/</li>
    The page where you can delete a user. 
    In place of x, insert the number of the user you want to delete.
  <li>5. http://127.0.0.1:8000/dashboard/ </li>
    Graphical representation of the results obtained. 
    Graph collecting information from users showing the number of infections as a function of time.
</details>







* [More detailed information about modules](#more-detailed-information-about-modules)
  <details>
  <summary>Click here to see general information about <b>Project modules</b>!</summary>
  <b>Covid-19 report application most important module</b> is a Plotly graph of the number of infections in a function of time.      The main code of the graph is sotred in thve main_web views.py in the dashboard function. The x_date and y_date list store the     coordinates of the points necessary to create a graph. Graph template is stored in dashboard.html file.  
  </details>

* [Application view](#application-view)
    <details>
   <summary>Click here to see the Application view of the <b>Project</b>!</summary>
   <b>Covid-19 report application</b> graph of the number of infections as a function of time.
    https://github.com/AlexArciszewski/SDA_Project/assets/102918054/b5d7282b-4810-4694-ab98-c0545f78e4d4
  </details>

