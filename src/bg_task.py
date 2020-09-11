import subprocess
from time import sleep

def read_tasks(mongo):
    """
    Infinite loop that reads tasks with status "Not started" from db
    """
    while True:
        query = mongo.db.tasks.find({"status" : "Not started" }) #query undone tasks
        for task in query:
            task_to_run = str(task['cmd']) # Store task to run
            try:
                process = subprocess.Popen(task_to_run.split(), stdout= subprocess.PIPE, 
                                                        stderr = subprocess.PIPE)
                process_output =str(process.communicate()[0])
                process_status = "Done"
            except Exception as e:
                process_output = "There was an error running the task: " + str(e)
                process_status = "Error"


            mongo.db.tasks.update(
                {"_id" : task['_id']}, 
                {"$set":
                    {
                    "status" : process_status,
                    "output" : process_output
                    }
                }
            )
        sleep(10)
        








