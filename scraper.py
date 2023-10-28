from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape(baseurl, outputdir, pagefile, username, password):
    driver = webdriver.Chrome()
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    driver.get(baseurl)

    # skip DSGVO screen
    # <button type='submit' name='accept-individual' value='1' class='btn btn-primary'>Einstellungen speichern</button>
    driver.find_element('name', 'accept-individual').click()

    # login username
    # <input type='text' name='login_rufnummer' id='login_rufnummer' class='form-control' ...
    driver.find_element('id', 'login_rufnummer').send_keys(username)

    # login password
    # <input type='password' name='login_passwort' id='login_passwort' class='form-control' required=''>
    driver.find_element('id', 'login_passwort').send_keys(password)

    # <button type='submit' class='btn btn-primary'>Anmelden</button>
    driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()

    found = True
    page = 0
    while found:
        page = page + 1
        driver.get(baseurl + f'app/datentransfers.php?page={page}')

        content = driver.page_source

        found = 'list-group-item' in content
        if found:
            filename = pagefile.replace('{page}', str(page))
            outputfile = Path(outputdir)
            outputfile.mkdir(parents=True, exist_ok=True)
            outputfile = outputfile / filename
            with open(outputfile, 'w', encoding='utf-8') as text_file:
                text_file.write(content)
