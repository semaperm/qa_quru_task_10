import allure
from selene import browser, by, be


def test_github_issue_title():
    open_main_page()
    search_for_repository('semaperm/qa_quru_task_10')
    go_to_repository('semaperm/qa_quru_task_10')
    open_issue_tab()
    should_see_issue_with_text('homework')


@allure.step('Открываем главную страницу сайта GitHub')
def open_main_page():
    browser.open('https://github.com')



@allure.step('Ищем репозиторий {repository_name}')
def search_for_repository(repository_name):
    browser.element('[class="search-input"]').click()
    browser.element('[id="query-builder-test"]').type(repository_name)
    browser.element('[id="query-builder-test"]').press_enter()


@allure.step('Переходим на страницу репозитория')
def go_to_repository(repository_name):
    browser.element('a[href="/semaperm/qa_quru_task_10"]').click()


@allure.step('Открываем список доступных issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('В общем списке находим issue с названием {issue_title}')
def should_see_issue_with_text(issue_title):
    browser.element(by.partial_text('homework')).should(be.visible)