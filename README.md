# calls-quality-measures

### A python tool which puts Rainbow log's quality indicators fields' values into a csv file

### Check wether Python is installed
If Python isn't installed on your computer, please download it from this link :
[Download page](https://www.python.org/downloads/)

### How to run it ?

#### On Windows :

##### 1. Open the Windows default terminal

##### 2. Run the first python program which will download a Rainbow log :
```shell
py download_log.py <mail_account> <password_account>
```

##### 3. Run the second python program which will display the metrics from the downloaded Rainbow log :
```shell
py get_quality_values_rainbow_log.py
```

##### 4. Finished !
Either a "stats.csv" file will be created or a Pandas DataFrame will be displayed into the terminal.
