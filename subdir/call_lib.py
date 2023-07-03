# Databricks notebook source
import os
import sys
print("Before", os.path.abspath("."))
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
print("module path", module_path)
sys.path.append('.')

# COMMAND ----------

from lib import test_lib
test_lib()

# COMMAND ----------

import sys
sys.path.append('.')

# COMMAND ----------

# MAGIC %run ../mainnotebook

# COMMAND ----------

checkLibarary()

# COMMAND ----------


