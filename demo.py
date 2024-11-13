from US_VISA.pipeline.training_pipeline import TrainPipeline
from US_VISA.exceptions import USVISAException
import sys

try:
    obj = TrainPipeline()
    obj.run_pipeline()
except USVISAException as e:
    print(f"Error: {e}")
    sys.exit(1)
