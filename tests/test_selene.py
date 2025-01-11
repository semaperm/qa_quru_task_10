from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_github():
    browser.open("https://github.com")

    browser.element('[class="search-input"]').click()
    browser.element('[id="query-builder-test"]').type('semaperm/qa_quru_task_10')
    browser.element('[id="query-builder-test"]').press_enter()

    browser.element('a[href="/semaperm/qa_quru_task_10"]').click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('homework')).should(be.visible)