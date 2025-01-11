from selene import by, be, browser
import allure


def test_name():
    with allure.step("Открываем github"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        browser.element('[class="search-input"]').click()
        browser.element('[id="query-builder-test"]').type('semaperm/qa_quru_task_10')
        browser.element('[id="query-builder-test"]').press_enter()

    with allure.step("Открываем репозиторий"):
        browser.element('a[href="/semaperm/qa_quru_task_10"]').click()

    with allure.step("Открываем вкладку Issues"):
        browser.element('#issues-tab').click()

    with allure.step("Проверяем наличие Issue содержащего homework в названии"):
        browser.element(by.partial_text('homework')).should(be.visible)

