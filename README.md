# This testing use python 3.8.10

## For the start run package manager install:
pip install -r requirements.txt

## For generate reports execute next steps:
### install Java
sudo apt update
sudo apt install default-jre -y
sudo apt install default-jdk -y
javac -version

### install allure
mkdir allure
cd allure
wget https://github.com/allure-framework/allure2/releases/download/2.13.8/allure-2.13.8.zip

sudo apt install unzip -y
unzip allure-2.13.8.zip

## Use this command for run tests:
python3 -m pytest --driver Chrome --driver-path ./drivers/chromedriver --alluredir=./allure/report

## Use for generate allure report:
./allure/allure-2.13.8/bin/allure serve allure/report
