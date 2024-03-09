import requests
import bs4
from bs4 import BeautifulSoup

def get_content(chaptertarget):
    req = requests.get(url=chaptertarget, headers={
        "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
    })
    req.encoding = 'utf-8'
    soup = BeautifulSoup(req.text, 'html.parser')
    chapter_content = soup.find('div', {'class': 'chapter_content'})
    content = chapter_content.text
    return content


if __name__ == '__main__':
    book_name = "三国演义.txt"
    server = 'https://www.shicimingju.com'
    target = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    req = requests.get(url=target, headers={
        "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
    })
    req.encoding = 'utf-8'
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'html.parser')
        chapters = soup.find('div', {'class': 'book-mulu'})
        chapters = chapters.find_all('a')
        for chapter in chapters:
            chapter_name = chapter.string
            url = chapter.get('href')
            content = get_content(server+url)
            with open(book_name, 'a', encoding='utf-8') as f:
                f.write(chapter_name)
                f.write('\n')
                f.write('\n'.join(content))
                f.write('\n')

    else:
        print("unable to get the target")
        print(req.status_code)
