**Problem Statement**:
To ingest and transform a set of images using PySpark.
The transformations performed are rotation and resize and are applied to all the images in the directory.

**Requirements**:

The script is dependent on the following python packages:
-   PySpark
-   PIL (Python Imaging Library)
-   StringIO
-   os
    
For installing PySpark refer to the following link:
-   [https://www.tutorialspoint.com/pyspark/pyspark_environment_setup.htm](https://www.tutorialspoint.com/pyspark/pyspark_environment_setup.htm)
For installing the remaining dependencies, run the following command from the inside the project root directory:
-   `pip install -r requirements.txt`

**Usage**:
The script can be invoked and executed as a command which is as follows:

-   `spark-submit transform_images.py`
    
Please make sure that the directory containing the spark-submit job is added to the path else provide the absolute path to the spark-submit binary.

**Resources**:
The test images can be found at:
- -   [http://btsd.ethz.ch/shareddata/](http://btsd.ethz.ch/shareddata/)
