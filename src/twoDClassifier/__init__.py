'''
Custom logger module for 2DClassifier project
'''
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# Creating log directory & file
log_dir = "logs"
log_filepath = os.path.join(log_dir,"run_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), #save
        logging.StreamHandler(sys.stdout) #print
    ]
)

logger = logging.getLogger("2DClassifierLogger")