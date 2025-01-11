import allure
from selene import browser, by, be



@allure.step("Открытие браузера и переход на github.com")
def open_browser():
    browser.open("https://github.com")


@allure.step("Поиск репозитория semaperm/qa_quru_task_10")
def searching_repository():
    browser.element('[class="search-input"]').click()
    browser.element('[id="query-builder-test"]').type('semaperm/qa_quru_task_10')
    browser.element('[id="query-builder-test"]').press_enter()


@allure.step("Открытие репозитория semaperm/qa_quru_task_10")
def open_repository():
    browser.element('a[href="/semaperm/qa_quru_task_10"]').click()


@allure.step("Открытие вкладки Issues")
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step("Проверка наличия Issue с 'homework' в названии")
def check_homework_issue():
    browser.element(by.partial_text('homework')).should(be.visible)