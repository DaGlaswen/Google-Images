from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from valid_path import is_pathname_valid


def downloadGoogleImages(download_path, input_file, num_of_copies=1):

    driver = webdriver.Chrome(
        "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    )
    driver.get("https://www.google.com/")

    box = driver.find_element_by_xpath(
        "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
    )

    while not is_pathname_valid(download_path):
        download_path = input("Your download path is invalid, try again")

    def helper(query):

        driver.get("https://www.google.com/")

        box = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
        )
        box.send_keys(query)
        box.send_keys(Keys.ENTER)

        driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()

        for i in range(1, num_of_copies + 1):
            if i == 1:
                down_path_and_name = f"{download_path}\\{query}.png"
            else:
                down_path_and_name = "{download_path}{query}({i}).png".format()
            try:
                driver.find_element_by_xpath(
                    '//*[@id="islrg"]/div[1]/div[' + str(i) + "]/a[1]/div[1]/img"
                ).screenshot(down_path_and_name)
            except:
                print(f"{query} unsuccessful")
            finally:
                continue

    with open(input_file) as f:  # WORKS ONLY FOR TXT FILES
        for query in f:
            helper(query.strip())


if __name__ == "__main__":
    downloadGoogleImages(
        download_path=R".\tierlist",
        input_file="series i've watched.txt",
    )
