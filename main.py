import time,csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import threading


BASE_URL = "https://www.usu.ac.id/id/direktori"
TIMEOUT = 10
headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

def get_faculties(driver):
    res = []
    faculties = driver.find_element(By.CLASS_NAME, 'hero-search__fakultas')
    for f in driver.find_elements(By.TAG_NAME,'option'):
        if f.text not in ['Semua Fakultas', 'Inbound']:
            res.append(f.text)
    #print(res)
    return res

def get_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options = chrome_options)
    return driver

def get_docents(driver,select,faculties):
    docents = {}
    with open('data.csv','w',newline='') as f:
        writer = csv.writer(f)

        for fac in faculties:
            faculty = select.select_by_value(fac)
            time.sleep(10)
            cari_btn = driver.find_element(By.CLASS_NAME, 'btn-yellow')
            cari_btn.click()
            #time.sleep(30)
            #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(30)
            docents[fac] = []
            profile_cards = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located(By.CLASS_NAME, 'profile-card'))
            for profile in profile_cards:
                docents[fac].append(profile.find_element(By.TAG_NAME,'h6').text)
                row = fac, profile.find_element(By.TAG_NAME,'h6').text
                print('row',row)
                if row:
                    writer.writerow(row)
                f.flush()

            #driver.back()
            time.sleep(10)
        return docents

def select_data(faculty,docent,writer,csvfile):
    driver = get_driver()
    driver.get(BASE_URL)
    time.sleep(2)
    try:
        #WebDriverWait(driver, 10).until(EC.element_to_be_selected(By.CLASS_NAME, 'hero-search__fakultas'))
        faculties = driver.find_element(By.CLASS_NAME, 'hero-search__fakultas')
        time.sleep(2)
        select = Select(faculties)
        time.sleep(2)
        select.select_by_value(faculty)
        time.sleep(10)
    except:
        driver.refresh()
        faculties = driver.find_element(By.CLASS_NAME, 'hero-search__fakultas')
        select = Select(faculties)
        select.select_by_value(faculty)
        time.sleep(10)
    finally:
        print(driver.current_url)
        print('Cannot find',faculty,docent)

    try:
        #WebDriverWait(driver, 30).until(EC.element_to_be_clickable(By.CLASS_NAME, 'btn-yellow'))
        cari_btn = driver.find_element(By.CLASS_NAME, 'btn-yellow')
        cari_btn.click()
        time.sleep(10)
    except:
        print('Failed to locate cari_btn..')
    docents = driver.find_elements(By.TAG_NAME, 'h6')
    #print('docents',docents)
    for d in docents:
        try:
            if d.text == docent:
                d.click()
                time.sleep(10)
                name = driver.find_element(By.CLASS_NAME, 'name').text
                data_items = driver.find_elements(By.CLASS_NAME, 'hero-biodata-datapegawai-items')
                for d in data_items:
                    if d.text.startswith('NIP'):
                        nip = d.text.split(':')[1].strip()
                    elif d.text.startswith('NIDN'):
                        nidn = d.text.split(':')[1].strip()
                    else:
                        email = d.text.split(':')[1].strip()
                
                expertises = ''
                for e in driver.find_elements(By.CLASS_NAME, 'hero-expertise'):
                    expertises += e.text+' '
                bio = driver.find_element(By.CLASS_NAME, 'bio').text
                profile_url = driver.current_url
                print(f"""
Name        : {name}
NIP         : {nip}
NIDN        : {nidn}
Email       : {email}
Expertises  : {expertises}
Bio         : {bio}
Profile URL : {profile_url}
                      """)
                row = name, faculty, nip, nidn, email, expertises, bio, profile_url
                print(row)
                writer.writerow(row)
                csvfile.flush()
        except:
            pass
if __name__ == '__main__':
    #driver = get_driver()
    #driver.get(BASE_URL)
    #time.sleep(2)
    #select = Select(driver.find_element(By.CLASS_NAME, 'hero-search__fakultas'))

    #faculties = get_faculties(driver)
    #docents = get_docents(driver,select, faculties)
    
    #driver = get_driver()

    with open('input.csv', newline='') as input_file:
        with open('output.csv','w',newline='') as output_file:
            writer = csv.writer(output_file)
            header = 'Name', 'Faculty','NIP','NIDN', 'Email', 'Expertises', 'Bio', 'Profile URL'
            writer.writerow(header)

            for row in csv.reader(input_file):
                #driver.get(BASE_URL)
                faculty, docent = row
                #select_data(faculty, docent,writer,output_file)

                try:
                    #print('7'+tingkat+area+d)
                    t = threading.Thread(target=select_data, args=[faculty, docent,writer,output_file])
                    t.start()
                    time.sleep(10)
                    threads.append(t)
                    for thread in threads:
                        thread.join()
                    threads = []  
                except:
                    pass 