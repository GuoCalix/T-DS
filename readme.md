# T&DS
T&DS is a vscode extension for you to test data and debug in your programming assignments or light projects.

## Test
- Test_single.py : For testing single data (\<name>.in and \<name>.out), and return the message.
- Test_batch.py : For testing a batch of data (<name[i]>.in and <name[i]>.out)
    - If there is no name.out for name.in, show NotFoundOut erro.
    - If there is no name.out for name.in, show NotFoundIn erro.
    - If the name.in and name.out is allright, return whether the test instance is working well. And the specific data path.

## Debug
- Recognize the language is using. (currently cpp or python).
- Connect to the vscode Debug API.
- Containing an instance of gdb, and connect gdb to vscode command console.
- Connect to Openai API (user setting) for AI assitance in debugging.


## OS
The OS part is for the API to vscode.
- command control
  - ```tnds -t [instance path] -s [datain path] ``` For test single data.
  - ```tnds -d [instance path] -s [datain path] ``` For debug single data.
  - ```tnds -t [instance path] -s [data directory path1] [data directory path2] ...``` For test a batch of data.
- setting_DNTS.json
  - self defined quick operation.
    - quick pack into compressed file and rename.
    - quick eliminate useless files (filter).
  - the virtual assistant's image.
  - your default programming language.
    - cpp (cl)
    - cpp (clang)  
    - cpp (g++)
    - python
- Your Openai account and sign in. 