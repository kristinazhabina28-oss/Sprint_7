# Sprint_7

API tests for the Yandex Scooter training service.

## Run tests

```bash
pip install -r requirements.txt
pytest --alluredir=allure_results
```

## Generate Allure report

```bash
allure generate allure_results -o allure_report --clean
```

