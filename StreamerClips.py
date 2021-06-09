from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import os
import re

game = "Minecraft"
my_path = "C:\Clips\MCC2.1Streamers"

#download preferences
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : my_path}     #downloaded file location
chromeOptions.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe",  options=chromeOptions)
chromeOptions = webdriver.ChromeOptions()
driver.set_window_size(1024, 600)
driver.maximize_window()

players_list = ["HBomb94", "tommyinnit"]

m = 1       #variable to manage first time use statements

#load site and check language
x = 0
while x < len(players_list):
    i = 2
    print(players_list[x])
    print(x)
    while i < 7:
        k = 0
        while k < 1:

            try:
                #load site
                driver.get("https://www.twitch.tv/" + players_list[x] + "/clips?filter=clips&range=24hr")     #link of clips for game or streamer
                driver.implicitly_wait(5)

                #if m == 1:
                #    #set language
                #    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div/div/div/div[4]/div[2]/div[1]/div[1]/div/div/div[1]/button").click()
                #    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div/div/div/div[4]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[3]/div/div/div[1]/div").click()
                #    m = m + 1

            except NoSuchElementException:
                k = 0
                print("Could not load ")
                print(driver.title)

            else:
                k = k + 1
                print("Could load ")
                print(driver.title)


        #click on clip
        clip = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[" + str(i) + "]/article/div[1]/div/div[1]/div[1]/div/a")
        link = clip.get_attribute("href")      #clip link
        clip.click()
        streamer = driver.title
        streamer = streamer.split(" ", 1)
        print("Got the clip and split it. Streamer is: ")
        print(streamer[0])

        #get the title
        time.sleep(5)
        message = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/div[1]")
        time.sleep(5)
        clip_title = message.get_attribute("textContent")
        print("Got the title, game and clipper: ")
        print(clip_title)
        driver.implicitly_wait(5)

        arr = os.listdir(my_path)
        num = len(arr)
        print(arr)
        print(num)

        #go to clipper website
        driver.get("https://clipsey.com/")
        down = driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/div[1]/div/div[1]/input")        #input bar
        down.send_keys(link)
        print("Input the link")
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/div[1]/div/div[1]/button").click()      #download button
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/a").click()        #version button

        print(arr)
        print(num)

        # changing the file name and waiting for clip to download
        arr = os.listdir(my_path)
        j = 0
        while j < 1:
            try:
                arr = os.listdir(my_path)
                l = len(arr)
                str = arr[0]
                first = str[0]
                if(first < "c"):
                    os.rename('C:/Clips/MCC2.1Streamers/' + arr[0], 'C:/Clips/MCC2.1Streamers/Temp.mp4')
                    print("Could download")
                elif(first > "c"):
                    os.rename('C:/Clips/MCC2.1Streamers/' + arr[l-1], 'C:/Clips/MCC2.1Streamers/Temp.mp4')
                    print("Could download")
                j = 1
            except PermissionError and IndexError:
                print("Could not download")
                time.sleep(10)
                j = 0


        #split message into usable string
        tube_title = clip_title.split("•")
        vid_title = tube_title[0]
        clipper = tube_title[1]
        splitat = vid_title.find('Minecraft')
        title = vid_title[:splitat]
        game = vid_title[splitat:]
        print("Title is: ")
        print(title)
        print("\n Game is: ")
        print(game)




        #load site
        driver.get("https://www.youtube.com/account")
        driver.implicitly_wait(5)


        if m == 1 :
            #log in details needed for first time only
            name = driver.find_element_by_xpath("//*[@id='identifierId']")
            name.send_keys("clipbot1509@gmail.com")
            driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/span").click()
            pas = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
            pas.send_keys("qwe123r4@clipbot1509")
            driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/span").click()
            print(driver.title)
            m = m + 1


        l = 0
        while l < 1 :
            try:
                # switch to channel
                driver.find_element_by_xpath("//*[@id='options']/ytd-channel-options-renderer/yt-formatted-string[2]/a").click()
                print("1")
                time.sleep(3)
                driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-switcher-page-renderer/div[2]/ytd-account-item-renderer[3]/tp-yt-paper-icon-item/tp-yt-paper-item-body").click()
                print("2")
                time.sleep(7)

                # navigate to upload part
                driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button").click()
                print("3")
                time.sleep(3)
                driver.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item/div[1]/yt-icon").click()
                print("4")
                time.sleep(3)
            except NoSuchElementException:
                l = 0
            else:
                l = l + 1

        # upload time
        driver.find_element_by_xpath("//*[@id='select-files-button']/div").click()
        os.system(r"C:\AutoIT\UploadFileMCC2.1Streamers.exe")
        time.sleep(10)


        #video details
        temp_title = driver.find_element_by_xpath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-mention-textbox/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div")
        temp_title.clear()
        temp_title.send_keys(title)     #enter title
        driver.find_element_by_xpath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytcp-form-audience/ytcp-audience-picker/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]/div[2]/ytcp-ve").click()      #not safe for kids
        des = driver.find_element_by_xpath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-mention-textbox/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div")
        des.send_keys(title + " - " + game + "  by @" + streamer[0])        #enter description
        des.send_keys("\n" + clipper + " from https://www.twitch.tv/" + game)
        des.send_keys(" \n This action was performed by a bot. ")
        driver.find_element_by_xpath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/div/ytcp-button").click()
        tags = driver.find_element_by_xpath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[2]/ytcp-form-input-container/div[1]/div[2]/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input")
        #custom_tags = "lol, "
        time.sleep(3)
        tags_in = title + ", " + game + ", " + streamer[0] + ", " + streamer[1].replace("- ", "") + ", " + "clips, " + "epic, " + "lol, " + "gamermoment, "
        tags.send_keys(re.sub(r"[-()\"#/@;:<>{}`+=~|.!?]", "", tags_in))  # tags
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[7]/div[3]/ytcp-form-select/ytcp-select/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger/div/div[2]").click()        #category
        driver.find_element_by_xpath("/html/body/ytcp-text-menu/tp-yt-paper-dialog/tp-yt-paper-listbox/tp-yt-paper-item[7]/ytcp-ve/div").click()        #select category
        time.sleep(3)
        #driver.find_element_by_xpath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytcp-form-audience/ytcp-audience-picker/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]/div[1]/div[1]").click()

        driver.find_element_by_xpath("//*[@id='next-button']/div").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='next-button']/div").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='next-button']/div").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]/div[1]/div[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]").click()
        time.sleep(5)


        #rename the video
        os.rename(r'C:\Clips\MCC2.1Streamers\Temp.mp4', r'C:\Clips\MCC2.1Streamers\clip- ' + title.replace("?", "") + r'.mp4')

        i += 1

    x = x + 1
