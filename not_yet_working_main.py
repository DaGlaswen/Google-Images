from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import click
import os.path

from valid_path import is_pathname_valid


def downloadGoogleImages(download_path=None, input_file=None, num_of_copies=1):
    driver = webdriver.Chrome(
        "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    )
    if download_path is None:
        download_path = input(
            "Please enter the download_path (the path where the image will be saved at): "
        )
        while not is_pathname_valid(download_path):
            download_path = input("Try again")

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
                down_path_and_name = "{download_path}{line}.png".format()
            else:
                down_path_and_name = "{download_path}{line}{i}.png".format()
            driver.find_element_by_xpath(
                '//*[@id="islrg"]/div[1]/div[' + str(i) + "]/a[1]/div[1]/img"
            ).screenshot(down_path_and_name)

    if not input_file:
        try:
            if click.confirm(
                input(
                    "Do you want to enter the input file path (input file - file where all the queries will be read from (only txt))? "
                )
            ):
                input_file = input("Please enter an input txt file ")
                while not os.path.exists(input_file):
                    input_file = input("try again ")

            else:
                helper(input("enter the query: "))
        except:
            print("Unexpected error, try again")
    else:
        with open(input_file) as f:  # WORKS ONLY FOR TXT FILES
            for query in f:
                helper(query)


if __name__ == "__main__":
    downloadGoogleImages(
        download_path=R"C:\Users\miste\Pictures\Saved Pictures\tierlist",
        input_file="series i've watched.txt",
    )
