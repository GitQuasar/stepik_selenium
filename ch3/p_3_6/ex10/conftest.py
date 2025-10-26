import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="ru",
        help="Choose language: ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb",
    )


@pytest.fixture(scope="function")
def browser(request):
    languages = (
        "ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb "
    )
    language = request.config.getoption("language")
    if (language + " ") in languages:
        print("\nStart chrome browser for test...")
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": language})
        browser = webdriver.Chrome(options=options)
    else:
        print(
            "\nlanguage {} not supported :(\ntry: ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb".format(
                language
            )
        )
        pytest.fail("Wrong Language")
    yield browser
    print("\nQuitting browser...")
    browser.quit()
