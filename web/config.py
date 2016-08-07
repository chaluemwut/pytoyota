import os
class Config:
#     production
    db_name='toyota'
    db_host=os.environ['DB_1_PORT_27017_TCP_ADDR']
    db_port='27017'
    base_path_file = '/datafile'    

# dev
#     db_name = 'fbfilter'
#     db_host = 'localhost'
#     db_port = '27017'
#     base_path_file = '/Users/chaluemwutnoyunsan/development/data/filter/post_img'   