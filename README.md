# world-polulation
Python application which maintains list of cities and its polpulation


**Step1:** Install and configure elasticsearch (Here i have steps for MACOS)
  Pre-requisites: install java for elasticsearch: sudo apt-get install openjdk-11-jdk
	a. brew tap elastic/tap
	b. brew install elastic/tap/elasticsearch-full
	c. elasticsearch (this command will start the elastic search service)
	d. [To test the successful installation: curl localhost:9200 (you will see the cluster details)]
	e. Create an index using command: curl -X PUT "localhost:9200/new_index?pretty" 
	f. index creation can be validated using: curl localhost:9200/_cat/indices
    
**Step2:** Load the data in to elasticsearch
	a. population data is available in json file (population.json) which should be loaded in to elasticsearch cluster using the python script load.py
	 (note: its takes some time to index the data)
  
Step3:Python flask application (app.py) with endpoints below
	a. healthcheck endpoint: (curl http://127.0.0.1:5000/health)
	b. endpoint for inserting and updating the city and its population (http://127.0.0.1:5000/city)
	c. endpoint for retreiving the data: (http://127.0.0.1:5000//city/<string:city>)
