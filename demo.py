from US_VISA.pipeline.training_pipeline import TrainPipeline
from US_VISA.exceptions import USVISAException
import sys

try:
    obj = TrainPipeline()
    obj.run_pipeline()
except USVISAException as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    print(f"Error: {e} occurred in script: {fname} at line: {line_number}")
    sys.exit(1)
