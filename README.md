# Genie CLI Application

Genie is a CLI application that answers questions related to the Linux Bash terminal.

## Setup Instructions


### Steps

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/MAMDOUHjr/genie
    cd genie
    ```

2. Get your API key from Google Cloud Platform and replace `YOUR_API_KEY` in the script with your actual API key.

3. Run the script:
    ```bash
    python genie.py
    ```

### Creating an Alias

To make it easier to run the Genie script, you can create an alias in your `.bashrc` file.

1. Open your `.bashrc` file in a text editor:
    ```bash
    nano ~/.bashrc
    ```

2. Add the following line to create an alias named `genie`:
    ```bash
    alias genie='python3 /path/to/genie.py'
    ```

    Replace `/path/to/your-repo-name` with the actual path to the cloned repository.

3. Save and close the file. If you're using `nano`, you can do this by pressing `CTRL + X`, then `Y`, and then `ENTER`.

4. Reload the `.bashrc` file to apply the changes:
    ```bash
    source ~/.bashrc
    ```    

### Usage
- Type your Linux Bash terminal question after the `>>>` prompt.
- Type `exit` to quit the application.

## Example

```sh
$ genie
hello from genie how can i help u in commands
>>> How do I list all files in a directory?
Q :  How do I list all files in a directory?
Loading ....
Use the `ls` command to list all files in a directory.
>>> exit
