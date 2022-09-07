# Simple example of web scraping with Selenium in Python  
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=3KAJXTAYQC7BW)

Support open source software and help me in further development. Thank you for every donation and star!

### What is it? 
The program make automated search on pracuj.pl website to find interesting job offers according to keyword and location. Then, each job offer from search result is being collected. Subsequently result is exported through Pandas to create beautiful .xlsx file full of job offers. At the final step the .xlsx file is send to given email. 

We are starting here:<br>
![pracuj.pl website](./readmeImages/pracujWebsite.png "pracuj.pl website")<br>
To get the result:<br>
![mail result - received job offers](./readmeImages/mailResult.png "mail result - received job offers")

### How it works?
! The automation happens with use of Selenium.<br>
We want to get to the section with advanced search and do appropriate scraping of job offers. 
1. Find advanced search and click it.<br>
![advanced search position](./readmeImages/advancedSearchPosition.png "advanced search position")
2. Find specific fields to enter keyword and location.<br>
![advanced search](./readmeImages/advancedSearch.png "advanced search")
3. Find "Pozostałe" (it means other) button and click it to add additional details to our search. We want to find only new offers (added within 24 hours). Then find and click the button that contains "Pokaż oferty"(Show offers).<br>
![other details about search](./readmeImages/otherDetailsSearch.png "other details about search")
4. Collect each job offer from every page of result as block of "offer info".<br>
![search result](./readmeImages/searchResult.png "search result")<br>
If there is more than one page of result: find next page button and until exists go to the next page to once again collect job offers.<br>
![next page button](./readmeImages/nextPageButton.png "next page button")
5. Get job title, website with details and company name from each block with offer info.<br>
![job offer details](./readmeImages/jobOfferDetails.png "job offer details")
6. Create table from gathered data and export it to excel
 # Simple example of web scraping with Selenium in Python  
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=3KAJXTAYQC7BW)

Support open source software and help me in further development

### What is it? 
The program make automated search on pracuj.pl website to find interesting job offers according to keyword and location. Then, each job offer from search result is being collected. Subsequently result is exported through Pandas to create beautiful .xlsx file full of job offers. At the final step the .xlsx file is send to given email. 

We are starting here:<br>
![pracuj.pl website](./readmeImages/pracujWebsite.png "pracuj.pl website")<br>
To get the result:<br>
![mail result - received job offers](./readmeImages/mailResult.png "pracuj.pl website")

### How it works?
! The automation happens with use of Selenium.<br>
We want to get to the section with advanced search and do appropriate scraping of job offers. 
1. Find advanced search and click it<br>
![advanced search position](./readmeImages/advancedSearchPosition.png "advanced search position")
2. Find specific fields to enter keyword and location<br>
![advanced search](./readmeImages/advancedSearch.png "advanced search")
3. Find "Pozostałe" (it means other) button and click it to add additional details to our search. We want to find only new offers (added within 24 hours). Then find and click the button that contains "Pokaż oferty"(Show offers)<br>
![other details about search](./readmeImages/otherDetailsSearch.png "other details about search")
4. Collect each job offer from every page of result as block of "offer info"<br>
![search result](./readmeImages/searchResult.png "search result")<br>
If there is more than one page of result: find next page button and until exists go to the next page to once again collect job offers.<br>
![next page button](./readmeImages/nextPageButton.png "next page button")
5. Get job title, website with details and company name from each block with offer info<br>
![job offer details](./readmeImages/jobOfferDetails.png "job offer details")
6. Create table from gathered data and export it to excel
    df = pd.DataFrame(jobOffersList)  
    df.to_excel(r'jobOffers.xlsx', index=False)
7. Send the complete message with .xlsx attachment to recipient address
8. DONE!
![mail result - received job offers](./readmeImages/mailResult.png "mail result - received job offers")

### How to use it? 
* Setup a virtual envinronment inside clone directory
* Install modules from requirements.txt with:
    pip install -r requirements.txt
* Run main.py in IDE of your choice 
* Admire how amazing Selenium is 