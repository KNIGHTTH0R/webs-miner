#TODO List

##Thoughts about how it should be work.

###General flow:
- Setup and run the core.
- Get the user preferences web links.
- Match the urls with the class templates and extract description and target (price).
- Save every product in the data base.
- Generate the html structure for index page and every chart.

###Web page Class Template.
- This package have every web for example Asus Store is almost the same HTML syntax for all the store web.
- In this templates we don't need to import the pkg http module this function is for core module.
- In this case the class template only import the core module for all the functions.
- This class temple should not be save in the git project.
- Interesting all the tag modules and the filters are in pkg module, should we need to call inside of this class.
- If it is the case, what is the point of this structure. Answer: It setup all, ready to create the class templates.
- Wait this class should be call core versus directly pkg because if something change I need to replace in 1000 files.
- In this way I only change and test in the core.wrapper_html_tag or something like this.

Eureka!

- Reset! This class only needs to return 2 params: Description and Target which is the price or word, or whatever.
- The Product/Title should be get from the preferences yaml file that's mean we only need to extract the description.

###Preferences YAML.
- It should be has URL, Short title.

###Data base.
- Save the information into a data base every url has one data base.
- Sounds a good idea to have a NonSQL data base.
- It saves in general (one time) the short title and description then it records every UTC date and target.

###Show charts.
- Show an HTML with links, the first one should be "show all charts together" then the link for every url.
- Visualization, ff I choose show all; it shows on right the list of products and in the chart the target and date.
- Visualization, if I choose individually chart it shows teh title, description and the chart whit the target and date.

##New features:

###Multi products/targets in one url.
- What happens if I have the url for the Asus Gaming laptops and I want to extract all the computers.
- The problem is the visualization in the chart just because how I say this is the ROG Laptops and it has
multi-targets... How I need to save in the data base and how I need to present the information in the charts?
