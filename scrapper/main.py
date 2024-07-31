import re
import time
import json
# import strconv  
import re._constants
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


    

def submit_answer(course_details, user_details):
    
    GOOGLE_SIGN_IN_BTN_ID = "GoogleExchange"
    GOOGLE_SIGN_IN_EMAIL_INPUT_CLASSNAME = "whsOnd.zHQkBf" 
    GOOGLE_SIGN_IN_PASSWORD_INPUT_CLASSNAME = "whsOnd.zHQkBf" 
    WEEK_LIKE_DIVS_CLASSNAME = "unit_navbar"

    # WEEK_ASSESSMENT_COMPLETED_IMG_CLASSNAME = "assessment_180"
    WEEK_ASSESSMENT_COMPLETED_IMG_CLASSNAME = "gcb-progress-icon.gcb-progress-icon-holder-completed"
    WEEK_ASSESSMENT_CLASSNAME = "gcb-left-activity-title-with-progress.gcb-nav-pa"
    
    answer_options_to_number = {
        "a":0,
        "b":1,
        "c":2,
        "d":3
    }

    options = Options()
    # options.add_argument('--headless=new')
    # options.add_argument('--disable-web-security')
    # options.add_argument('--allow-running-insecure-content')
    # options.add_argument('--no-sandbox')
    # options.add_argument("--enable-javascript")
    # options.add_argument("--user-data-dir=C:/Users/palas/AppData/Local/Google/Chrome/User Data/")
    # options.add_argument("--profile-directory=Profile 2")

    browser = webdriver.Firefox(service=Service(executable_path= "C:\\Users\\palas\\Desktop\\Projs\\NPTELNaiKarna\\scrapper\\geckodriver.exe"))
    # browser = webdriver.Chrome(service=Service(executable_path="chromedriver.exe"), options=options)
    actions = ActionChains(browser)
    
    # Login into Google Account through Stack Overflow
    # try:
    #     # stackurl = "https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27"
    #     stackurl = "https://stackoverflow.com/users/login"
    #     # stackurl = "https://accounts.google.com/v3/signin/identifier?opparams=%253Foperation%253Dregister&dsh=S1946584585%3A1722244837612202&access_type=online&client_id=216296035834-k1k6qe060s2tp2a2jam4ljdcms00sttg.apps.googleusercontent.com&ddm=0&nonce=73118b1c98321ff4eb0f7d7b957d21d15d823c07782e0a2f81ce4671ae5750e8&o2v=1&redirect_uri=https%3A%2F%2Fmedium.com%2Fm%2Fcallback%2Fgoogle&response_type=id_token+token&scope=email+openid+profile&service=lso&state=google-%7Chttps%3A%2F%2Fmedium.com%2F%3Fsource%3Dregister--------------------------lo_home_nav-----------%7Cregister&flowName=GeneralOAuthFlow&continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%2Fconsent%3Fauthuser%3Dunknown%26part%3DAJi8hAOcAuDatvDc_IOi1V_ZBVOGUDaWOOmWKsHHrtFaZaupFV9UIAaiIJUDv8ZpGtxgC4rXMrWPzCm2yZdN32qM9819jwx3cwQb07_9KhHTkUxgOHwoH1HUElmkexkIO5LFEQgvivgxF0BE7HLAl_u9bfw7dl3cwD6Xcdm-LB0gWEZMogQyvBcVrS-lPYhm1pl9JcufVbyJ6g7AUlgk0yAa4Im4dAH0-hiuntRxtDW-K8wTCaXL8UTeZFz5SbjFTf3ZqPzLjELgT1ShCIyxpteIhKRDZ_4rS4Ky-2QBE-z6zkFY_-WrYmKVGOVfgdklcATvQG8mYyddUR_mK2FDD5Q1pTPL655Gf_FyNW_9ubXq_vIb5lFwMk-cSWl3VpkzMWC2W7uUOLwAHBn_Iv7eWSirggHnBhhDGz6rZTZby-vDiLTTkovLTxHTx-kBqxHPT-hOfqyhG0qpWpMnddsXvWxwplMq6iNeJA%26flowName%3DGeneralOAuthFlow%26as%3DS1946584585%253A1722244837612202%26client_id%3D216296035834-k1k6qe060s2tp2a2jam4ljdcms00sttg.apps.googleusercontent.com%23&app_domain=https%3A%2F%2Fmedium.com&rart=ANgoxcfeVphfBO8M67RZdkkrw7VbLqNCgadq3JERHjGmTt93FrkRB909nhMVo9RwIsLJKSFZQSn8ycBfMdt9PVBM0vymvYAezYbr2eB6eyFzztpYi1F1d2o"
    #     # stackurl = "https://accounts.google.com/v3/signin/identifier?opparams=%253Foperation%253Dregister&dsh=S1946584585%3A1722244837612202&access_type=online&client_id=216296035834-k1k6qe060s2tp2a2jam4ljdcms00sttg.apps.googleusercontent.com&ddm=0&nonce=73118b1c98321ff4eb0f7d7b957d21d15d823c07782e0a2f81ce4671ae5750e8&o2v=1&redirect_uri=https%3A%2F%2Fmedium.com%2Fm%2Fcallback%2Fgoogle&response_type=id_token+token&scope=email+openid+profile&service=lso&state=google-%7Chttps%3A%2F%2Fmedium.com%2F%3Fsource%3Dregister--------------------------lo_home_nav-----------%7Cregister&flowName=GeneralOAuthFlow&continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%2Fconsent%3Fauthuser%3Dunknown%26part%3DAJi8hAOcAuDatvDc_IOi1V_ZBVOGUDaWOOmWKsHHrtFaZaupFV9UIAaiIJUDv8ZpGtxgC4rXMrWPzCm2yZdN32qM9819jwx3cwQb07_9KhHTkUxgOHwoH1HUElmkexkIO5LFEQgvivgxF0BE7HLAl_u9bfw7dl3cwD6Xcdm-LB0gWEZMogQyvBcVrS-lPYhm1pl9JcufVbyJ6g7AUlgk0yAa4Im4dAH0-hiuntRxtDW-K8wTCaXL8UTeZFz5SbjFTf3ZqPzLjELgT1ShCIyxpteIhKRDZ_4rS4Ky-2QBE-z6zkFY_-WrYmKVGOVfgdklcATvQG8mYyddUR_mK2FDD5Q1pTPL655Gf_FyNW_9ubXq_vIb5lFwMk-cSWl3VpkzMWC2W7uUOLwAHBn_Iv7eWSirggHnBhhDGz6rZTZby-vDiLTTkovLTxHTx-kBqxHPT-hOfqyhG0qpWpMnddsXvWxwplMq6iNeJA%26flowName%3DGeneralOAuthFlow%26as%3DS1946584585%253A1722244837612202%26client_id%3D216296035834-k1k6qe060s2tp2a2jam4ljdcms00sttg.apps.googleusercontent.com%23&app_domain=https%3A%2F%2Fmedium.com&rart=ANgoxcfeVphfBO8M67RZdkkrw7VbLqNCgadq3JERHjGmTt93FrkRB909nhMVo9RwIsLJKSFZQSn8ycBfMdt9PVBM0vymvYAezYbr2eB6eyFzztpYi1F1d2o"
    #     # browser.get('https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent'
    #     #        '.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2'
    #     #        '259%3A3%3Abbc%2C16%3A561fd7d2e94237c0%2C10%3A1599663155%2C16%3Af18105f2b08c3ae6%2C2f06af367387a967072e3124597eeb4e36c2eff92d3eef697'
    #     #        '1d95ddb5dea5225%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%'
    #     #        '2C%22k%22%3A%22Google%22%2C%22ses%22%3A%2226bafb488fcc494f92c896ee923849b6%22%7D&response_type=code&flowName=GeneralOAuthFlow')
        
    #     browser.get(stackurl)
    #     time.sleep(3)
        
    #     # cookie_btn = browser.find_elements(By.TAG_NAME, "button")[1]
    #     # cookie_btn.click()
    #     google_btn = browser.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div[2]/button[1]")
    #     google_btn.click()
    #     time.sleep(3)

    #     url = browser.title
    #     print(url)
    #     sign_in_email_input= browser.find_element(By.CLASS_NAME, GOOGLE_SIGN_IN_EMAIL_INPUT_CLASSNAME)
    #     sign_in_email_input.send_keys(user_details["email"])
    #     sign_in_email_input.send_keys(Keys.ENTER)
    #     time.sleep(3)
        
    # except Exception as e:
    #     print(e)
    #     browser.close()
    #     return




    # Login in NPTL
    browser.get(course_details['course_dashboard'])
    time.sleep(10)
    try:
        sign_in_btn = browser.find_element(By.ID, GOOGLE_SIGN_IN_BTN_ID)
        actions.move_to_element(sign_in_btn).perform()
        actions.click(sign_in_btn).perform()
        time.sleep(10)

        sign_in_email_input = browser.find_element(By.CLASS_NAME, GOOGLE_SIGN_IN_EMAIL_INPUT_CLASSNAME)
        sign_in_email_input.send_keys(user_details["email"])
        sign_in_email_input.send_keys(Keys.ENTER)
        time.sleep(10)

        sign_in_email_input = browser.find_element(By.CLASS_NAME, GOOGLE_SIGN_IN_PASSWORD_INPUT_CLASSNAME)
        sign_in_email_input.send_keys(user_details["password"])
        sign_in_email_input.send_keys(Keys.ENTER)
        time.sleep(30)
        # lol = input("Done?")

        # weeks_parent_div = browser.find_element(By.XPATH, "/html/body/div[11]/div[1]/div/div[2]/div[1]/div[3]/div")
        all_week_like_divs = browser.find_elements(By.CLASS_NAME, WEEK_LIKE_DIVS_CLASSNAME)
        weeks_div = []
        quiz_not_done = []
        # assessment_links

        # Remove THis Latter
        week0 = "/html/body/div[11]/div[1]/div/div[2]/div[1]/div[3]/div/" + "div[3]" + "/ul/li/div"
        week1 = "/html/body/div[11]/div[1]/div/div[2]/div[1]/div[3]/div/" + "div[4]" + "/ul/li[8]/div"
        week2 = "/html/body/div[11]/div[1]/div/div[2]/div[1]/div[3]/div/" + "div[5]" + "/ul/li[7]/div"        
        
        # weeks_divs_count = 2

        # Week _ : Starts from div[3]
        itr = 3
        # Last 2 Divs are Text Transcripts and Books
        while(itr < len(all_week_like_divs) - 3):
            all_week_like_divs[itr].click()
            scroll_origin = ScrollOrigin.from_element(all_week_like_divs[itr], 100)
            actions.scroll_from_origin(scroll_origin, 0, 100).perform()
            time.sleep(3)
            try:
                INSIDE_WEEK_CLASS_NO = "gcb-left-activity-title-with-progress.gcb-nav-pa"
                lecture_and_quiz = all_week_like_divs[itr].find_elements(By.CLASS_NAME, INSIDE_WEEK_CLASS_NO)
                
                # Check If Last Element is the Quiz
                last_element = lecture_and_quiz[-1]
                last_element_text_withweekno = last_element.find_element(By.TAG_NAME, "a").text
                last_element_text = last_element_text_withweekno.split(" ")[0]
                if  last_element_text == "Quiz:":
                    try:
                        icon = last_element.find_element(By.TAG_NAME, "div").find_element(By.CLASS_NAME, WEEK_ASSESSMENT_COMPLETED_IMG_CLASSNAME)
                        print(f"Done: {last_element_text}")
                    except:
                        quiz_not_done.append(f"{last_element_text_withweekno}")

            except Exception as e:
                print(e)

            itr += 1
        print(quiz_not_done)
        
        answered_weeks = course_details['answers'].keys()
        formatted_quiz_not_done = ["week" + str(x[-1]) for x in quiz_not_done]
        for quiz in formatted_quiz_not_done:
            if quiz in answered_weeks:
                browser.get(course_details['week_assessment_template'] + quiz.replace("week", ""))
                time.sleep(5)
                # heading = browser.find_element(By.XPATH, "/html/body/div[11]/div[1]/div/div[2]/div[4]/div[2]/div[1]/h1")
                QUESTION_CLASSNAME = "qt-mc-question.qt-embedded"
                OPTIONS_CLASSNAME = "gcb-mcq-choice"
                OTIONS_DIV_CLASSNAME = "qt-choices"
                all_questions_divs = browser.find_elements(By.CLASS_NAME, QUESTION_CLASSNAME)
                for itr, question in enumerate(all_questions_divs):      
                    try:          
                        options_div = question.find_element(By.CLASS_NAME, OTIONS_DIV_CLASSNAME).find_elements(By.CLASS_NAME, OPTIONS_CLASSNAME)
                    # Check if input Type is : 1. radio  2. checkbox  3. text(not)
                        option_input = options_div[0].find_element(By.TAG_NAME, "input")
                        input_attribute = option_input.get_attribute("type")
                        # print(f"Type = {input_attribute}")
                        if  input_attribute == "radio":
                            # print(f"KEY: {quiz}")
                            weeks_answers = course_details["answers"][quiz]
                            # print(weeks_answers)
                            ans = answer_options_to_number[weeks_answers[str(itr)]]
                            input_option = options_div[ans]
                            print(f"ans: {ans} | input_option : {input_option}")
                            input_option.find_element(By.TAG_NAME, "input").click()
                            scroll_origin = ScrollOrigin.from_element(question, 100)
                            actions.scroll_from_origin(scroll_origin, 0, 1000).perform()
                        else :
                            print(input_attribute)
                    except Exception as e:
                        print(e)
                        


    except Exception as e:
        print(e)
        browser.close()



def submit_all_course_answers():
    file = open('../answers.json', 'r') 
    ans_content = json.load(file)
    file.close()

    file = open('../config.json', 'r')
    config_content = json.load(file)
    file.close()


    for course in list(ans_content.keys()):
        for user in config_content['users']:
            submit_answer(ans_content[course], user)




submit_all_course_answers()


