# Проект по тестированию API для тестового API LearnQA API
> <a target="_blank" href="https://playground.learnqa.ru/api/map">Swagger тестового API</a>
<img width="1200" src="source/swagger.png">

## Используемый стек технологий и инструментов
|                        Python                         |                          Pytest                          |                       Requests                        |                        Git                         |                        Jenkins                         |                        Allure                         |                        Allure TestOps                         |                         Telegram                         |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| <img width="55" height="55" src="source/python.svg"/> | <img width="55" height="55" src="source/requests.webp"/> | <img width="55" height="55" src="source/pytest.svg"/> | <img width="55" height="55" src="source/git.svg"/> | <img width="55" height="55" src="source/jenkins.svg"/> | <img width="55" height="55" src="source/allure.svg"/> | <img width="40" height="40" src="source/allure-testops.png"/> | <img width="40" height="40" src="source/telegram.svg"/>  |

## Tесты
<ul style="list-style-type: '\2705 &#160'">
    <li>Create user with unique email</li>
    <li>Create user with already used email</li>
    <li>Authorization</li>
    <li>Get user info with authorization by same user</li>
    <li>Get user info with authorization by another user</li>
    <li>Modify user data with authorization by same user</li>
    <li>Modify user data with authorization by another user</li>
    <li>Delete user with authorization by same user</li>
    <li>Delete user with authorization by another user</li>
</ul>

## <img width="3%" title="Jenkins" src="source/jenkins.svg"> Запуск проекта в Jenkins
#### Для запуска автотестов в Jenkins
1. __Открыть проект <a href="https://jenkins.autotests.cloud/job/c16-api_tests_learn_qa/">в Jenkins</a>__
2. __Нажать кнопку `Build`__
3. __Результат запуска сборки можно посмотреть в отчете Allure__

## <img width="3%" title="Allure report"  src="source/allure.svg"> Отчет в Allure report
>__Просмотр результатов выполнения тестов в Allure report__
<img width="1200" src="source/allure_report_overview.png">

>__Отчет позволяет получить общую информацию о прохождении тестов__
<img width="1200" src="source/allure_report_suites_all.png">

>__Отчет позволяет получить информацию о прохождении каждого теста__
>__Каждый тесто содержит детальную информацию по всем шагам тестов, включая подробное логирование всех запросов:__
<img width="1200" src="source/allure_report_suites_one_test.png">

## <img width="3%" title="Telegram"  src="source/telegram.svg"> Оповещения в Telegram
>__После выполнения тестов, в Telegram bot приходит сообщение с графиком и информацией о тестовом прогоне.<br>__
> <img width="120" src="source/tg_report.png">
