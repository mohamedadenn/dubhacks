import os
import image
#import cv2
import numpy as np
import io, os
from numpy import random
from PIL import Image
import io, os
from numpy import random
import pandas as pd
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"abc.json"
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
from pytrends.request import TrendReq
import pytrends
import time
from sklearn import preprocessing
import statistics
parent_dir = "C:\covid-copy2\static"

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'bmp'}
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template("dashboard.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/inputform", methods=["GET", "POST"])
def input_symptoms():
    paths=[]
    if request.method == 'POST':
        instausername = str(request.form['instausername'])
        instapassword = str(request.form['instapassword'])
        duration = str(request.form['duration'])
    def input1():
        if request.method == 'POST':
                

            instausername = str(request.form['instausername'])
            instapassword = str(request.form['instapassword'])
            duration = str(request.form['duration'])


            directory = f"{instausername}"
            parent_dir = "C:\covid-copy2\static"
            
            path = os.path.join(parent_dir, directory) 
            
            # Create the directory 
            # 'GeeksForGeeks' in 
            # '/home / User / Documents' 
            try:
                os.mkdir(path) 
            except:
                print("sdf")
            files = request.files.getlist('files[]')
            file_names = []
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_names.append(filename)
                    file.save(os.path.join("static",f"{instausername}",filename))
                    paths.append(os.path.join(f"{instausername}",filename))
            
            return paths
            #else:
            #	flash('Allowed image types are -> png, jpg, jpeg, gif')
            #	return redirect(request.url)

    
    

    def google_predict(path):
        from google.cloud import vision
        from pillow_utility import draw_borders, Image
        import pandas as pd

        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"abc.json"
        client = vision.ImageAnnotatorClient()

        file_name = path
        image_path = os.path.join('', file_name)

        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.object_localization(image=image)
        localized_object_annotations = response.localized_object_annotations

        pillow_image = Image.open(image_path)
        df = pd.DataFrame(columns=['name', 'score'])
        for obj in localized_object_annotations:
            df = df.append(
                dict(
                    name=obj.name,
                    score=obj.score
                ),
                ignore_index=True)
        return df


    def pop(lists):
        from pytrends.request import TrendReq
        

        # Create pytrends object, request data from Google Trends
        pytrends = TrendReq(hl='en-US', tz=360)

        # Extracts data based on our keywords
        kw_list=lists
        pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

        # Specify, get, and normalize data
        data = pytrends.interest_over_time()
        data.drop('isPartial', axis=1, inplace=True)
        normData = data.apply(lambda x: x / x.max(), axis=0)

        # Max normalized value from most recent date + index in list
        recent = normData.values[-1].tolist()
        max_value = max(recent)
        max_index = recent.index(max_value)

        # Name of most popular normalized item
        out = kw_list[max_index]
        pytrends.build_payload(kw_list=[out], cat=0, timeframe='today 5-y', geo='', gprop='')
        trend = pytrends.related_queries()
        trend_list = trend[out]['top']['query']

        # Adds variable number of hashtags to topList
        numHashtags = 5
        topList = []
        for i in range(numHashtags):
            topList.append(trend_list[i])

        # TopList is a list of hashtags, out is most popular item
        
        poplist=topList

        import pandas as pd                        
        from pytrends.request import TrendReq
        import pytrends
        from pytrends.request import TrendReq
        import pandas as pd
        import time
        import datetime
        import matplotlib.pyplot as plt
        import seaborn as sns
        from datetime import datetime, date, time
        pytrend = TrendReq()
        pytrend = TrendReq()
        pytrend.build_payload(kw_list, timeframe='today 12-m', geo = 'GB', cat = 71)

        interest_over_time_df = pytrend.interest_over_time()
        print(interest_over_time_df.head())


        sns.set(color_codes=True)
        dx = interest_over_time_df.plot.line(figsize = (9,6), title = "Interest Over Time")
        dx.set_xlabel('Date')
        dx.set_ylabel('Trends Index')
        dx.tick_params(axis='both', which='major', labelsize=13)
        dx.figure.savefig("static/output.png")

        return(poplist)


    def pop2(lists):
        from pytrends.request import TrendReq
        

        # Create pytrends object, request data from Google Trends
        pytrends = TrendReq(hl='en-US', tz=360)

        # Extracts data based on our keywords
        kw_list=lists
        pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

        # Specify, get, and normalize data
        data = pytrends.interest_over_time()
        data.drop('isPartial', axis=1, inplace=True)
        normData = data.apply(lambda x: x / x.max(), axis=0)

        # Max normalized value from most recent date + index in list
        recent = normData.values[-1].tolist()
        max_value = max(recent)
        max_index = recent.index(max_value)

        # Name of most popular normalized item
        out = kw_list[max_index]
        pytrends.build_payload(kw_list=[out], cat=0, timeframe='today 5-y', geo='', gprop='')
        trend = pytrends.related_queries()
        trend_list = trend[out]['top']['query']

        # Adds variable number of hashtags to topList
        numHashtags = 5
        topList = []
        for i in range(numHashtags):
            topList.append(trend_list[i])

        # TopList is a list of hashtags, out is most popular item
        
        poplist=out
        return(poplist)

    
        


    input1()
    list2=[]
    for item in paths:
        a=google_predict(item)
        list1=a["name"].tolist()
        list2.append(statistics.mode(list1))
        
    if len(list2)==0:
        print("hello world")
        
    else:
        df2 = pd.DataFrame(list(zip(list2, paths)), columns =['Name', 'path'])
        print("List2 is", list2)
        print("df2 is: ",df2)
        
        poplist2=pop(list2)
        poplist3=pop2(list2)
        print("poplist2 is" ,poplist2)
        print("poplist3 is" ,poplist3)
        index = list2.index(poplist3)
        
        
        path2=os.path.join("../static",paths[index])
        print(path2)
        import autoit
        from time import sleep
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.action_chains import ActionChains

        username = instausername #Enter your username
        password = instapassword #Enter your password
        image_path = os.path.join(parent_dir,paths[index]) #The written path is just an example, Delete the path and Enter the Path of your image. #1. path should not start with a back slash
        caption = f"Hey everyone! We are currently selling our new batch of {poplist3}. Come down to {instausername} to purchase some.    Tags: {poplist2}" #Enter the caption 

        mobile_emulation = { "deviceName": "Pixel 2" }
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option("mobileEmulation", mobile_emulation)

        driver = webdriver.Chrome(executable_path=r"C:\covid-copy2\chromedriver.exe",options=opts) #you must enter the path to your driver

        main_url = "https://www.instagram.com"
        driver.get(main_url)

        sleep(4)

        def login():
            login_button = driver.find_element_by_xpath("//button[contains(text(),'Log In')]")
            login_button.click()
            sleep(3)
            username_input = driver.find_element_by_xpath("//input[@name='username']")
            username_input.send_keys(username)
            password_input = driver.find_element_by_xpath("//input[@name='password']")
            password_input.send_keys(password)
            password_input.submit()

        login()

        sleep(4)

        def close_reactivated():
            try:
                sleep(2)
                not_now_btn = driver.find_element_by_xpath("//a[contains(text(),'Not Now')]")
                not_now_btn.click()
            except:
                pass

        close_reactivated()

        def close_notification():
            try: 
                sleep(2)
                close_noti_btn = driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")
                close_noti_btn.click()
                sleep(2)
            except:
                pass

        close_notification()

        def close_add_to_home():
            sleep(3) 
            close_addHome_btn = driver.find_element_by_xpath("//button[contains(text(),'Cancel')]")
            close_addHome_btn.click()
            sleep(1)

        close_add_to_home()

        sleep(3)

        close_notification()

        new_post_btn = driver.find_element_by_xpath("//div[@role='menuitem']").click()
        sleep(1.5)
        autoit.win_active("Open") 
        sleep(2)
        autoit.control_send("Open","Edit1",image_path) 
        sleep(1.5)
        autoit.control_send("Open","Edit1","{ENTER}")

        sleep(2)

        next_btn = driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()

        sleep(1.5)

        caption_field = driver.find_element_by_xpath("//textarea[@aria-label='Write a caption…']")
        caption_field.send_keys(caption)

        share_btn = driver.find_element_by_xpath("//button[contains(text(),'Share')]").click()

        sleep(25)
        driver.close()

    
        len2=len(poplist2)

       
    return render_template('dashboard.html',caption=caption,path2=path2,poplist2=poplist2,len2=len2)

if __name__ == '__main__':
    app.run(debug=True)


