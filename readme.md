# T&DS
T&DS is a vscode extension for you to test data and debug in your programming assignments or light projects.

## Test
- Test_single.py : For test single data (\<name>.in and \<name>.out).
- Test_batch.py : For test a batch of data (<name[i]>.in and <name[i]>.out)
    - If there is no name.out for name.in, show NotFoundOut erro.
    - If there is no name.out for name.in, show NotFoundIn erro.
    - If the name.in and name.out is allright, return whether the test instance is working well. And the specific data path.

## Debug
- Recognize the language is using. (currently cpp or python).
- Connect to the vscode Debug API.


## OS
The OS part is for the API to vscode.
- command control
  - ```tnds -t [instance path] -s [datain path] ``` For test single data.
  - ```tnds -d [instance path] -s [datain path] ``` For debug single data.
  - ```tnds -t [instance path] -s [data directory path1] [data directory path2] ...``` For test a batch of data.
