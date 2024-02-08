import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.debug('The debug message is displaying')  
# logging.info('The info message is displaying')  
# logging.error('The error message is displaying')  

marks = 120
logging.error(f"Invalid marks:{marks} Marks must be between 0 to 100")
subjects = ['Physics', 'Maths']
logging.warning(f"Number of subjects:{subjects} Should be at least three ")