#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,name=None,job=None):
        self._name="Name must be string between 1 and 25 characters.\n"
        if name is not None:
            self.set_name(name)
        
        if job is not None:
            self.set_job(job)

    def get_name(self):
        return self._name 
    def set_name(self,name):
        if (type(name) == str) and (0 < len(name)<25):
            self._name= name.title()
        else:
            print('Name must be string between 1 and 25 characters.')
    name= property(get_name,set_name)

    def get_job(self):
        return self._job
    def set_job(self,job):
        if job not in APPROVED_JOBS:
            print('Job must be in list of approved jobs.')
        else:
            self._job = job
    job = property(get_job,set_job)
