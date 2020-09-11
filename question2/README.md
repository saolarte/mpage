# mpage

BUILD INSTRUCTIONS
- Run 'docker-compose up' to start mongo-db and Flask server

TO TEST END POINTS:
Endpoints become available in localhost:8000. Perform requests using Postman

* /new_task [POST]
    json formated input with "cmd" key should be passed
    Sample input:
        {
	        "cmd" : "pwd"
        }
    Returns 'id' key-value pair

*/get_output/<id> [GET]
    <id>: Corresponds to task id (Returned upon creation) 
    Returns:
        {
            "output": "/app",
            "status": "Done"
        }
