from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import os
import re

#download preferences
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "C:\Clips\LeagueOfLegends"}     #downloaded file location
chromeOptions.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe",  options=chromeOptions)
chromeOptions = webdriver.ChromeOptions()
driver.set_window_size(1024, 600)
driver.maximize_window()

m = 1       #variable to manage first time use statements


#load site and check language
i = 1
while i < 5:

    k = 0
    while k < 1:

        try:
            #load site
            driver.get("https://www.twitch.tv/directory/game/League%20of%20Legends/clips?range=24hr")     #link of clips for game or streamer
            driver.implicitly_wait(5)
            #if m == 1:
            #    #set language
            #    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div/div/div/div[4]/div[2]/div[1]/div[1]/div/div/div[1]/button").click()
            #    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/main/div[2]/div[3]/div/div/div/div/div/div[4]/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[3]/div/div/div[1]/div").click()

        except NoSuchElementException:
            k = 0
            print("Could not load ")
            print(driver.title)

        else:
            k = k + 1
            print("Could load ")
            print(driver.title)


    #click on clip
    clip = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div/main/div[2]/div[3]/div/div/div/div/div/div[5]/div[1]/div/div/div/div[" + str(i) + "]/article/div[1]/div/div[1]/div[1]/div/a")
    link = clip.get_attribute("href")       #clip link
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


    #go to clipper website
    driver.get("https://scloudtomp3downloader.com/twitch-clip-downloader?lang=en")
    down = driver.find_element_by_xpath("//*[@id='url']")        #input bar
    down.send_keys(link)
    print("Input the link")
    driver.find_element_by_xpath("//*[@id='send']").click()      #download button
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]/a[3]").click()        #version button


    # changing the file name and waiting for clip to download
    j = 0
    while j < 1 :
        try:
            time.sleep(10)
            os.rename(r'C:\Clips\LeagueOfLegends\twitch-video-clip-from-'+ (streamer[0].replace("_", "-")).replace(".", "-") + r'-scloudtomp3downloader.com.mp4', r'C:\Clips\LeagueOfLegends\Temp.mp4')
            #twitch-video-clip-from-riotgames-scloudtomp3downloader.com.mp4

        except FileNotFoundError:
            j = 0
            print("Could not downlaod: ")
            print(clip_title)

        else:
            j = j + 1
            print("Could downlaod: ")
            print(clip_title)
            #driver.quit()


    #split message into usable string
    tube_title = clip_title.split("•")
    vid_title = tube_title[0]
    clipper = tube_title[1]
    splitat = vid_title.find('League of Legends')
    title = vid_title[:splitat]
    game = vid_title[splitat:]
    print("Title is: ")
    print(title)
    title = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", title)
    print("\n Game is: ")
    print(game)




    #load site
    driver.get("https://www.youtube.com/account")
    driver.implicitly_wait(5)


    if m == 1 :
        #log in details needed for first time only
        name = driver.find_element_by_xpath("//*[@id='identifierId']")
        name.send_keys(" ")
        driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
        pas = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
        pas.send_keys(" ")
        driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/div[2]").click()
        print(driver.title)
        m = m + 1


    l = 0
    while l < 1 :
        try:
            # switch to channel
            driver.find_element_by_xpath("//*[@id='options']/ytd-channel-options-renderer/yt-formatted-string[2]/a").click()
            print("1")
            time.sleep(3)
            driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-switcher-page-renderer/div[2]/ytd-account-item-renderer[2]/tp-yt-paper-icon-item/tp-yt-paper-item-body/yt-formatted-string[1]").click()
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
    os.system(r"C:\AutoIT\UploadFileLeagueOfLegends.exe")
    time.sleep(10)


    #video details
    temp_title = driver.find_element_by_xpath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-mention-textbox/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div")
    temp_title.clear()
    temp_title.send_keys(title)     #enter title
    des = driver.find_element_by_xpath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-mention-textbox/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div")
    des.send_keys(title + " - " + game + "  by @" + streamer[0])        #enter description
    des.send_keys("\n" + clipper + " from https://www.twitch.tv/" + game)
    des.send_keys(" \n This action was performed by a bot. ")
    driver.find_element_by_xpath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/div/ytcp-button").click()
    tags = driver.find_element_by_xpath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[2]/ytcp-form-input-container/div[1]/div[2]/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input")
    #custom_tags = "lol, "
    time.sleep(3)
    tags.send_keys(title + ", " + game + ", " + streamer[0] + ", " + streamer[1] + ", " + "clips, " + "epic, " + "lol, " + "gamermoment, ")        #tags
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
    os.rename(r'C:\Clips\LeagueOfLegends\Temp.mp4', r'C:\Clips\LeagueOfLegends\Clip- ' + title + r'.mp4')

    i += 1
