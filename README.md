# python-selenium-chromium-on-lambda
Run selenium scripts in python with chromium on aws lambdas on **easy way** using docker custom images.

## Requirements

- Docker
- [AWS SAM CLI](https://aws.amazon.com/serverless/sam/) with configured API credentials

## Usage

1) Clone this repo and change current dir
    ```bash
    git clone https://github.com/wesleywilian/python-selenium-chromium-on-lambda.git
    cd python-selenium-chromium-on-lambda
    ```
2) Open https://console.aws.amazon.com/ecr/create-repository then select your region.
3) Create the repository
4) Copy the repository URI
5) On this project root run **sam build**

    Expected output:

    ```
    Build Succeeded

    Built Artifacts  : .aws-sam/build
    Built Template   : .aws-sam/build/template.yaml

    Commands you can use next
    =========================
    [*] Invoke Function: sam local invoke
    [*] Deploy: sam deploy --guided
    ```
6) Run **sam deploy --guided** and fill in the fields with values of your choice. 

    On **Image Repository** field paste your repository URI.

    ```
    $ sam deploy --guided

    Configuring SAM deploy
    ======================

            Looking for config file [samconfig.toml] :  Not found

            Setting default arguments for 'sam deploy'
            =========================================
            Stack Name [sam-app]: stack-name-here
            AWS Region [us-east-1]: us-east-2
            Image Repository for PythonSeleniumChromiumOnLambdaFunction: **repo uri here**
            pythonseleniumchromiumonlambdafunction:python3.8-v1 to be pushed to xxxx.dkr.ecr.xxxx.amazonaws.com/xxxx:pythonseleniumchromiumonlambdafunction-xxxx-python3.8-v1

            #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
            Confirm changes before deploy [y/N]: 
            #SAM needs permission to be able to create roles to connect to the resources in your template
            Allow SAM CLI IAM role creation [Y/n]: 
            Save arguments to configuration file [Y/n]: 
            SAM configuration file [samconfig.toml]: 
            SAM configuration environment [default]: 
    ```

7) All done, you can now run selenium scripts in lambda (you can customize **app/app.py**). Also you can invoke locally with **sam local invoke**

    ```
    $ sam local invoke

    Invoking Container created from pythonseleniumchromiumonlambdafunction:python3.8-v1
    Building image.................
    Skip pulling image and use local one: pythonseleniumchromiumonlambdafunction:rapid-1.25.0.

    START RequestId: 7eb75e8a-4210-4a8a-8c93-730d958d9ac0 Version: $LATEST
    [INFO]  2021-08-28T19:18:47.998Z        7eb75e8a-4210-4a8a-8c93-730d958d9ac0    python-selenium-chromium-on-lambda started
    [INFO]  2021-08-28T19:18:49.203Z        7eb75e8a-4210-4a8a-8c93-730d958d9ac0    opening google...
    [INFO]  2021-08-28T19:18:50.391Z        7eb75e8a-4210-4a8a-8c93-730d958d9ac0    taking screenshot screenshot_google.png...
    [INFO]  2021-08-28T19:18:50.566Z        7eb75e8a-4210-4a8a-8c93-730d958d9ac0    screenshot location: /var/task/screenshot_google.png
    END RequestId: 7eb75e8a-4210-4a8a-8c93-730d958d9ac0
    REPORT RequestId: 7eb75e8a-4210-4a8a-8c93-730d958d9ac0  Init Duration: 0.13 ms  Duration: 2932.37 ms    Billed Duration: 3000 ms        Memory Size: 2048 MB    Max Memory Used: 2048 MB
    null
    ```

## Components versions

- Selenium: 3.141.0 (app/requirements.txt)
- Chromium: 92.0.4515.0 (app/Dockerfile)
- Chromedriver: 92.0.4515.107 (app/Dockerfile)
