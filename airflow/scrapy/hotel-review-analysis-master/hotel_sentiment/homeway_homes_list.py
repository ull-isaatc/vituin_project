# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, os
import unicodecsv as csv
from elasticsearch import Elasticsearch


driver = webdriver.Chrome()


exceptionErrorItem=False
es = Elasticsearch(
    [
        'elastic:vituinproject@elasticsearch:9200/',
    ]
)


#Fields where data will be write
homeway_files='homeway_homes_list.csv'
CSVdir='/usr/local/airflow/scrapy-hotels/hotel-review-analysis-master/classify_elastic/unstructured_data'
homeway_files = os.path.join(CSVdir, homeway_files)

#Arrays will be save the dada
samples_homes=[]
samples_homes.append(["id_homeway", "title", "url"])


index_homes=1


contador = 0
load = False

#It could be that no load at first
while load is False and contador <= 5:
    load = True
    try:
        url = 'https://www.homeaway.es/results/region:1976/@28.33705961045927,-16.61179916612673,28.48894858941568,-16.464631721897604,12z?petIncluded=false&ssr=true&legacyRegionPath=canarias&legacyRegionPath=puerto-de-la-cruz'
        driver.get(url)
        time.sleep(1)
        next = True
        i=0

        contador = 0

        while next == True:
            load = False
            while load is False:
                try:
                    load = True
                    i+=1
                    last_page = driver.find_element_by_xpath("//div[@class='ResultsCount']").text
                    print 'Page', last_page
                    print '-----Pagina '+str(i)+'------'
                    links = driver.find_elements_by_xpath("//h4[contains(@class, 'HitInfo__headline')]")
                    samples_homes_tmp = []
                    #print links
                    for link in links:
                        name = link.text
                        link=link.get_attribute('href')
                        id_homeway = link[1:]
                        link='https://www.homeaway.es'+link
                        print 'nombre =',name,'| id =', id_homeway
                        print 'link =',link
                        samples_homes_tmp.append([id_homeway, name, link])
                        index_homes+=1
                    print '-----Fin página '+str(i)+'------'
                    contador = 0
                    samples_homes.extend(samples_homes_tmp)
                except Exception as error:
                    load = False
                    print 'Error elementos de la pagina. Contador', contador, ', error', error
                    contador += 1
                    if contador > 5:
                        load = True
                        contador = 0
                    time.sleep(1)
                    pass
            load = False
            while load is False:
                try:
                    load = True
                    new_page = driver.find_element_by_xpath("//button[@label='Next page']")
                    new_page.click()
                except Exception as error:
                    load = False
                    print 'Error cargar siguiente. Contador', contador, ', error', error
                    contador += 1
                    if contador > 5:
                        contador = 0
                        load = True
                    print 'Contador,', contador, 'load', load
                    time.sleep(1)
                    pass
                print 'nooooo'
            print 'ehhh'
            load = False
            while load is False:
                try:
                    load = True
                    current_page = driver.find_element_by_xpath("//div[@class='ResultsCount']").text

                    print 'Current',current_page, ', last', last_page
                    contador = 0
                    if last_page!=current_page:
                        pass
                    else:
                        print 'Fin'
                        next = False

                except Exception as error:
                    load = False
                    print 'Error ver pagina actual. Contador', contador, ', error', error
                    contador += 1
                    if contador > 5:
                        load = True
                        contador = 0
                    time.sleep(1)
                    pass

    except Exception as error:
        print 'No Load', contador, ', error', error
        driver.close()
        #chromedriver dont stop itself
        os.system("pkill -f chromedriver")
        load = False
        contador += 1
        pass



driver.close()
#chromedriver dont stop itself
os.system("pkill -f chromedriver")


print('--------------')
print(samples_homes[0])
print('Write ' + str(index_homes-1) + ' homeway homes')


#It writes the comments and posts files
with open(homeway_files, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(samples_homes)