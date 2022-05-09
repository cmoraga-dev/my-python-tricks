###################################
#### Main file ####################
##### By cmoraga-dev ##############


##### 0
# Dictionary iteration functions
# enumerate function -> allows to iterate an object using a numeric index and the original index
# Useful to get the previous and next node inside the loop
# Example:

exampleDict = {12:{'some': 'dictionary'}}

for index, key in enumerate(exampleDict):
            # Like arrays, start position would be 0. To get the last index, we can use -1.
            startPosition   = index == 0
            endPosition     = index == len(exampleDict) -1

            # This is a logic to get the previous and next node, preventing out of bounds based on position
            # However, there is some logic duplicated here.
            if startPosition:
                nextKey                 = list(exampleDict.keys())[index+1]
                duplicatedToTheRight    = exampleDict[key]['type'] == exampleDict[nextKey]['type']
                duplicatedToTheLeft     = False
            elif endPosition: 
                prevKey                 = list(exampleDict.keys())[index-1]
                duplicatedToTheLeft     = exampleDict[key]['type'] == exampleDict[prevKey]['type']
                duplicatedToTheRight    = False
            else:
                prevKey                 = list(exampleDict.keys())[index-1]
                nextKey                 = list(exampleDict.keys())[index+1]
                duplicatedToTheLeft     = exampleDict[key]['type'] == exampleDict[prevKey]['type']
                duplicatedToTheRight    = exampleDict[key]['type'] == exampleDict[nextKey]['type']

# End loop

# In a nested dictionary, get the key with the highest/lowest inner value. 
# This is like vlookup in excel (?)
max(exampleDict, key=lambda v: exampleDict[v]['some_inner_key'])

# I needed something like this, but I couldn't find it on Python.
# So I found this, added some little adjustments, and it does the trick :D
def isNumber (n):
    '''
    Custom function. Works with almost every object - as far as I know.
    '''
    try:
        float(n)
        return True
    except (ValueError, TypeError):
        return False


    '''
    THIS IS SOME CODE FOR SCRAPPING WITH SELENIUM, NOT USING IT RIGHT NOW IN THE PROJECT.
    Example of move with offset function of Selenium 

    def checkCandles (driver: WebDriver, ticker):
    
        print (ticker)
        tickerInputForChart = driver.find_element_by_xpath('//*[@id="trading-chart-input-symbol-1"]')
        tickerInputForChart.clear()
        tickerInputForChart.send_keys(ticker)
        tickerInputForChart.send_keys(Keys.ENTER)
        driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})', tickerInputForChart)
        time.sleep(1)


        # Action    
        action = webdriver.ActionChains(driver)

        # get IDs
        # //*[@id="fcMain1"]/div[2]/div/div
        chartElements = driver.find_elements_by_xpath('//*[@id="fcMain1"]/div[2]/div/div/.//*')
        ids = []
        for webElement in chartElements:
            if webElement.get_attribute('class') == 'fc-panel-box':
                ids.append((webElement.get_attribute('id')))
                continue

        # move from last candle to first
        chart = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH ,'//*[@id="fcMain1"]')))
        print (chart.size)
        #print (chart.location)
        action.move_to_element_with_offset(chart, 793, 285).perform()
        position = 793        
        while position > 0:
            position = position - 16
            if position < 0: break         
            try:
                date = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH ,f'//*[@id="{ids[0]}"]/div[1]/div[2]')))
                print (date.text)
                #action.move_by_offset(-8, 0)
                action.move_to_element_with_offset(chart, position, 285).perform()
                action.perform()
            except TimeoutException:
                tickerInputForChart.clear()
                tickerInputForChart.send_keys(ticker)
                tickerInputForChart.send_keys(Keys.ENTER)
                print (WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH ,f'//*[@id="{ids[0]}"]/div[1]/div[2]'))).text)
    '''


