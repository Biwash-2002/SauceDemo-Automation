import os
import pytest

from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from config import STANDARD_USERNAME, STANDARD_PASSWORD


@pytest.fixture
def page(request):

    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("videos", exist_ok=True)
    os.makedirs("traces", exist_ok=True)

    with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=os.getenv("CI") == "true"
    )

        context = browser.new_context(
            record_video_dir="videos"
        )

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        page = context.new_page()

        yield page

        # Check whether test failed
        test_failed = (
            hasattr(request.node, "rep_call")
            and request.node.rep_call.failed
        )

        if test_failed:

            # Screenshot
            screenshot_path = (
                f"screenshots/{request.node.name}.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )

            # Trace
            trace_path = (
                f"traces/{request.node.name}.zip"
            )

            context.tracing.stop(
                path=trace_path
            )

        else:
            context.tracing.stop()

        context.close()
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        setattr(item, "rep_call", report)


@pytest.fixture
def logged_in_page(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        STANDARD_USERNAME,
        STANDARD_PASSWORD
    )

    return page