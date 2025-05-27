from selenium import webdriver
from selenium.webdriver.edge.service import Service
from bs4 import BeautifulSoup
import time
import datetime
import re
import os

def fetch_questions(url):
    service = Service("D:\\OneDrive - HUCE\\2_Code\\Python\\Craw_data\\msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    content = soup.find('div', class_='entry-content')
    if not content:
        print("Unable to find the main content.")
        return []

    questions = []
    current_question = None

    for element in content.find_all(['p', 'div']):
        text = element.get_text(strip=True)
        text = text.replace('View Answer', '')

        if element.name == 'p' and text.strip().startswith(tuple(str(i) + "." for i in range(1, 100))):
            parts = re.split(r'([a-d]\))', text)
            question_text = parts[0].strip()
            options = []
            for i in range(1, len(parts)-1, 2):
                if parts[i] and parts[i+1]:
                    option_letter = parts[i][0].upper()
                    option_text = parts[i+1].strip()
                    options.append((option_letter, option_text))
            current_question = (question_text, options)

        elif element.name == 'div' and 'collapseomatic_content' in element.get('class', []):
            answer_text = element.get_text(strip=True)
            answer_match = re.search(r'Answer:\s*([a-d])', answer_text, re.IGNORECASE)
            if answer_match:
                answer_text = answer_match.group(1)
            if current_question:
                questions.append((*current_question, answer_text))
                current_question = None

    return questions

def save_to_markdown(questions, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for i, (question, options, answer) in enumerate(questions, 1):
            question_clean = re.sub(r'^\d+\.\s*', '', question)
            f.write(f"# {question_clean}\n\n")
            for option_letter, option_text in options:
                marker = "*" if option_letter.lower() == answer.lower() else "-"
                f.write(f"{marker} ```\n  {option_text}\n  ```\n\n")

def main():
    input_file = 'urls.txt'
    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' not found.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        questions = fetch_questions(url)
        if not questions:
            print("No questions found. Please check the HTML structure or URL.")
        else:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{timestamp}.md"
            save_to_markdown(questions, filename)
            print(f"Markdown file created with {len(questions)} questions. Filename: {filename}")

if __name__ == '__main__':
    main()
