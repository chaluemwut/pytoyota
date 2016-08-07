# -*- coding: utf-8 -*-
from flask import Blueprint, request, url_for
from iweb.controller import ViewController
from model.toyota_documents import *

base_name = 'toyota'
app_name = '/'+base_name
toyota = Blueprint(base_name, __name__)

class LoginController(ViewController):
    def process(self):
        param = self.get_post(['email','password'])
        if param['email'] == 'toyota' and param['password'] == 'toyota':
            self.page_name = 'list.html' 
            return {'result':Problem.objects}   
        else:
            self.page_name = 'index.html'
            return {'error':'User name password not correct'}

class List(ViewController):
    def process(self):
        print('******* start list')
        self.page_name = 'list.html' 
        return {'result':Problem.objects}       

class Save(ViewController):
    def process(self):
        param = self.get_post(['problem_level', 'title', 'message'])
        problem = Problem()
        problem.problem_level = param['problem_level']
        problem.title = param['title']
        problem.message = param['message']
        problem.save()
        self.page_name = 'list.html' 
        return {'result':Problem.objects}
    
toyota.add_url_rule(app_name+'/login', view_func=LoginController.as_view('login'), methods=['post'])
toyota.add_url_rule(app_name+'/list', view_func=List.as_view('list'))
toyota.add_url_rule(app_name+'/save', view_func=Save.as_view('save'), methods=['post'])