import multiprocessing
import os
import time

class Worker:
    def info(self, data):
        print(f"Process info ID: {os.getpid()}")
        for item in data:
            print(f"id: {item["id"]}, name: {item["name"]}, age: {item["age"]}, salary: {item["salary"]}")

    def create(self, data):
        print(f"Process create ID: {os.getpid()}")
       # get max id 
        max_id = max([item["id"] for item in data])
        # insert new data
        data.append({"id": max_id + 1, "name": "David", "age": 40,"salary": 80000})

        return data

if __name__ == "__main__":
    # create a worker instance
    worker = Worker()
    # manager : to manage shared data between processes , it is a singleton object, so it is shared between all processes
    # and it is used to create a list, dict, etc. that can be shared between processes
    # create a manager instance
    manager = multiprocessing.Manager()
    # create a warker list
    data = manager.list(
        [
            {"id":1, "name": "Alice", "age": 30,"salary": 50000},
            {"id":2, "name": "Bob", "age": 25,"salary": 60000},
            {"id":3, "name": "Charlie", "age": 35,"salary": 70000}
        ]
    )
    # create a process
    p1 = multiprocessing.Process(target=worker.create, args=(data,))
    p2 = multiprocessing.Process(target=worker.info, args=(data,))
    # start the process
    p1.start()
    p2.start()
    # get the process id
    print(f"Process create ID: {p1.pid}")
    print(f"Process info ID: {p2.pid}")
    # wait for the process to finish
    p1.join()
    p2.join()
    # check process is alive
    print(f"Process create is alive: {p1.is_alive()}")
    print(f"Process info is alive: {p2.is_alive()}")





