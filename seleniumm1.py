from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_google_search():
    try:

        driver = webdriver.Chrome()


        driver.get("https://www.google.ru/")


        search_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )


        search_field.send_keys("TUSUR")


        search_field.submit()


        result_page = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".g"))
        )


        assert len(result_page) > 0, "Ошибка! Результаты поиска отсутствуют."

        print("Тест успешно завершён.")

    except Exception as e:
        print(f"Ошибка при выполнении теста: {e}")

    finally:

        driver.quit()


if __name__ == "__main__":
    test_google_search()