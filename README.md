# News_Aggregator_Website
A Website  which shows the real news using multiple sources


[IN]ews
                                    “A NEWS AGGREGATOR WEBSITE”

Name of 1st Student : Ayush Sinha  
  17bit118@ietdavv.edu.in | 8602189022

Name od 2nd Student : Aman Sohani
  17bit110@ietdavv.edu.in | 9993899208

Name of 3rd Student : Pragyesh Jain 
   17bit134@ietdavv.edu.in | 7999419106

Name of 4th Student : Shivam Patidar 
17bit152@ietdavv.edu.in | 9340949332

Name of the Supervisor : Mr. Manoj Pawaiya sir 
mpawaiya@ietdavv.edu.in | 9926839606


                                   DEPARTMENT OF INFORMATION TECHNOLOGY

Keywords: Aggregator, News, Website


1. INTRODUCTION 

Do you want to read the latest news and updates from your favorite blogs all at one place?
If so, then news aggregator websites are the best option for you. These websites automatically show the latest content from your favorite websites on one single page.
News aggregator websites allow users to view news and updates from various sources at one
convenient location. They fetch the data, organize them in tags / categories, and display it in the right order for easier consumption. You can also think of them as a compilation of news and updates presented according to user’s preference. Using news aggregators, you don’t need to visit different websites for their latest content. Instead, you can find all the content in one place.
We are trying to build a News Aggregator website Using Django as our technology stack, so our main aim here is to make Available many popular website’s news at one place so that anyone can get their favorite news at any time.
Some similar projects from which we get to know about our idea are Hindustan times, times of India, dainik jagran, this all platforms shoe news from only their sources but we will combine these website together.


2. LITERATURE SURVEY 

In the Existing System if an individual wants to read news then he had to go to different places for reading different categories of news or he don’t know that which news websites are best for having informed very soon and always show important news which we want. Some very popular news websites are:

-	https://timesofindia.indiatimes.com/
-	https://www.bbc.com/news
-	http://www.espn.com/espn/news/more/_/sport/espn
-	https://www.jagran.com/
-	https://www.bhaskar.com/
-	https://www.patrika.com/

Main issues with these website are that each website show there own news in there own words so it can be varied sometimes, and this is possible that some news website is not showing the news which is important so here we looked into this problem and thought about content aggregation or we can say that News aggregation. Let’s agree that the information age can be overwhelming without news aggregator websites. Not only is there a lot of information in total, but it is also scattered all over the web. In order to save time, you can bring all of the news, updates, insights, tips, guides, articles into one location with content aggregators. With that said, let’s take a look at the best news aggregator websites :

-	https://feedly.com : Feedly is one of the most popular news aggregator websites on the internet. It allows you to create a news stream of your own with latest content from your favorite publishers. 
-	https://news.google.com : Google News is a powerful news aggregator powered by Google’s sophisticated search technologies, AI, and user’s own search history. By default, it shows you top news stories based on your geographical location. It offers the latest news and updates for local, regional, international, business, technology, entertainment, sports, science, and health news.
-	https://news360.com : News360 is one of the most popular news aggregator apps on the internet. It lets you find world news as well as stories around your interests. It is an excellent alternative to Google News and Feedly.
-	https://getpocket.com : Pocket is another news aggregator app where you can explore the most popular content across the internet. It also lets you create your own reading space by saving the content you like. Pocket features different types of content, including articles, videos, and stories from a wide range of publications. It has various content categories like must-reads, trending, tech, finance, health, etc. for easy browsing.

After Watching this great website we are also going to implement our own version of a news aggregator website.


3. PROBLEM DOMAIN

In the Existing System if an individual wants to read news then he has to go to different places for reading different categories of news or he don’t know which news websites are best for having informed very soon and always show important news which we want. So the main issues with these website are that each website show there own news in there own words so it can be varied sometimes, and this is possible that some news website is not showing the news which is important so here we looked into this problem and thought about content aggregation or we can say that News aggregation
Our main Objective is to make a Website which comprises multiple news sources so that no one can miss anything.


4. SOLUTION DOMAIN 

Here we are solving the problem of aggregating news from different websites using Django (Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.) on Backend and HTML5, CSS3, Bootstrap and JavaScript for creating Frontend. We may also use jQuery for ajax calls. 
We will be taking out news articles from different websites through web scraping using Beautiful Soup library in python and then storing it in our Database. And if some news website is providing an API then we will use that api, for getting the Articles in proper formatted manner.
Our website will have different news feeds for different users based on their initial preferences which they will set during signing up. Hence our website will be having an authentication system implemented for logging in our website. We will be categorizing news from different sources in different domains like sports, technology, science, health and fitness, political, entertainment and many more. 
We will also implement lazy loading in our website so that all news articles will not be loaded at an instant which will save bandwidth, instead they will be loaded as the user scrolls down the page. Our website will also have a search option for searching a particular news across different categories and sources of news. For searching we will use regular expression or django ORM queries or we can directly hit the get request to the API which we are using. In the database we will be storing users news preferences and their personal credentials (name, email, contact no,.etc). 
At last we are also adding polling functionality to some article which will be manually handled by admin and by using this we can get user views on any scenario (like which party will won election, or which team will win match), Last but not least we are also thinking of adding Podcasts to our website as an additional feature.


5. SYSTEM DOMAIN 

Our News Aggregator Website will be designed in such a manner so that it can even work on CPUs with single core, additional cores would definitely speed up the execution. Also we try to make the web app which is compact in size(memory). Hence, hardware requirement is minimal. 
Django (a Python based framework) would be required to build and run the project as a development time and run time dependency.

User Interface:
The user interface will run on any Web Browser.


6. APPLICATION DOMAIN 

•	The main application of iNews is that it gives the most relevant and appropriate news to the fellow user.
•	It will also make sure that the news will revolve around the interest of the user.
•	It will pick up the news category wise from the wholesome and will present it to the user, this will help the curious user to know what's happening around in the globe.
•	Its another  application is that it will help know the public opinion through polling feature.



7. EXPECTED OUTCOME 

•	iNews is a news website that selects latest news from multiple national and international sources and present news in personalized manner for you.
•	iNews curates all types of news and headlines from topics like politics, entertainment, business, technology, startups, world, sports – all in one place.
•	Get updated with the latest news and current affairs in a JIFFY!
•	News is sourced from various categories and various sources, making sure that you always get the best.
•	iNews brings all of the day’s news together in one beautifully simple, elegantly quick interface.
•	There is also pooling functionality on hot topic to get an user view.


References :

[1] Alaa Mohamed, Marwan Ibrahim, Mayar Yasser, Mohamed Ayman, Menna Gamil, Walaa Hassan, “News Aggregator and Efficient Summarization System”, (IJACSA) International Journal of Advanced Computer Science and Applications, Vol. 11, No. 6, 2020.

[2] https://steelkiwi.com/blog/how-to-build-content-aggregator-website/ , “Content Aggregator Website Examples and How to Build One”,

[3] https://en.wikipedia.org/wiki/News_aggregator , “News Aggregator Wiki”,

[4] https://www.wpbeginner.com/showcase/best-news-aggregator-websites-how-to-build-your-own 

[5] https://themeisle.com/blog/news-aggregator-websites-examples/ 

[6] https://www.djangoproject.com/ . “Django documentation”

