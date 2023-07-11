def scrape_jobs():
    # Setup Selenium
    options = Options()
    options.add_argument("--headless")  # Ensure GUI is off
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    webdriver_service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=webdriver_service, options=options)

    # Go to the website
    driver.get('https://careers.homedepot.com/job-search-results/?keyword=Data%20Analyst&fuzzy=false')

    # Find all job postings
    jobs = driver.find_elements(By.CLASS_NAME, 'search-job-listing__title')

    # Extract the job titles
    job_titles = [job.text for job in jobs if job.text.strip().lower() == 'data analyst']

    driver.quit()

    return job_titles
