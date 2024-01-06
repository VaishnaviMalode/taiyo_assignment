import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import plotly.express as px
import schedule
import time

def scrape_caltrans_projects():
    url1 = 'https://dot.ca.gov/programs/design/lap/lap-archive'
    response = requests.get(url1)
	
def scrape_enr_projects():
    url2 = 'https://www.enr.com/california/construction_cities'
    response = requests.get(url2)

def scrape_constructionwire_projects():
    url3 = 'https://www.constructionwire.com/Report'
    response = requests.get(url3)

def scrape_bidclerk_projects():
    url4 = 'https://projects.constructconnect.com/bidclerk'
    response = requests.get(url4)

def scrape_dodge_projects():
    url5 = 'https://www.construction.com/projects/'
    response = requests.get(url5)

def scrape_and_visualize_all():
    try:
        # Scraping data from all sources
        scrape_caltrans_projects()
        scrape_enr_projects()
        scrape_constructionwire_projects()
        scrape_bidclerk_projects()
        scrape_dodge_projects()

        # Data cleaning, handling missing values, and normalization using pandas
        df['Project_Title'].fillna('Unknown Title', inplace=True)
        df['Project_Description'].fillna('No description available', inplace=True)

        # Save the cleaned data to a CSV file
        cleaned_data.to_csv('cleaned_projects_data.csv', index=False)

        # Visualization using Matplotlib
        plt.figure(figsize=(10, 6))
        cleaned_data['Project_Title'].value_counts().plot(kind='bar', color='skyblue')
        plt.title('Number_of_Projects_by_Title')
        plt.xlabel('Project_Title')
        plt.ylabel('Number_of_Projects')
        plt.savefig('projects_bar_chart.png')

        # Visualization using Plotly
        fig = px.pie(cleaned_data, names='Project_Title', title='Distribution_of_Projects_by_Title')
        fig.write_html('projects_pie_chart.html')

	except Exception as e:
        # Handle potential issues during scraping
        print(f"Error during data scraping and visualization: {str(e)}")

# Schedule the job to run every 24 hours
schedule.every(24).hours.do(scrape_and_visualize_all)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)

